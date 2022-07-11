def commonCharacterCount(s1, s2):
    A = {x: sum(len(i) for i in s1 if x == i) for x in list(s1)}
    B = {x: sum(len(i) for i in s2 if x == i) for x in list(s2)}
    U = set(A) & set(B)
    commonCharacterCount = 0
    for a in A:
        if a in U:
            commonCharacterCount += min(A[a], B[a])
    return commonCharacterCount
