#MenuTitle: Add handles to selected path segments
# -*- coding: utf-8 -*-
__doc__ = """
Adds offcurve points to selected straight line path segments.
"""

for node in Layer.selection:
  path = node.parent
  if node.nextNode.selected and node.index != len(path.nodes) - 1 and node.type != 'offcurve' and node.nextNode.type != 'offcurve':
  	offcurve1 = path.insertNodeWithPathTime_(node.index + 1.6667)
  	offcurve2 = path.insertNodeWithPathTime_(node.index + 1.5)
  	offcurve1.type = 'offcurve'
  	offcurve2.type = 'offcurve'
  	node.nextNode.nextNode.nextNode.type = 'curve'
