#!/usr/bin/env python
# coding: utf-8

# # Is the Python Standard Library included with PyInputPlus?
A. No Python Standard Library is not included with PyInputPlus. So, we have to install it separately using pip.To install
PyInputPlus, run pip install --user pyinputplus from command line
# # 2.Why is PyInputPlus commonly imported with import pyinputplus as pypi?
A.pyinputplus will keep asking the user for text until they enter valid input. So, its recommended to import pyinputplus as pypi
import pyinputplus as pypi

All of PyInputPlus’s functions begin with the input, such as inputStr() or inputDate()

For example, you can ask the user for an integer with inputInt(), and the return value will be an integer instead
of the string that input() would normally return:
# In[2]:


input()


# # 3. How do you distinguish between inputInt() and inputFloat()?
inputint() - in python input() will reads an string and returns always string
int(input()) will gives the integer value.

inputFloat - which will reads the floating point numbers say, curreny denominations are generally read in float data type
float(input())
# # 4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
import pyinputplus as pypi
for i in range(0,99):
    pypi.inputInt()
# # 5.What is transferred to the keyword arguments allowRegexes and blockRegexes?
A. 
     prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                              blockRegexes=[('.*', 'Incorrect!')])
# # 6. If a blank input is entered three times, what does inputStr(limit=3) do?
A.If the user answers incorrectly more than 3 times, it raises a RetryLimitException exception. Both of these exception types are in the PyInputPlus module, so pyip. needs to prepend them like 


 except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')


# # 7.If blank input is entered three times, what does inputStr(limit=3, default=&#39;hello&#39;) do?
A.inputStr(limit=3, default='hello') will ensure that user has 3 attempts for the correct answer with default data 
# In[ ]:




