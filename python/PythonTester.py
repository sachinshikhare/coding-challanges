
string = "123456789"
if len(string) % 3 == 1:
    arr = [string[0]]
    arr.extend([string[i:i+3] for i in range(1, len(string), 3)])
elif len(string) % 3 == 2:
    arr = [string[0:2]]
    arr.extend([string[i:i+3] for i in range(2, len(string), 3)])
else:
    arr = [string[i:i+3] for i in range(0, len(string), 3)]

print(arr)

# arr1 = [1,0,0,0]
# arr2 = [[0,1],[0,0]]
# # print(any(arr1))
# # output = any([any(val == 1 for val in arr2)])
# output = any(any(i == 1 for i in arr) for arr in arr2)
# print(output)


# import heapq
#
# max_heap = []
# heapq.heappush(max_heap, -3)
# heapq.heappush(max_heap, -8)
# heapq.heappush(max_heap, -1)
# heapq.heappush(max_heap, -6)
# heapq.heappush(max_heap, -2)
# heapq.heappush(max_heap, -7)
#
# for item in max_heap:
#     print(item)
# max_heap.remove(-6)
# print()
# for item in max_heap:
#     print(item)

#
#
# while pq.not_empty:
#     print(pq.queue)
#     print(pq.get())


# print("Hello World!")
#
# dict = {'a':3}
# val = dict.get('4')
# if val:
#     dict['a'] = val + 1
# print((dict['a']))
# a = set()
# a.add(1)
# a.add(2)
# a.add(3)
#
# b = set()
# b.add(1)
# b.add(4)
# b.add(5)
#
# print(a.union(b))


# print(10 / 2, 10//2, 11/2, 11//2)