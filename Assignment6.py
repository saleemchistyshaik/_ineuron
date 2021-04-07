1. What are escape characters, and how do you use them?
A.An escape character is a backslash \ followed by the character you want to insert.

Example:
    text = "hello world "i"" -----> throws error
    text = "hello world \"i\" "
    

The following are escape characters
\'
\\
\n
\r
\t
\b
\f

2. What do the escape characters n and t stand for?
A.the escape character n stands for new line and denoted as '\n'. Similarly escape character t stands for tab and denoted as '\t'

3. What is the way to include backslash characters in a string?
A.To include backslash characters in a string we have to use two backslashes(\\) or @

var s = "\\hello";
var s = @"\hello";

4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?
A. The double quotes are required to end the quote, single quotes are not recognized

5. How do you write a string of newlines if you don't want to use the n character?
Multiline strings allow you to use newlines in strings without the \n escape character.


text = "hello world\n" this is way of writing string using new line

print("hello", end = " ") this is way of writing string without using new line instead we can use end keyword with space or else 
we can use print statement taht gives everything in a single line
6. What are the values of the given expressions?
 'Hello, world!'[1]
 'Hello, world!'[0:5]
 'Hello, world!'[:5]
 'Hello, world!'[3:]
 
# In[9]:


'Hello, world!'[1]


# In[10]:


'Hello, world!'[0:5]


# In[11]:


'Hello, world!'[:5]


# In[12]:


'Hello, world!'[3:]


7. What are the values of the following expressions?
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
 

# In[13]:


'Hello'.upper()


# In[14]:


'Hello'.upper().isupper()


# In[15]:


'Hello'.upper().lower()


8. What are the values of the following expressions?'Remember, remember, the fifth of July.'.split()'-'.join('There can only one.'.split())
 
A. The expressions evaluate to the following:

['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

'There-can-be-only-one.

9. What are the methods for right-justifying, left-justifying, and centering a string?
A.The rjust(), ljust(), and center() string methods, respectively

10. What is the best way to remove whitespace characters from the start or end?
A.The lstrip() and rstrip() methods remove whitespace from the start and  end of a string.




