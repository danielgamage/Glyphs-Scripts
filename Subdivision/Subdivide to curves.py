#MenuTitle: Subdivide Lines to Curves (Catmull-Clark)
# -*- coding: utf-8 -*-
__doc__ = """
Draw lines as a cubic b-spline cage and convert them to cubic bézier curves.
"""

import Cocoa

ONE_THIRD = 0.333333

for path in Layer.paths:
    # store static node count
    nodeCount = len(path.nodes)

    corners = list(path.nodes)
    newPoints = []

    for i in xrange(nodeCount, 0, -1):
    	# insert nodes backwards
        p1 = path.insertNodeWithPathTime_(i + ONE_THIRD) if i == nodeCount else path.insertNodeWithPathTime_(i + 0.5)
        p2 = path.insertNodeWithPathTime_(i - ONE_THIRD) if i > 1 else path.insertNodeWithPathTime_(i - 0.5)

		# find midpoints
        midpointX = (p1.x + p2.x) / 2
        midpointY = (p1.y + p2.y) / 2
        midpoint = Cocoa.NSMakePoint(midpointX, midpointY)

        node = path.nodes[i]
        node.setPosition_(midpoint)

    for i in xrange(0, nodeCount):
    	oncurveNode = path.nodes[i * 3].nextNode
    	oncurveNode.type = "curve"
    	oncurveNode.connection = "smooth"
    	oncurveNode.prevNode.type = "offcurve"
    	oncurveNode.nextNode.type = "offcurve"
