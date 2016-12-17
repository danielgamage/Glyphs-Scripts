#MenuTitle: Split Selected Nodes (Make Inktraps)
# -*- coding: utf-8 -*-
__doc__ = """
Splits nodes into two and separates them by 2 units at 90°-snapped angle.
Great for making inktraps fast.
"""

import Cocoa
import math
import copy

def translateNode(node, distance):
    path = node.parent
    angleFloat = path.tangentAngleAtNode_direction_(node, path.direction) + (90 * path.direction)
    angleSnapped = round(angleFloat / 90) * 90
    # always make corners LESS acute and separate away from vertex
    direction = -1 if angleFloat < angleSnapped else 1
    # convert to radians for translation
    angleSnappedRadians = angleSnapped * (math.pi/180)

    x = node.x + distance * direction * math.cos(angleSnappedRadians)
    y = node.y + distance * direction * math.sin(angleSnappedRadians)
    newPoint = Cocoa.NSMakePoint(x, y)
    return newPoint

for node in Layer.selection:
    path = node.parent
    cloneNode = node.copy()

    # make sure nodes don't go in the same direction
    originPosition = translateNode(node, 1)
    clonePosition = translateNode(node, -1)

    path.insertNode_atIndex_(cloneNode, node.index)

    # make joining path segment a line
    if node.type == "curve":
        node.type = "line"

    # separate nodes from origin
    node.setPosition_(originPosition)
    cloneNode.setPosition_(clonePosition)
