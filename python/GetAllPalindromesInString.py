def getPalidromesForIndex(string, pivot):
    palindromes = set()
    # palindromes.add(string[pivot])
    minValue = min(pivot, len(string)-pivot)
    evenLegthPivotPresent = False
    oddPaliEnd = False
    evenPaliEnd = False
    if pivot != 0 and string[pivot] == string[pivot-1]:
        palindromes.add(string[pivot-1:pivot+1])
        evenLegthPivotPresent = True
    for counter in range(1, minValue):
        if not oddPaliEnd and string[pivot - counter] == string[pivot + counter]:
            palindromes.add(string[(pivot - counter) : (pivot + counter+1)] )
        else:
            oddPaliEnd = True

        if not evenPaliEnd and evenLegthPivotPresent:
            if string[pivot - counter-1] == string[pivot + counter]:
                palindromes.add(string[(pivot - counter - 1) : (pivot + counter+1)] )
            else:
                evenPaliEnd = True
        if oddPaliEnd and evenPaliEnd:
            break
    return palindromes


def getAllPalindromes(string):
    allPalindromes = set()
    for i in range(len(string)):
        allPalindromes = allPalindromes.union(getPalidromesForIndex(string, i))
    return allPalindromes if len(allPalindromes) > 0 else None


if __name__ == "__main__":
    string = "aba abcba sachin anagha abcdc zabaz abba aa sachin a nihcas"
    print(getAllPalindromes(string))

    print(getAllPalindromes("bc"))