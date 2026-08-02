#MenuTitle: Infill Guides
# -*- coding: utf-8 -*-
__doc__ = """
Creates a shape from the intersections of selected guides
"""

import math
from Foundation import NSPoint

# Get selected guides
selected_guides = [obj for obj in Layer.selection if obj.__class__.__name__ == 'GSGuide']

if len(selected_guides) < 3:
    print("Please select at least 3 guides to find intersections")
else:
    # Find all intersection points
    intersections_by_guide = {i: [] for i in range(len(selected_guides))}

    for i in range(len(selected_guides)):
        for j in range(i + 1, len(selected_guides)):
            guide1 = selected_guides[i]
            guide2 = selected_guides[j]

            angle1 = math.radians(guide1.angle)
            angle2 = math.radians(guide2.angle)

            # Skip parallel guides
            if abs(angle1 - angle2) < 0.001 or abs(abs(angle1 - angle2) - math.pi) < 0.001:
                continue

            x1, y1 = guide1.position.x, guide1.position.y
            x2, y2 = guide2.position.x, guide2.position.y

            # Calculate intersection
            if abs(math.cos(angle1)) < 0.001:  # guide1 is vertical
                x_intersect = x1
                y_intersect = math.tan(angle2) * (x1 - x2) + y2
            elif abs(math.cos(angle2)) < 0.001:  # guide2 is vertical
                x_intersect = x2
                y_intersect = math.tan(angle1) * (x2 - x1) + y1
            else:
                tan1, tan2 = math.tan(angle1), math.tan(angle2)
                x_intersect = (y2 - y1 + tan1 * x1 - tan2 * x2) / (tan1 - tan2)
                y_intersect = tan1 * (x_intersect - x1) + y1

            point = NSPoint(x_intersect, y_intersect)
            intersections_by_guide[i].append(point)
            intersections_by_guide[j].append(point)

    if not any(intersections_by_guide.values()):
        print("No intersections found between selected guides")
    else:
        # Deduplicate points
        def points_equal(p1, p2, tol=0.01):
            return abs(p1.x - p2.x) < tol and abs(p1.y - p2.y) < tol

        unique_points = []
        for points in intersections_by_guide.values():
            for point in points:
                if not any(points_equal(point, p) for p in unique_points):
                    unique_points.append(point)

        print(f"Found {len(unique_points)} unique intersection points")

        # Build adjacency graph
        adjacency = {i: [] for i in range(len(unique_points))}

        for guide_idx, points in intersections_by_guide.items():
            if len(points) < 2:
                continue

            # Sort points along guide direction
            angle = math.radians(selected_guides[guide_idx].angle)
            key_func = (lambda p: p.x) if abs(math.cos(angle)) > abs(math.sin(angle)) else (lambda p: p.y)
            sorted_points = sorted(points, key=key_func)

            # Connect consecutive points
            for k in range(len(sorted_points) - 1):
                idx1 = next(i for i, p in enumerate(unique_points) if points_equal(p, sorted_points[k]))
                idx2 = next(i for i, p in enumerate(unique_points) if points_equal(p, sorted_points[k + 1]))
                if idx2 not in adjacency[idx1]:
                    adjacency[idx1].append(idx2)
                    adjacency[idx2].append(idx1)

        # Find minimal cycles using right-hand rule
        def find_minimal_cycles():
            seen = set()
            cycles = []

            for start in range(len(unique_points)):
                for next_node in adjacency[start]:
                    if (start, next_node) in seen:
                        continue

                    path = [start, next_node]
                    current = next_node

                    while True:
                        candidates = [n for n in adjacency[current] if n != path[-2]]
                        if not candidates:
                            break

                        # Choose rightmost turn
                        prev, curr = unique_points[path[-2]], unique_points[current]
                        def turn_angle(n):
                            nxt = unique_points[n]
                            return (math.atan2(nxt.y - curr.y, nxt.x - curr.x) -
                                    math.atan2(curr.y - prev.y, curr.x - prev.x)) % (2 * math.pi)

                        next_node = min(candidates, key=turn_angle)

                        if next_node == start and len(path) >= 3:
                            # Normalize cycle to avoid duplicates
                            min_idx = path.index(min(path))
                            norm = tuple(path[min_idx:] + path[:min_idx])
                            norm_rev = tuple([norm[0]] + list(reversed(norm[1:])))

                            if norm not in seen and norm_rev not in seen:
                                cycles.append(path[:])
                                seen.add(norm)
                            break

                        if next_node in path:
                            break

                        path.append(next_node)
                        current = next_node

                    seen.add((start, path[1] if len(path) > 1 else start))

            return cycles

        cycles = find_minimal_cycles()

        # Create paths
        for cycle in cycles:
            if len(cycle) >= 3:
                new_path = GSPath()
                for idx in cycle:
                    node = GSNode()
                    node.position = unique_points[idx]
                    node.type = 'line'
                    new_path.nodes.append(node)
                new_path.closed = True
                Layer.shapes.append(new_path)

        print(f"Created {len(cycles)} polygons")
