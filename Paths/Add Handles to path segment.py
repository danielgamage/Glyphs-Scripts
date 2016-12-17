#MenuTitle: Add handles to selected segments
# -*- coding: utf-8 -*-
__doc__ = """
Adds offcurve points to selected straight line path segments.
"""

for node in Layer.selection:
    path = node.parent
    if node.nextNode.selected and node.type != 'offcurve' and node.nextNode.type != 'offcurve':
        if not (not path.closed and node.index == len(path.nodes) - 1):
            offcurve1 = path.insertNodeWithPathTime_(node.index + 1.6667)
            offcurve2 = path.insertNodeWithPathTime_(node.index + 1.5)
            offcurve1.type = 'offcurve'
            offcurve2.type = 'offcurve'
            node.nextNode.nextNode.nextNode.type = 'curve'
