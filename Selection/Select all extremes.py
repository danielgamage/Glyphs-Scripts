#MenuTitle: Select all extremes
# -*- coding: utf-8 -*-
__doc__ = """
Adds all extreme points in the current layer to the layer selection.
"""

from GlyphsApp import Glyphs
from math import atan2, pi
font = Glyphs.font

for path in Layer.paths:
    for i, node in enumerate(path.nodes):
        if node.type == OFFCURVE:
            # Get the source CURVE node
            source_node = path.nodes[i].prevNode
            # Calculate the angle
            angle = atan2(node.y - source_node.y, node.x - source_node.x) * 180 / pi
            if (angle + 360) % 90 == 0:
                # Select the node
                node.prevNode.selected = True
