#MenuTitle: Remove Nodes and Try to Keep Shape (from mekkablue)
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
__doc__ = """
Delete the selected on-curve nodes, but try to keep the shape of the path. Hold down Shift for balanced handles.
from https://github.com/mekkablue/Glyphs-Scripts/blob/213986af08376e9919c7daccf85779a9c943fe41/Paths/Remove%20Nodes%20and%20Try%20to%20Keep%20Shape.py
"""

from Foundation import NSEvent
thisFont = Glyphs.font # frontmost font
thisLayer = thisFont.selectedLayers[0] # first of active layers of selected glyphs
thisGlyph = thisLayer.parent # current glyph
selection = thisLayer.selection # node selection in edit mode

# check if Shift is held down:
shiftKeyFlag = 131072
shiftKeyPressed = NSEvent.modifierFlags() & shiftKeyFlag == shiftKeyFlag

if selection:
	selectedNodes = [obj for obj in selection if type(obj) == GSNode and obj.type == GSCURVE]
	if selectedNodes:
		# thisGlyph.beginUndo() # undo grouping causes crashes
		thisLayer.selection = None
		for thisNode in selectedNodes:
			thisPath = thisNode.parent
			if not shiftKeyPressed:
				thisPath.removeNodeCheckKeepShape_(thisNode)
			else:
				thisPath.removeNodeCheckKeepShape_normalizeHandles_(thisNode, True)
		# thisGlyph.endUndo() # undo grouping causes crashes