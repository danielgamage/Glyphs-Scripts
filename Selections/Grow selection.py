#MenuTitle: Grow Selection
nodesToSelect = []
for path in Layer.paths:
    for node in path.nodes:
        if node.selected != True:
            if node.nextNode.selected or node.prevNode.selected:
				nodesToSelect.append(node)
for node in nodesToSelect:
	node.selected = True
