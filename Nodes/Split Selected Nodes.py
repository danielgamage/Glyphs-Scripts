#MenuTitle: Split Selected Nodes
# -*- coding: utf-8 -*-
__doc__ = """
Splits nodes into two and separates them by 2 units at 90°-snapped angle
"""

import Cocoa
import math
import copy


def translateNode(node, distance):
    angleFloat = node.parent.tangentAngleAtNode_direction_(node, 1) + 90
    angleSnapped = round(angleFloat / 90) * 90 * (math.pi/180)
    x = node.x + distance * math.cos(angleSnapped)
    y = node.y + distance * math.sin(angleSnapped)
    newPoint = Cocoa.NSMakePoint(x, y)
    return newPoint

for node in Layer.selection:
    path = node.parent
    cloneNode = node.copy()
    originPosition = translateNode(node, 1)
    clonePosition = translateNode(node, -1)

    path.insertNode_atIndex_(cloneNode, node.index)

    # set positions
    node.setPosition_(originPosition)
    cloneNode.setPosition_(clonePosition)
