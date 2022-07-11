def sortByHeight(people):
    peopleWithTrees = list(
        filter(lambda tree: tree != -1, sorted(people)))[::-1]
    sortedHeights = []
    for element in people:
        if element == -1:
            sortedHeights.append(element)
        else:
            sortedHeights.append(peopleWithTrees.pop())
    return sortedHeights
