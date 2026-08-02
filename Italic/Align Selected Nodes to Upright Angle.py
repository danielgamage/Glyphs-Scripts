#MenuTitle: Align Selected Nodes to Upright Angle
# -*- coding: utf-8 -*-
__doc__ = """
Aligns selected nodes along the upright axis.

Uses the layer’s italic angle when set; otherwise true vertical (0°).
Nodes keep their y positions and are slid horizontally onto a shared upright line.
"""

from GlyphsApp import GSNode
from Foundation import NSPoint
import math

nodes = [obj for obj in Layer.selection if isinstance(obj, GSNode)]
if len(nodes) < 2:
	pass
else:
	slant = math.tan(math.radians(Layer.italicAngle or 0.0))
	# Unslanted x = intercept of each node’s upright line at y = 0
	target = sum(n.position.x - n.position.y * slant for n in nodes) / len(nodes)
	for node in nodes:
		y = node.position.y
		node.position = NSPoint(target + y * slant, y)
