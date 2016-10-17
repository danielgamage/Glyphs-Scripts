#MenuTitle: Subdivide (Faceted)
for path in Layer.paths:
    # store static node count
    nodeCount = len(path.nodes)

    for x in range(1, len(path.nodes) - 1):
        path.insertNodeWithPathTime_(nodeCount - x + 0.5)
