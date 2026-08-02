#MenuTitle: Copies measurements from master
# -*- coding: utf-8 -*-
__doc__ = """
Copies the measurements (stems) from the selected master to the current master.
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

    selectedMasterIndex = window.popupButton.get()
    selectedMasterId = font.masters[selectedMasterIndex].id
    currentMasterId = font.selectedFontMaster.id

    print(currentMasterId, font.userData["GSDimensionPlugin.Dimensions"][currentMasterId])
    print(selectedMasterId, font.userData["GSDimensionPlugin.Dimensions"][selectedMasterId])

    font.userData["GSDimensionPlugin.Dimensions"][currentMasterId] = font.userData["GSDimensionPlugin.Dimensions"][selectedMasterId]
    # Glyphs.redraw()

window.okButton = Button((10, 40, -10, 20), "OK", callback=buttonCallback)
window.open()


# given objects with structure {id: string, value: float}[], return only a list of ids
