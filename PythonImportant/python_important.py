'''
String, tuple are imutables so for doing any operations on them just change 
them to list then change them back to proper format
set.add()
set.pop()
list.append()
list.pop(index)
list.remove(val)
del list[index]
list[start:end:iteration]
from collections import deque 
dedqueu.append()
dequeue.appendleft()
dequeue.pop()
dequeue.popleft()
dequeue.insert(4,3)
print (dequeue.count(3))
# using insert() to insert the value 3 at 5th position
'''

# dict(sorted(x.items(), key=lambda item: item[1]))
# sorted_nee = {item[0]: item[1] for item in sorted(nee.items(),key=lambda item:item[1])}
# sorted_nee = dict(sorted(nee.items(),key=lambda item:item[1],reverse=True))
# sort by value if you want by key just replace item[1] to item[0]
# txt = "welcome to the jungle"

# x = txt.split()
# print(x)
# txt = "apple#banana#cherry#orange"

# x = txt.split("#")
# x = ["apple","banana","cherry","orange"]
# x = '#'.join(x)
# print(x)
# x = lambda param : param+1
# print(x(2))
# prints 3
# mydict = {'george': 16, 'amber': 19}
# print(list(mydict.keys())[list(mydict.values()).index(19)])
# Get an key by value from this list
# x = [1,2,3,5,4,5,6]
# y = x.index(5)
# print(y)
# y will be 4 index gives us the first index value of that element
# del dict[key]
# dict.pop(key)
# #two ways to delete element from the dictionary but is also deletes the reference

# str1 = "mystring"
# list1 = list(str1)
# # string to list
# list1[5] = 'u'
# # how to change something in a string change it to list than do what you want to do than change back to str.
# # list join to str
# str1 = ''.join(list1)

# For making it a max heap just multiply every element you put by -1 and when you pop
# multiply again by -1
# heap library
# import heapq
# li = [1,9,3,4,5]
# heapq.heapify(li)
# # print(list(li))
# print(heapq.heappop(li))
# print(heapq.heappop(li))
'''
		heappushpop(heap, ele) => combines the functioning of both push and pop
		heapreplace(heap, ele) = > element is first popped, then the element is pushed.i.e, 
		the value larger than the pushed value can be returned
		nlargest(k, iterable, key = fun) :- This function is used to return the k largest elements
		 from the iterable specified and satisfying the key if mentioned.
		 nsmallest(k, iterable, key = fun) :- This function is used to return the k smallest
		  elements from the iterable specified and satisfying the key if mentioned.
'''