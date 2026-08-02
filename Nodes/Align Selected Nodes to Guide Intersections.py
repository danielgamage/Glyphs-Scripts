#MenuTitle: Align selected nodes to guide intersections
# -*- coding: utf-8 -*-
__doc__ = """
Aligns selected nodes to intersection points of global guides.
Useful for (eg.) isometric or other nonstandard unit grids.
"""

from GlyphsApp import Glyphs, EDIT_MENU
import functools
import math
from Foundation import NSPoint

selectedPoints = []
intersections = []

print(f"Processing layer: {Layer.name} of glyph: {Layer.parent.name}")

for path in Layer.paths:
	for node in path.nodes: # (or path.anchors etc.)
		if node.selected:
			selectedPoints.append(node)

print(f"Found {len(selectedPoints)} selected nodes")
for i, point in enumerate(selectedPoints):
	print(f"  Node {i+1}: ({point.position.x:.1f}, {point.position.y:.1f})")

def deg_to_rad(deg):
	return deg * math.pi / 180

def get_line_intersection (x0, y0, a0, x1, y1, a1):
	""" returns a (x, y) tuple or None if there is no intersection """
	toRad = math.pi / 180
	if (((a0-a1) % 180) + 180) % 180 == 0:
		return None
	if ((a0 % 180) + 180) % 180 == 90:
		# vertical line at x = x0
		return (x0, math.tan(deg_to_rad(a1)) * (x0-x1) + y1)
	elif ((a1 % 180) + 180) % 180 == 90:
		# vertical line at x = x0
		return (x1, math.tan(deg_to_rad(a0)) * (x1-x0) + y0)
	m0 = math.tan(deg_to_rad(a0)) # Line 0: y = m0 (x - x0) + y0
	m1 = math.tan(deg_to_rad(a1)) # Line 1: y = m1 (x - x1) + y1
	x = ((m0 * x0 - m1 * x1) - (y0 - y1)) / (m0 - m1)
	y = m0 * (x - x0) + y0
	return (x, y)

guides = Glyphs.font.selectedFontMaster.guides
print(f"\nFound {len(guides)} guides in font master")
for i, guide in enumerate(guides):
	print(f"  Guide {i+1}: pos=({guide.position.x:.1f}, {guide.position.y:.1f}), angle={guide.angle}°")

intersection_count = 0
for guide in guides:
	for guideB in guides:
		if guide == guideB:
			continue
		intersection = get_line_intersection(guide.position.x, guide.position.y, guide.angle, guideB.position.x, guideB.position.y, guideB.angle)
		if intersection is not None:
			intersections.append(intersection)
			intersection_count += 1

print(f"\nCalculated {intersection_count} intersection points (with duplicates)")

# update intersections to a list of NSPoints for distance measurement
intersections = list(map(lambda p: NSPoint(p[0], p[1]), list(set(intersections))))
print(f"Unique intersection points: {len(intersections)}")
for i, pt in enumerate(intersections[:10]):  # Show first 10
	print(f"  Intersection {i+1}: ({pt.x:.1f}, {pt.y:.1f})")
if len(intersections) > 10:
	print(f"  ... and {len(intersections) - 10} more")

print(f"\nAligning nodes to nearest intersections:")
for i, selectedPoint in enumerate(selectedPoints):
	nearestPoint = None
	shortestDistance = 1000000.0
	for intersection in intersections:
		dist = distance(intersection, selectedPoint.position)
		if dist < shortestDistance:
			shortestDistance = dist
			nearestPoint = intersection
	print(f"  Node {i+1}: ({selectedPoint.position.x:.1f}, {selectedPoint.position.y:.1f}) -> ({nearestPoint.x:.1f}, {nearestPoint.y:.1f}) [distance: {shortestDistance:.1f}]")
	selectedPoint.position = nearestPoint

print(f"\nAlignment complete!")
