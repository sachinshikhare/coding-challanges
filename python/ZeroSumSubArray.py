def findZeroSumSurArray(arr):
    currSum = arr[0]
    retSum = arr[0]
    for num in arr:
        currSum = sum(num, currSum)


    pass

# COPIED
def solution(arr):
    sums = {}
    sum = 0
    for i in range(len(arr)):
        oldIndex = sums.get(sum)
        if oldIndex == None and i == len(arr):
            return None
        elif oldIndex == None:
            sums[sum] = i
            sum += arr[i]
        else:
            return arr[oldIndex:i]




# findZeroSumSurArray([1,2,-5,1,2,-1])
print(solution([1,2,-5,1,2,-1]))