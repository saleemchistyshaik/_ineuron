Solution to Question 2:
-----------------------
String is the type of information which store using variable in enclosed punctuate. String is datatype for a sequence of characters, in addition to letters, they can also include numbers, spaces and punctuations.
Variables are references that you create to refer some value in programe.

Example: my_value = "Hello World". In this my_value referes as variable and "Hello World" is string

Solution to question 3:
-----------------------
Three different data forms in python are
a.Numeric
b.Boolean
c.Set

a.Numeric data type repreents numeric data values. It can be float, integer or complex number.
INTEGER: The integer value represented by int class. It can be whole numbers, in python there is no limit to how long integer value can be.
FLOAT:  The float value represented by float class. It is real numbers with floating poiunt representation, it has decimal point also
COMPLEX NUMBERS: Complex values are repreented by complex class. It is represented as (realpart) + (imaginary part)
a = 5
print("Type of a" + type(a))  ---------> Type of a <class 'int'>
a = 2.5
print("Type of a" + type(a))  ---------> Type of a <class 'float'>
a = 2 + 3j
print("Type of a" + type(a))  ---------> Type of <class 'complex'>

b.Boolean data type represents two type of values i.e TRUE or FALSE. Boolean object when they are equal then it is TRUE or else FALSE.
in python we should Use T and F for boolean i.e True and False otherwise throws error
a = 10
if a == 10:
   print(type(True))  -----> <class 'bool'>
 else
   print(type(False)) -----> <class 'bool'>
   
c. Set is unordered collection of data type that is iterable , mutable and has no duplicate elements.
Two operations of sets i.e creating set and accessing set
1. creating set: set can be created using built in set() which is iterable. we can create set using list also
set1 = set("hello")  
print("\nSet with the use of String: ")          output: Set with the use of String: 
                                                        {'e', 'h', 'l', 'o'}
print(set1)

set1 = set(["Apple", "For", "Apple"])  
print("\nSet with the use of List: ")            output : Set with the use of List: 
                                                          {'For', 'Apple'}
print(set1)
