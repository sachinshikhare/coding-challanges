class Solution:
    def countAndSay(self, number: int) -> str:
        if number == 1:
            return "1"

        output = self.countAndSay(number - 1)
        print(output)
        i = 0
        j = 1
        output2 = ""
        while i < len(output):
            continuous = 1
            while j < len(output):
                if output[j] != output[i]:
                    break
                continuous += 1
                j+=1
            output2 += str(continuous) + output[i]
            i = j
            j += 1
        return output2


print(Solution().countAndSay(10))



