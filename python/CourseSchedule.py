# https://leetcode.com/problems/course-schedule/
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dependencyToCourse = {}
        for edge in prerequisites:
            if dependencyToCourse.get(edge[1]) is None:
                dependencyToCourse[edge[1]] = [edge[0]]
            else:
                dependencyToCourse[edge[1]].append(edge[0])

        visited = [False] * numCourses
        visitedInCurrentRec = [False] * numCourses

        def isCyclicDependencyPresent(course):
            visited[course] = True
            visitedInCurrentRec[course] = True
            coursesCanBeTaken = dependencyToCourse.get(course)
            if coursesCanBeTaken:
                for course1 in coursesCanBeTaken:
                    if not visited[course1]:
                        if isCyclicDependencyPresent(course1):
                            return True
                    elif visitedInCurrentRec[course1]:
                        return True

            visitedInCurrentRec[course] = False
            return False

        for course in range(numCourses):
            if not visited[course]:
                if isCyclicDependencyPresent(course):
                    return False

        return True



# print(Solution().canFinish(2, [[1,0]]))
print(Solution().canFinish(10, [[2,3], [4,5], [5,3], [1,2], [7,8], [5,0], [0,8], [3,7], [5,9],[2,9]]))



"""
207. Course Schedule
Medium

3162

160

Add to List

Share
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5


Inputs - 
numCourses,prerequisites

 for i upto numCouses
    j on which i depemndent 
    
    check dependency on j on and on 
    just tak case node which 

"""
