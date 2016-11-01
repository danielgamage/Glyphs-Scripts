This document is separated by group. Within each folder you'll find scripts for different occasions.

## Font

##### Replace glyphs with ss01
You may find this helpful if your roman font has upright italics in ss01 (for say, `a`, `g`, and `y`). Save a new font and run this to replace your default letters with their ss01 set counterparts.

##### Copy layer from italic
Mostly taken from mekkablue's [Copy Layer to Layer script](https://github.com/mekkablue/Glyphs-Scripts/blob/master/Masters/Copy Layer to Layer.py), this copies the entire layer of a glyph from an italic counterpart. Useful for quickly syncing changes between roman and oblique.

## Nodes

##### Convert Selected Nodes to Lines
Converts selected nodes to `line`-type nodes. Make sure you know how path segments (especially curves) are calculated in Glyphs, as this can create some odd results.

##### Convert Selected Nodes to Offcurves
Converts selected nodes to `offcurve` (handles). If you select two nodes, they'll be converted and the following node will become a curve.

If you execute this on an entire path, you'll get some quadratic curve cages (**experimental**).

##### Split Selected Nodes
Duplicates selected node(s) and separates them away from origin at a 0° or 90° angle. Great for quickly setting up ink traps.

## Subdivision

##### Subdivide Lines to Curves (Catmull-Clark)
Similar to b-spline cages (like very similar), you can draw out line nodes and run this script to convert them to smooth cubic bézier curves. The result after one execution should be identical in shape to the Subdivide Lines (Catmull-Clark) script after three executions, but this will use far fewer nodes.

![](https://pbs.twimg.com/media/CvM1vXrWgAETVor.jpg)

You can also use [Subdivide Filter](https://github.com/danielgamage/Subdivide) to get this functionality in a nondestructive way.

##### Subdivide Lines (Catmull-Clark)
Subdivides path using Catmull-Clark algorithm. With more subdivision, paths will smooth out, but node count will get unwieldy.

##### Subdivide Selection (Add Midpoint)
Adds midpoints to all selected path segments. For line segments, this is akin to faceted subdivision.

## Selection

##### Continue Selection
Infers a selection pattern based on the last two nodes selected and continues that selection.
![](https://github.com/danielgamage/Glyphs-Scripts/blob/master/Images/selection-continue.gif)

##### Grow Selection
Expands the current selection in all paths.
![](https://github.com/danielgamage/Glyphs-Scripts/blob/master/Images/selection-grow.gif)

##### Shrink Selection
Shrinks the current selection in all paths.
![](https://github.com/danielgamage/Glyphs-Scripts/blob/master/Images/selection-shrink.gif)

##### Undo Selection
Removes the most recently selected node from selection.
![](https://github.com/danielgamage/Glyphs-Scripts/blob/master/Images/selection-undo.gif)
