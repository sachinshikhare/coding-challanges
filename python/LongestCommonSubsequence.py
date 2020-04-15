def lcs(string1, string2):

    if len(string1) == 0 or len(string2) == 0:
        return 0
    if string1[-1] == string2[-1]:
        return 1 + lcs(string1[:-1], string2[:-1])
    return max(
        lcs(string1[:-1], string2),lcs(string1, string2[:-1])
    )

if __name__ == "__main__":
    string1 = "ABCDGH"
    string2 = "AEDFHR"
    print(lcs(string1, string2))