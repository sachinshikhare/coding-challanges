from typing import List

# INCOMPLETE
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        seen = set()
        alphabets = "".join(wordList)
        queue = []
        queue.append(beginWord)
        counter = 0
        while len(queue) != 0:
            word = queue.pop(0)
            counter += 1
            for i in range(len(word)):
                for j in alphabets:
                    temp = word[:i] + j + word[i+1:]
                    if temp == word:
                        continue
                    if temp == endWord:
                        return counter + 1
                    elif temp not in seen and temp in wordList:
                        counter += 1
                        seen.add(temp)
                        queue.append(temp)


        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(Solution().ladderLength(beginWord, endWord, wordList))

beginWord = "a"
endWord = "c"
wordList = ["a","b","c"]
print(Solution().ladderLength(beginWord, endWord, wordList))