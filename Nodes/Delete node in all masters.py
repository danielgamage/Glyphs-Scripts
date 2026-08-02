#MenuTitle: Delete selected nodes in all masters
# -*- coding: utf-8 -*-
__doc__ = """
Deletes the selected nodes in all masters.
"""

from GlyphsApp import *

font = Glyphs.font
glyph = Layer.parent

sourceNode = Layer.selection[0]
sourceNodeIndex = sourceNode.index

for node in Layer.selection:
  sourcePath = node.parent
  sourcePathIndex = list(sourcePath.parent.paths).index(sourcePath)
  for layer in glyph.layers:
    if layer.isMasterLayer:
      path = layer.paths[sourcePathIndex]
      node = path.nodes[sourceNodeIndex]
      node.parent.removeNodeCheckKeepShape_(node)