#MenuTitle: Replace primary glyphs with ssXX
# -*- coding: utf-8 -*-
__doc__ = """
Replaces primary glyphs with ssXX variants, and optionally delete ssXX glyphs
"""


from GlyphsApp import Glyphs
from vanilla import Window, PopUpButton, Button, CheckBox

# Get the current font
font = Glyphs.font

# Get the features that begin with 'ss'
features = [f.fullName() for f in font.features if f.name.startswith('ss')]

# Create a dialog
window = Window((400, 200))
window.popupButton = PopUpButton((10, 10, -10, 20), features)
window.deleteCheckbox = CheckBox((10, 40, -10, 20), "Delete source glyphs", value=False)
window.okButton = Button((10, 40, -10, 20), "OK", callback=buttonCallback)

def buttonCallback(sender):
    window.close()

    featureFullName = window.popupButton.getItems()[window.popupButton.get()]
    # Find the matching `ssXX` for `featureFullName`
    matchingFeature = next(filter(lambda d: d.fullName() == featureFullName, font.features), None)
    stringToMatch = "." + matchingFeature.name

    glyphsToRename = []

    for glyph in font.glyphs:
        if stringToMatch in glyph.name:
            glyphsToRename.append(glyph)

    for glyph in glyphsToRename:
        mainGlyphName = glyph.name.replace(stringToMatch, "")
        mainGlyph = font.glyphForName_(mainGlyphName)

        if window.deleteCheckbox.get():
            # remove main glyph
            font.removeGlyph_(mainGlyph)

        # rename ss01
        glyph.setName_changeName_(mainGlyphName, True)

window.open()