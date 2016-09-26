#MenuTitle: Continue Selection
lastNode = Layer.selection[len(Layer.selection) - 1]
originNode = Layer.selection[len(Layer.selection) - 2]

# Get difference of two nodes
if lastNode.index > originNode.index:
    # normal diff
    rhythm = lastNode.index - originNode.index
else:
    # crossing bounds of path
    rhythm = abs(originNode.index - len(originNode.parent.nodes)) + lastNode.index

# Move to node width rhythm
nodeToSelect = lastNode
i = 0
while i < rhythm:
    nodeToSelect = nodeToSelect.nextNode
    i += 1

# Select it
nodeToSelect.selected = True
