#MenuTitle: Undo Selection

# Get last-selected node
lastNode = Layer.selection[len(Layer.selection) - 1]

# Deselect it
lastNode.selected = False
