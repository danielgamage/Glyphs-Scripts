#MenuTitle: Copy sidebearings to all layers in master
# -*- coding: utf-8 -*-
__doc__ = """
Copies the sidebearings of the current layer to all other layers that share the same master (helpful for smart components)
"""

from GlyphsApp import Glyphs

font = Glyphs.font
currentLayer = font.selectedLayers[0]

# Get the metrics of the current layer
currentMetrics = (currentLayer.LSB, currentLayer.RSB)

# Iterate over all glyphs in the font
for glyph in font.glyphs:
    # Iterate over all layers of the glyph
    for layer in glyph.layers:
        # If the layer shares the same master as the current layer
        if layer.associatedMasterId == currentLayer.associatedMasterId:
            # Copy the metrics to the layer
            layer.LSB, layer.RSB = currentMetrics