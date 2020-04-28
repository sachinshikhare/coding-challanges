# https://leetcode.com/problems/the-skyline-problem/
from typing import List
from queue import PriorityQueue

import heapq


class Solution:
    # Partially copied
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        points = []
        for building in buildings:
            points.append([building[0], building[2], 'start'])
            points.append([building[1], -building[2], 'end'])

        points.sort(key=lambda x:( x[0], -x[1]))
        maxHeap = [0]
        result = []
        for point in points:
            if point[2] == 'start':
                if point[1]>-maxHeap[0]:
                    result.append([point[0],point[1]])
                heapq.heappush(maxHeap, -point[1])
            elif point[2] == 'end':
                maxHeap.remove(point[1])
                heapq.heapify(maxHeap)
                if -point[1]>-maxHeap[0]:
                    result.append([point[0],-maxHeap[0]])
        return result


buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]


print(Solution().getSkyline(buildings))



