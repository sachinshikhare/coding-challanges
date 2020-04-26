

def findLis(arr1, arr2, lastValue):
    if len(arr1) < 1 or len(arr2) < 1:
        return 0

    if arr1[0] == arr2[0] and arr1[0] > lastValue:
        return 1 + findLis(arr1[1:], arr2[1:])
    return max(
        findLis(arr1[1:], arr2),
        findLis(arr1, arr2[1:])
    )


findLis()