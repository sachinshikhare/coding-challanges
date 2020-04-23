from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString not in anagrams.keys():
                anagrams[sortedString] = [string]
            else:
                anagrams.get(sortedString).append(string)
        return list(anagrams.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))