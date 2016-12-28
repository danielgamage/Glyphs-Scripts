#MenuTitle: Move Selection Up 100 Units at Italic Angle
# -*- coding: utf-8 -*-
__doc__ = """
Moves selection in the direction of the italic angle
"""

import math
import Cocoa

globalHeight = 100


def getWidth(italicAngle, height):
    # subtract from 90 since 90º is upright
    angle = math.radians(90 - master.italicAngle)
    width = height / math.tan(angle)
    return width

for master in Font.masters:
    if master.name == Layer.name:
        globalWidth = getWidth(master.italicAngle, globalHeight)

for node in Layer.selection:
    newPoint = Cocoa.NSMakePoint(node.position.x + globalWidth, node.position.y + globalHeight)
    node.setPosition_(newPoint)
