#MenuTitle: Convert Selected Nodes to Offcurves
# -*- coding: utf-8 -*-
__doc__ = """
This is a rather dangerous operation.
Usually used on all nodes of a path to make a closed quad curve.
"""

for node in Layer.selection:
    node.type = "offcurve"
    if len(Layer.selection) == 1:
        node.nextNode.type = "qcurve"
    elif node.nextNode.type != "offcurve":
        node.nextNode.type = "curve"
