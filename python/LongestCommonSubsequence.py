def lcs(string1, string2):
    if len(string1) == 0 or len(string2) == 0:
        return 0
    if string1[-1] == string2[-1]:
        return 1 + lcs(string1[:-1], string2[:-1])
    return max(
        lcs(string1[:-1], string2), lcs(string1, string2[:-1])
    )


def lcsForArray(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return 0
    if arr1[0] == arr2[0]:
        return lcsForArray(arr1[1:], arr2[1:]) + 1
    return max(
        lcsForArray(arr1, arr2[1:]),
        lcsForArray(arr1[1:], arr2)
    )


if __name__ == "__main__":
    string1 = "ABCDGH"
    string2 = "AEDFHR"
    print(lcs(string1, string2))
    arr1 = list(string1)
    arr2 = list(string2)
    print(lcsForArray(arr1, arr2))
