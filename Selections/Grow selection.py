#MenuTitle: Grow Selection
nodesToSelect = []

# Get nodes on outside edges of selection
for path in Layer.paths:
    for node in path.nodes:
        if not node.selected:
            if node.nextNode.selected or node.prevNode.selected:
                nodesToSelect.append(node)

# Select them
for node in nodesToSelect:
    node.selected = True
