#MenuTitle: Convert selected nodes to offcurves
# -*- coding: utf-8 -*-
__doc__ = """
This is a rather dangerous operation.
Usually used on all nodes of a path to make a closed quad curve.
"""

for node in Layer.selection:
    node.type = "offcurve"
