#MenuTitle: Copy Layer from Italic
# -*- coding: utf-8 -*-
__doc__ = """
Copies layer from either the italic or the upright counterpart.
Mostly from @mekkablue
"""

# most of the code taken from
# https://github.com/mekkablue/ShowItalic/blob/master/ShowItalic.glyphsReporter/Contents/Resources/ShowItalic.py
# and
# https://github.com/mekkablue/Glyphs-Scripts/blob/master/Masters/Copy%20Layer%20to%20Layer.py

def masterHasItalicAngle(thisMaster):
    try:
        if thisMaster.italicAngle == 0.0:
            return False
        else:
            return True
    except Exception as e:
        print( "masterHasItalicAngle: %s" % str(e) )

def italicFontForFont(thisFont):
    try:
        if thisFont:
            familyName = thisFont.familyName
            listOfPossibleFamilyMembers = [ f for f in Glyphs.fonts if f.familyName == familyName and f != thisFont ]
            if len(listOfPossibleFamilyMembers) == 1:
                return listOfPossibleFamilyMembers[0]
            else:
                thisFontIsItalic = masterHasItalicAngle(thisFont.masters[0])
                listOfItalicFamilyMembers = [f for f in listOfPossibleFamilyMembers if masterHasItalicAngle(f.masters[0]) is not thisFontIsItalic]
                if len(listOfItalicFamilyMembers) == 1:
                    return listOfItalicFamilyMembers[0]
        return None
    except Exception as e:
        print( "italicFontForFont: %s" % str(e) )

italicFont = italicFontForFont(Layer.parent.parent)
glyph = Layer.parent
glyphName = glyph.name

uprightMasterID = Layer.associatedMasterId
uprightMasterName = italicFont.masters[uprightMasterID].name.replace("Italic","").strip()

italicGlyph = italicFont.glyphs[glyphName]
# print(italicGlyph.layers[uprightMasterID])
italicMasters = [m for m in italicFont.masters if m.name.startswith(uprightMasterName)]

target = glyph.layers[uprightMasterID]
source = italicGlyph.layers[uprightMasterID]

if len(target.paths) != 0:
    target.paths = []

if len(source.paths) > 0:
    for thisPath in source.paths:
        newPath = thisPath.copy()
        target.paths.append( newPath )
