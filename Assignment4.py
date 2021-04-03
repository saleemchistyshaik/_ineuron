 # 1.What exactly is []?
A.It is called to be as empty list or list value, which is a list value that contains no items.
# # 2.In a list of values stored in a variable called spam, how would you assign the value 'hello' as   the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
A.  spam[2] = ‘hello’
Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

# # 3.What is the value of spam[int(int('3' * 2) / 11)]?
A.‘d’ (‘3’ * 2 is the string ‘33’, which is passed to int() before being divided by 11 . This evaluates to   3. Expressions can be used wherever values used)
# # 4.What is the value of spam[-1]?
A.'d'
# # 5.What is the value of spam[:2]?
A.[‘a’,’b’]
# # Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
# 6. What is the value of bacon.index('cat')?
A. 1
# # 7.How does bacon.append(99) change the look of the list value in bacon?
A.[3.14, 'cat,' 11, 'cat,' True,99]
# # 8.How does bacon.remove('cat') change the look of the list in bacon?
A.. [3.14, 11, 'cat,' True,99]
# # 9.What are the list concatenation and list replication operators?
A. The operator used for list concatenation is ‘+’  and replication is ‘*’
# # 10.What is difference between the list methods append() and insert()?
A. append() will adds the values to the end of list while insert() will adds anywhere in list.
# # 11.What are the two methods for removing items from a list?
A. del statement and remove() are two methods used to remove from list
# # 12. Describe how list values and string values are identical.
A. Both list and string can be passed through len() , have indexes and slices used in for loops and can be concatenated or replicated , and be used with in and not in operators.
# # 13.What's the difference between tuples and lists?
A.Lists are mutable , they can have values added , removed or changed . Tuples are immutable they cannot be changed at all. Tuples used in ()  while list used in []
# # 14.How do you type a tuple value that only contains the integer 42?
A.(42,) [comma is mandatory]

# # 15.How do you get a list value's tuple form? How do you get a tuple v’lue's list form?
A.using typecasting i.e list() and tuple()
# # 16.Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
A.They contain reference to list values
# # 17.How do you distinguish between copy.copy() and copy.deepcopy()?
A.copy.copy() will allow shallow copy of list , while copy.deepcopy() will do deep copy of list . copy.deepcopy can be do duplicate values in the list
# In[ ]:




