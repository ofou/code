def makeArrayConsecutive2(statues):
    result = 0
    statues.sort()
    for i, statue in enumerate(statues):
        if (i < len(statues)-1):
            result += statues[i+1] - statues[i] - 1
    return result
