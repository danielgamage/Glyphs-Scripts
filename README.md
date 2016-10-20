# Glyphs-Scripts

## Nodes

### Convert Selected Nodes to Offcurves
Converts selected nodes of any type to `offcurve` (handles). If you select two nodes, they'll be converted and the following node will become a curve.

If you execute this on an entire path, you'll get some TrueType curves (**experimental**).

### Split Selected Nodes
Duplicates selected node(s) and separates them away from origin at a 0° or 90° angle. Great for quickly setting up ink traps.

## Subdivision

### Subdivide Lines to Curves (Catmull-Clark)
Similar to b-spline cages (like very similar), you can draw out line nodes and run this script to convert them to smooth cubic bézier curves. The result after one execution should be identical in shape to the Subdivide Lines (Catmull-Clark) script after three executions, but this will use far fewer nodes.

![](https://pbs.twimg.com/media/CvM1vXrWgAETVor.jpg)

### Subdivide Lines (Catmull-Clark)
Subdivides path using Catmull-Clark algorithm. With more subdivision, paths will smooth out, but node count will get unwieldy.

### Subdivide Selection (Add Midpoint)
Adds midpoints to all selected path segments. For line segments, this is akin to faceted subdivision.

## Selection

### Continue Selection
Infers a selection pattern based on the last two nodes selected and continues that selection.
![](https://github.com/danielgamage/Glyphs-Scripts/blob/master/Images/selection-continue.gif)

### Grow Selection
Expands the current selection in all paths.
![](https://github.com/danielgamage/Glyphs-Scripts/blob/master/Images/selection-grow.gif)

### Shrink Selection
Shrinks the current selection in all paths.
![](https://github.com/danielgamage/Glyphs-Scripts/blob/master/Images/selection-shrink.gif)

### Undo Selection
Removes the most recently selected node from selection.
![](https://github.com/danielgamage/Glyphs-Scripts/blob/master/Images/selection-undo.gif)
