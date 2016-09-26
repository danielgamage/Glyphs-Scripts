#MenuTitle: Shrink Selection
nodesToDeselect = []
for path in Layer.paths:
    for node in path.nodes:
        if node.selected:
            if not node.nextNode.selected or not node.prevNode.selected:
				nodesToDeselect.append(node)
for node in nodesToDeselect:
	node.selected = False
