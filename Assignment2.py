 ##Q1. 1.What are the Boolean data type's two values? How do you go about writing them?
A.  The Boolean data type is either True or False. In Python Boolean data or Boolean variables are defined by True or False as keywords.

Example:
       
# In[9]:


a = 10
if a==10:
    print(True)
    print(type(True))
else:
    print(False)
    print(type(False))

a.Above <class ‘bool’> indicates that the variable  is of Boolean data type.
b.Always the bool variables should start first letter with Upper case i. True or False 
c.If we try to give bool variable as true or false then the following error it generates as:

# In[10]:


a = 10
if a==10:
    print(true)
    print(type(true))
else:
    print(false)
    print(type(false))

•	In python integers and floating point numbers can be converted into Boolean data type using function called bool() 
•	When an integer or float  set to zero then we get False as return. Similarly when int or float set to 1 then it return True

# In[11]:


a = int(input("enter s value"))
if a == 1:
    print(bool(a))
elif a == 0:
    print(bool(a))
else:
    print("No input")


# In[12]:


a = int(input("enter s value"))
if a == 1:
    print(bool(a))
elif a == 0:
    print(bool(a))
else:
    print("No input")

.We can use Boolean variables in Arithmetic problems such as
# In[7]:


a = True
b = False
i = int(input("enter i value"))
if i == 1:
    print(a or b)
elif i == 2:
    print(a and b)
elif i == 3:
    print(a!=b)
else:
    print(a or (b and c))
    


# In[8]:


a = True
b = False
i = int(input("enter i value"))
if i == 1:
    print(a or b)
elif i == 2:
    print(a and b)
elif i == 3:
    print(a!=b)
else:
    print(a or (b and c))


# # 2.What are the three different types of Boolean operators?
A.The different Boolean operators in python are:
1.AND Operator (&& or and)
2.NOT Operator (not)
3.OR Operator(|| or “or”)1.AND Operator(&& or and):
Here AND Boolean operator is similar to bitwise AND operator which will analyzes the operands on both side. It is denoted by “and”

                                   True and True = True
                                   True and False = False
                                   False and False = False
                                   False and True = False 

# In[13]:


a = 9
b = 20
if a>=10 and b<=20:
    print(True)
else:
    print(False)


# In[14]:


a = 10
b = 20
if a>=10 and b<=20:
    print(True)
else:
    print(False)

2.NOT Operator(not)
Here NOT Boolean operator will does the reverse operation to the final result that immediately follows. It is denoted by “not”

                                    not (True) = False
                                    not(False) = True

# In[16]:


a = input("enter string")
if a == "python":
    print(not(True))
else:
    print(not(False))


# In[17]:


a = input("enter string")
if a == "python":
    print(not(True))
else:
    print(not(False))

3.	OR Operator(|| or “or”)
Here OR Operator is similar to bitwise OR where in bitwise we will look “1” as true and “0” as false. Similarly in OR we look for True or False as final result.
                                     
                                    True or False = True
                                    False or True = True
                                    False or False = False
                                    True or False = True


# In[18]:


a = 10
b = 30
if a == 10 or b == 40:
    print(True)
else:
    print(True)


# In[21]:


a = 20
b = 30
if a == 10 or b == 40:
    print(True)
else:
    print(False)


# # Q3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean  
#      values for the operator and what it evaluate ).
# 
A. The following are the Boolean operator:
                  1. AND Operator (&& or and)
                  2. NOT Operator (not)
                     OR Operator(|| or “or”)
1.	Truth Table for AND Operator
              True           False             True and False    False
              False          True              False and True    False
              False          False             False  and False   False
              True           True              True and True      True           

               (True and False) and True          False
               (False and False) and False        False
               (True and True) and False          False
               (True and True) and True           True
               (False and False) and True          False

2.	Truth Table for NOT Operator
            True              not(True)            False
            False             not(False)           True

3.	Truth Table for OR Operator
  True       True        True or True       True
  False       True        False or True       True
  False       False       False or False      False
  True        False       True or False       True

                
               (True or False) or True             True
               (False  or False) or False          False
               (True or True) or  False            True
               (True or  True) or True             True
               (False or False) or True            True

Combination of both OR, NOT AND:
       (True or False) and (not(True))                                                False
        (False and True) or(not(False))                                               True
     Not( (True and True) or (False))                                                 False
      (Not(False) and True) and (False or not(True)                        False


# Q4. What are the values of the following expressions?
A..                    (5 > 4) and ( 3 == 5) ------ False
                     Not(5>4)  ------                   False
                      (5 > 4) or (3 == 5)  -------- True
                     Not((5>4) or (3==5)) -------- False
                     (True and True) and (True == False) ---- False
                    (not(False)) or (not(True)) ------- True

# # Q5. What are the six different types of reference operators?
The six reference operators are  
                       a. Arithmetic Operator
                       b. Assignment Operator
                       c. Comparison Operator
                       d. Logical Operator
                       e. Identity Operator
a. Arithmetic Operator
     Arithmetic Operators are used in numeric values to perform operations
           +  -> Addition, -   -> Subtraction, *  -> Multiplication, / -> division,  % -> Modulus, // -> floor

# In[22]:


a = 21
b = 10
c = 0
c = a+b
print(c)
c = a-b
print(c)
c = a*b
print(c)
c = a/b
print(c)
c = a%b
print(c)
c = a**b
print(c)
c = a//b
print(c)

b. Assignment Operator:
     Assignment Opeartor are used to assign values to variables
        =, + =,  - =, * =, / =, %=, //= ,**=, ^=, >> =, << =  are some assignment operators

# In[23]:


a = 2
b = 5
c = 0
c = a+b
print(c)
c += a
print(c)
c *= a
print(c)
c /= a
print(c)
c %= a
print(c)
c **= a
print(c)
c //=a 
print(c)

c. Comparison Operator:
         Comparison operator used to compare two values.
             ==, !=, >, <, >=, <=    are comparison operators

# In[27]:


a = 21
b = 10
c = 0

if ( a == b ):
    print("Line 1 - a is equal to b")
else:
    print("Line 1 - a is not equal to b")

if ( a != b ):
    print("Line 2 - a is not equal to b")
else:
    print("Line 2 - a is equal to b")

if ( a < b ):
    print("Line 4 - a is less than b") 
else:
    print("Line 4 - a is not less than b")

if ( a > b ):
    print("Line 5 - a is greater than b")
else:
    print("Line 5 - a is not greater than b")

a = 5;
b = 20;
if ( a <= b ):
    print("Line 6 - a is either less than or equal to  b")
else:
    print("Line 6 - a is neither less than nor equal to  b")

if ( b >= a ):
    print("Line 7 - b is either greater than  or equal to b")
else:
    print("Line 7 - b is neither greater than  nor equal to b")

d.Logical Operator:
   logical operators are used in conditional statements
     AND, OR, NOT are three logical operators

# In[28]:


x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

e.Identity Operator:
   identity operator are used to compare objects.
      Is , is not are two identity operators.

# In[29]:


x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

f. BitWise Operators:
    Bitwise operators are used to compare binary numbers
      &, |, ^, ~, <<, >> are operators of bitwise

# In[31]:


a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print("Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101 
print("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print("Line 6 - Value of c is ", c)


# # Q6. How do you tell the difference between the equal to and assignment operators?
A.The assignment operator (“=”) is used to assign the value of right to left
# In[32]:


a = 10
print(a)

      The “==” operator will checks whether two operands are equal or not. Means it gives true or false
# In[33]:


a = 10
if a == 10:
    print(True)
else:
    print(False)


# In[34]:


a = 11
if a == 10:
    print(True)
else:
    print(False)


# # Q7. Describe a condition and when you would use one.
A. Condition is statement which helps programmer to evaluate whether following logic or condition is true or false. In python conditional keywords like if, elif and else.
# In[35]:


if "fool" in ["fool","bool","cool"]:
    print(True)

Above is the example for if condition , here we are checking whether the following string fool is exist in the list of elements or not. It returns true when it exists.
# In[36]:


if "fool" in ["fool","bool","cool"]:
    print(True)
elif "cool" in ["fool","cool","bool"]:
    print("True")
else:
    print(False)

Elif and else are two more conditions that are used by programmers to evaluate .
# # 8. Recognize the following three blocks in this code
.                      spam = 0
                        if spam == 10:
                                 print('eggs')     ---------------------     Block 1
                        if spam > 5:
                                   print('bacon')            --------------  Block 2
                          else:
                                  print('ham')                 ----------------- Block 3
                               print('spam')          
                     print('spam')
# Q9. Create a programme that prints. If 1 is stored in spam, prints Hello; if 2 is stored in spam, prints Howdy; and if 3 is stored in spam, prints Salutations! if there's something else in spam.
# In[37]:


spam = [1,2,3]
for i in range(len(spam)):
    if spam[i] == 1:
        print("hello")
    if spam[i] == 2:
        print("Howdy")
    if spam[i] == 3:
        print("Salutations")
else:
    print("Something else")


# # Q10.If your programme is stuck in an endless loop, what keys can you press?
A. CTRL + C
# # Q11.How can you tell the difference between break and continue?
A. Break  statement should be used inside a loop, when it is used it will terminate the loop based on condition . suppose if it is used inside nested loop then it will terminate from the current loop .
# In[40]:


i = 10
for i in range(0,10):
    if i == 10:
        break
    else:
        print(i)

     Continue statement will terminates or stops to execute current condition and control  will go back to   next iteration value or first step depends on logic 
# In[41]:


i = 10
for i in range(0,10):
    if i != 0:
        continue
    else:
        print(i)


# # Q12.In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
range(10) = it will gives sequence of numbers from 0 to 9

# In[42]:


for i in range(10):
    print(i)

  Range(0, 10) = it will generates the numbers from starting index i.e 0 and till end – 1 i.e 9
# In[43]:


for i in range(0,10):
    print(i)

Range(0,10,1) = it will generates the sequence of numbers from 0 to 9 where start index, end index and step index are arguments . step indicates the increment
# In[44]:


for i in range(0,10,1):
    print(i)


# # Q13.Using a for loop, write a short programme that prints the numbers 1 to 10 Then, using a while loop, create an identical programme that prints the numbers 1 to 10.

# In[45]:


for i in range(1,11):
    print(i)


# In[46]:


i = 1
while i!=0:
    print(i)
    if i == 10:
        break
    else:
        i = i + 1


# # Q14.If you had a bacon() function within a spam module, how  would you call it after importing spam?
spam.bacon()
# In[ ]:




