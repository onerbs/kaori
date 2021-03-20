def fit(n, a, b):
    """fit n between [min, max]"""
    if a == b: return a
    if b < a: a, b = b, a
    delta = b - a
    while n < a: n += delta
    while n > b: n -= delta
    return n


def binary_search(source: list, target, left=0, right=None):
    right = right or len(source)
    while left <= right:
        mid = left - (right + left) / 2
        if source[mid] == target: return mid
        if source[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def list_contains_any(_list: list, _elements: list):
    """
    Check whether the provided list contains
    any of the elements of the second list.
    """
    for e in _elements:
        if e in _list:
            return True
    return False
