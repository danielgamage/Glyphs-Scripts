#MenuTitle: Convert Selected Nodes to OFFCURVEs
# -*- coding: utf-8 -*-
__doc__ = """
This is a rather dangerous operation.
Usually used on all nodes of a path to make a closed quad curve.
"""

from GlyphsApp import OFFCURVE

for node in Layer.selection:
    node.type = OFFCURVE
