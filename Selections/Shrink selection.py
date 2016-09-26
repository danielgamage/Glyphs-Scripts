#MenuTitle: Shrink Selection
nodesToDeselect = []
for path in Layer.paths:
    for node in path.nodes:
        if node.selected = True:
            if (node.nextNode.selected ^ node.prevNode.selected):
				print node
				nodesToDeselect.append(node)
for node in nodesToDeselect:
	node.selected = False
