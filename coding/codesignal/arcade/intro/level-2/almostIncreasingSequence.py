def almostIncreasingSequence(sequence):

    erase = True
    for i in range(len(sequence)-1):
        if sequence[i] < sequence[i+1]:
            pass
        elif sequence[i-1] < sequence[i+1] and erase:
            erase = False
        elif i == 0 and erase:
            erase = False
        elif len(sequence)-2 == i and erase:
            erase = False
        elif sequence[i-1] == sequence[i+1] and erase and sequence[i] != sequence[i+2]:
            erase = False
        else:
            return False
    return True
