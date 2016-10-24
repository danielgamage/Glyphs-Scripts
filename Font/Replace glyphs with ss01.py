#MenuTitle: Replace primary glyphs with ss01
# -*- coding: utf-8 -*-
__doc__ = """
Replaces primary glyph with ss01 variant (if it exists)
"""

glyphsToRename = []
stringToMatch = ".ss01"

for glyph in Font.glyphs:
    if stringToMatch in glyph.name:
        glyphsToRename.append(glyph)

for glyph in glyphsToRename:
    mainGlyphName = glyph.name.replace(stringToMatch, "")
    mainGlyph = Font.glyphForName_(mainGlyphName)

    # remove main glyph
    Font.removeGlyph_(mainGlyph)

    # rename ss01
    glyph.setName_changeName_(mainGlyphName, True)
