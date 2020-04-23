class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [0 for _ in range(len(s))]
        return self.ways(s, 0, len(s), cache)

    def ways(self, string, index, length, cache):

        if index >= length:
            return 1

        if cache[index] != 0:
            print("cache used")
            return cache[index]
        indexChar = int(string[index])
        if indexChar == 0:
            return 0

        result = self.ways(string, index + 1, length, cache)
        if index+1 < length and (indexChar == 1 or (indexChar == 2 and int(string[index+1]) <= 6)):

            result += self.ways(string, index + 2, length, cache)
        cache[index] = result
        return result

print(Solution().numDecodings("226"))