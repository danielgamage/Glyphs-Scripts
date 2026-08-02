#MenuTitle: Create Isometric Guides
# -*- coding: utf-8 -*-
__doc__ = """
Creates isometric guides at a given interval and angle, covering the entire glyph.
"""

from GlyphsApp import *
from math import cos, radians, floor, ceil
from vanilla import FloatingWindow, TextBox, EditText, Button

class IsometricGuidesDialog:
    def __init__(self):
        self.w = FloatingWindow((250, 120), "Isometric Guides")

        self.w.intervalLabel = TextBox((10, 15, 80, 20), "Interval:")
        self.w.intervalInput = EditText((100, 12, 140, 22), "100")

        self.w.angleLabel = TextBox((10, 45, 80, 20), "Angle:")
        self.w.angleInput = EditText((100, 42, 140, 22), "30")

        self.w.createButton = Button((10, 80, -10, 20), "Create", callback=self.create_guides)

        self.w.open()

    def create_guides(self, sender):
        try:
            interval = float(self.w.intervalInput.get())
            angle = float(self.w.angleInput.get())
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

        self.w.close()

        # Create guides
        height = Layer.ascender - Layer.descender
        width = Layer.width

        overshoot = width * cos(radians(90 - angle))
        print(f"Height: {height}, Overshoot: {overshoot}")

        yCount = int((height + 2 * overshoot) / interval) + 2
        x = 0
        lowestY = floor((Layer.descender - overshoot) / interval) * interval

        for multiplier in [-1, 1]:
            for y in range(yCount):
                guide = GSGuide()
                guide.x = x * interval
                guide.y = lowestY + y * interval
                guide.angle = angle * multiplier

                Layer.guides.append(guide)

        print(f"Created {yCount * 2} guides")

# Run dialog
IsometricGuidesDialog()
