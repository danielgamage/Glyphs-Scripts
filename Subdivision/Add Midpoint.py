#MenuTitle: Subdivide Selection (Add Midpoint)
# -*- coding: utf-8 -*-
__doc__ = """
Adds a midpoint between selected nodes.
"""

for node in Layer.selection:
    if (node.nextNode.selected):
        path = node.parent
        nodeIndex = path.indexOfNode_(node)
        path.insertNodeWithPathTime_(nodeIndex + 1.5)
