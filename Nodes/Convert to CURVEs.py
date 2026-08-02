#MenuTitle: Convert Selected Nodes to CURVEs
# -*- coding: utf-8 -*-
__doc__ = """
This is a rather dangerous operation.
Usually used on all nodes of a path to make a closed quad curve.
"""

from GlyphsApp import CURVE

for node in Layer.selection:
    node.type = CURVE
