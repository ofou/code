def adjacentElementsProduct(inputArray):
    candidates = []
    for i, num in enumerate(inputArray):
        if i+1 == len(inputArray):
            break
        candidates.append(inputArray[i]*inputArray[i+1])
    return max(candidates)
