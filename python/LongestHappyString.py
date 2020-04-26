
# UNSOLVED


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # while (a > 0 and b > 0) or (b > 0 and c > 0) or (c > 0 and a > 0):
        #     if a > b:
        #         if a > c:
        #             largest = a;
        #         largest = c
        #     elif b > c:
        #         largest = b
        #     else:
        #         largest = c

        dict = {'a': a, 'b': b, 'c': c}

        dict = {k:v for k, v in sorted(item.items(), key=lambda item: item[1])}


        arr = [a,b,c]
        arr = sorted(arr)
        exitFlag = False
        string = ""
        while not exitFlag:
            counter = min(arr[0], 2)
            arr[0] -= counter





