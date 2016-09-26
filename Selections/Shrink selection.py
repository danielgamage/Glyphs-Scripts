#MenuTitle: Shrink Selection
nodesToDeselect = []

# Get nodes on inside edges of selection
for path in Layer.paths:
    for node in path.nodes:
        if node.selected:
            if not node.nextNode.selected or not node.prevNode.selected:
				nodesToDeselect.append(node)

# Deselect them
for node in nodesToDeselect:
	node.selected = False
