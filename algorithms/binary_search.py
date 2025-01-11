def binary_search(array, target):
    """
    Binary search algorithm to find the target element in the array.
    Time complexity: O(log n)
    Space complexity: O(1)
    >>> binary_search([1, 2, 3, 4, 5], 3)
    2
    >>> binary_search([1, 2, 3, 4, 5], 6)
    -1
    """
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2  # or low + (high - low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
