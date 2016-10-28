#MenuTitle: Copy Layer from Italic
# -*- coding: utf-8 -*-
__doc__ = """
Quickly copies layer from either the italic or the upright counterpart.
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

def copyPathsFromLayerToLayer( sourceLayer, targetLayer ):
	"""Copies all paths from sourceLayer to targetLayer"""
	numberOfPathsInSource  = len( sourceLayer.paths )
	numberOfPathsInTarget  = len( targetLayer.paths )

	if numberOfPathsInTarget != 0:
		print "- Deleting %i paths in target layer" % numberOfPathsInTarget
		targetLayer.paths = []

	if numberOfPathsInSource > 0:
		print "- Copying paths"
		for thisPath in sourceLayer.paths:
			newPath = thisPath.copy()
			targetLayer.paths.append( newPath )

def copyComponentsFromLayerToLayer( sourceLayer, targetLayer ):
	"""Copies all components from sourceLayer to targetLayer."""
	numberOfComponentsInSource = len( sourceLayer.components )
	numberOfComponentsInTarget = len( targetLayer.components )

	if numberOfComponentsInTarget != 0:
		print "- Deleting %i components in target layer" % numberOfComponentsInTarget
		targetLayer.components = []

	if numberOfComponentsInSource > 0:
		print "- Copying components:"
		for thisComp in sourceLayer.components:
			newComp = thisComp.copy()
			print "   Component: %s" % ( thisComp.componentName )
			targetLayer.components.append( newComp )

def copyAnchorsFromLayerToLayer( sourceLayer, targetLayer ):
	"""Copies all anchors from sourceLayer to targetLayer."""
	numberOfAnchorsInSource = len( sourceLayer.anchors )
	numberOfAnchorsInTarget = len( targetLayer.anchors )

	if numberOfAnchorsInTarget != 0:
		print "- Deleting %i anchors in target layer" % numberOfAnchorsInTarget
		targetLayer.setAnchors_(None)

	if numberOfAnchorsInSource > 0:
		print "- Copying anchors from source layer:"
		for thisAnchor in sourceLayer.anchors:
			newAnchor = thisAnchor.copy()
			targetLayer.anchors.append( newAnchor )
			print "   %s (%i, %i)" % ( thisAnchor.name, thisAnchor.position.x, thisAnchor.position.y )

def copyMetricsFromLayerToLayer( sourceLayer, targetLayer ):
	"""Copies width of sourceLayer to targetLayer."""
	sourceWidth = sourceLayer.width
	if targetLayer.width != sourceWidth:
		targetLayer.width = sourceWidth
		print "- Copying width (%.1f)" % sourceWidth
	else:
		print "- Width not changed (already was %.1f)" % sourceWidth

italicFont = italicFontForFont(Layer.parent.parent)
glyph = Layer.parent
glyphName = glyph.name

uprightMasterID = Layer.associatedMasterId
uprightMasterName = italicFont.masters[uprightMasterID].name.replace("Italic","").strip()

italicGlyph = italicFont.glyphs[glyphName]
italicMasters = [m for m in italicFont.masters if m.name.startswith(uprightMasterName)]

targetlayer = glyph.layers[uprightMasterID]
sourcelayer = italicGlyph.layers[uprightMasterID]

copyPathsFromLayerToLayer( sourcelayer, targetlayer )
copyComponentsFromLayerToLayer( sourcelayer, targetlayer )
copyAnchorsFromLayerToLayer( sourcelayer, targetlayer )
copyMetricsFromLayerToLayer( sourcelayer, targetlayer )
