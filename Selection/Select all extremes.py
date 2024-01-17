#MenuTitle: Select all extremes
# -*- coding: utf-8 -*-
__doc__ = """
Adds all extreme points in the current layer to the layer selection.
"""

from GlyphsApp import Glyphs, CURVE, OFFCURVE, LINE
from math import atan2, pi
font = Glyphs.font

getAngleBetweenPoints = lambda p1, p2: atan2(p2.y - p1.y, p2.x - p1.x) * 180 / pi
isMultipleOf90 = lambda angle: (angle + 360) % 90 == 0

for path in Layer.paths:
    for i, node in enumerate(path.nodes):
        if (node.type == CURVE or node.type == LINE) and (node.prevNode.type == OFFCURVE or node.nextNode.type == OFFCURVE):
            # Calculate the angles
            angle1 = getAngleBetweenPoints(node.prevNode, node)
            angle2 = getAngleBetweenPoints(node, node.nextNode)

            is_extreme = angle1 == angle2 and isMultipleOf90(angle1)
            if is_extreme:
                # Select the node
                Layer.selection.append(node)
