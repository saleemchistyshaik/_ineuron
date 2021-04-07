#!/usr/bin/env python
# coding: utf-8

1. What does an empty dictionary's code look like?

 A To create an empty dictionary, the dictionary set should be set to {}

the code shown as

# In[1]:
items = {}

Above code explains that, we create an empty dictionary by name called as items. Another way to create empty dictionary is
to set dictionary equals to dict()

2. What is the value of a dictionary value with the key 'foo' and the value 42?

 A.{'foo':42}

3. What is the most significant distinction between a dictionary and a list?

A.The items stored in dictionary are unordered and items stored in list are ordered

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

A. KeyError: 'foo'

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

A.There wont be no difference. The in operator checks whether a value exists as a key in the dictionary

6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

A.'cat' in spam checks whether there is 'cat' key in the dictionary , while 'cat' in spam.values() checks whether there is 
 a value 'cat' for one of the keys in the spam

7. What is a shortcut for the following code?if 'color' not in spam:spam['color'] = 'black'
A. spam.setdefault('color', 'black')

8. How do you "pretty print" dictionary values using which module and function?

A. pprint.pprint()






