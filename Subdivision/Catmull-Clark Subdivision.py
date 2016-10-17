#MenuTitle: Subdivide Lines (Catmull-Clark)
import Cocoa

for path in Layer.paths:
    # store static node count
    nodeCount = len(path.nodes)

    corners = list(path.nodes)
    vertexPoints = []

    for i in range(0, nodeCount):
        # midpoints between edgePoints and their vertex neighbors
        midpointOne = path.pointAtPathTime_(i - 0.25) if i != 0 else path.pointAtPathTime_(nodeCount - 0.25)
        midpointTwo = path.pointAtPathTime_(i + 0.25)
        x = (midpointOne.x + midpointTwo.x) / 2
        y = (midpointOne.y + midpointTwo.y) / 2
        vertexPoints.append(Cocoa.NSMakePoint(x, y))

    # add edge points
    for x in range(0, nodeCount):
        path.insertNodeWithPathTime_(nodeCount - x + 0.5)

    # translate corners
    for n in range(0, nodeCount):
        index = (n * 2 - 2) if n > 0 else len(path) - 2
        path.nodes[index].position = vertexPoints[n]
