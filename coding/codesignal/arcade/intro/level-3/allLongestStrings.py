def allLongestStrings(inputArray):
    elements = {}
    for word in inputArray:
        if len(word) in elements.keys():
            elements[(len(word))].append(word)
        else:
            elements[(len(word))] = [word]
    return list(elements[max(elements.keys())])
