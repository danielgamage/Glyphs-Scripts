#MenuTitle: Copies sidebearings from master
# -*- coding: utf-8 -*-
__doc__ = """
Copies the sidebearings from the selected master to the current layer.
"""

#1: get the selected layers

from GlyphsApp import Glyphs
from vanilla import Window, PopUpButton, Button, CheckBox

# Get the current font
font = Glyphs.font

# Get the features that begin with 'ss'
masters = [master.name for master in font.masters]

# Create a dialog
window = Window((400, 100))
window.popupButton = PopUpButton((10, 10, -10, 20), masters)

def buttonCallback(sender):
  window.close()
  # get the selected master from popupButton
  selectedMasterIndex = window.popupButton.get()
  selectedMasterId = font.masters[selectedMasterIndex].id
  
  # foreach `Font.selectedLayers`
  for layer in font.selectedLayers:
    glyph = layer.parent
    sourceLayer = glyph.layers[selectedMasterId]
    currentMetrics = (sourceLayer.LSB, sourceLayer.RSB)
    print(currentMetrics)
    layer.LSB, layer.RSB = currentMetrics
  
window.okButton = Button((10, 40, -10, 20), "OK", callback=buttonCallback)
window.open()