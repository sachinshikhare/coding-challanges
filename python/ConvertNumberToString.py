zero = "zero"
oneToNine = [
    "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
]
tenToTwenty = [
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
]
multiplesOfTen = [
    "", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"
]

exponentials = [
    "", "", [" thousand ", ""], [" million ", " thousand ", ""], [" billion ", " million ", " thousand ", ""]
]

# OPTMIZATION RRQUIRED

def getStringForSignelDigitNumber(input):
    return oneToNine[int(input)]

def getStringForTwoDigitNumber(input):
    input = int(input)
    if input < 10:
        return getStringForSignelDigitNumber(input)
    if input <= 20:
        return tenToTwenty[int(input) - 10]
    input = str(input)
    return multiplesOfTen[int(input[0])] + " " + oneToNine[int(input[1])]

def getStringForThreeDigitNumber(input):
    input = str(int(input))
    firstPartString  = ""
    secondPartString =""
    if len(input) == 3:
        firstPartString = oneToNine[int(input[0])] + " hundred "
        secondPart = str(int(input[1:]))
    else:
        secondPart = str(int(input))

    secondPartString = getStringForSignelDigitNumber(secondPart) if int(secondPart) < 10 else getStringForTwoDigitNumber(secondPart)
    return firstPartString + secondPartString


def convert(input):
    print(input)
    parts = input.split(",")
    if len(parts) == 1:
        if (int(input) == 0):
            return zero
        return getStringForThreeDigitNumber(input)
    partialOutputs = []
    for part in parts:
        partialOutputs.append(getStringForThreeDigitNumber(part))
    exponentialsToUse = exponentials[len(partialOutputs)]
    result = ""
    for cntr in range(0, len(exponentialsToUse)):
        if len(partialOutputs[cntr].strip()) != 0:
            result += partialOutputs[cntr] + exponentialsToUse[cntr]
    return result


if __name__ == "__main__":
    # Assumption: only valid inputs with well formatting and only integers
    print(convert("0"))
    print(convert("1"))
    print(convert("10"))
    print(convert("11"))
    print(convert("20"))

    print(convert("30"))
    print(convert("45"))
    print(convert("100"))
    print(convert("103"))
    print(convert("110"))

    print(convert("1,000"))
    print(convert("1,234"))
    print(convert("10,000"))
    print(convert("15,345"))
    print(convert("99,999"))

    print(convert("100,000"))
    print(convert("123,456"))
    print(convert("12,345,678"))
    print(convert("123,000,678"))
