#MenuTitle: Convert Selected Nodes to Lines
# -*- coding: utf-8 -*-
__doc__ = """
If you're selecting off-curves, select ALL off-curve nodes in a path segment.
"""

for node in Layer.selection:
    node.type = "line"
    node.nextNode.type = "line"
