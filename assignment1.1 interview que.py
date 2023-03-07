# Q 1. What are lists and tuples? What is the key difference between the two?
# ans:-  Lists and Tuples are both sequence data types that can store a collection of objects in Python. The objects stored in both sequences can have different data types. Lists are represented with square brackets ['sara', 6, 0.19], while tuples are represented with parantheses ('ansh', 5, 0.97).
#The key difference between the two is that while lists are mutable, tuples on the other hand are immutable objects.

# Q2.  What is _init_?
# ans:- _init_ is a contructor method in Python and is automatically called to allocate memory when a new object/instance is created. All classes have a _init_ method associated with them. It helps in distinguishing methods and attributes of a class from local variables.

# Q3. What is lambda in Python? Why is it used?
# ans:-Lambda is an anonymous function in Python, that can accept any number of arguments, but can only have a single expression. It is generally used in situations requiring an anonymous function for a short time period.

#Q4. What are functions in Python?
# ANS:-A function is a block of code which is executed only when a call is made to the function. def keyword is used to define a particular function as shown below:

#def function():
#print("Hi, Welcome to Intellipaat")
#function(); # call to the function

#Q5.What are the common built-in data types in Python?
#ANS :- Python supports the below-mentioned built-in data types:

#Immutable data types:

#Number
#String
#Tuple
#Mutable data types:

#List
#Dictionary
#set

#Q.6 What does [::-1] do?
# ANS:- [::-1] ,this is an example of slice notation and helps to reverse the sequence with the help of indexing.

#Q7 How to comment with multiple lines in Python?
#ANS:-To add a multiple lines comment in python, all the line should be prefixed by #.


#Q8. Explain split(), sub(), subn() methods of “re” module in Python?
#ANS :- These methods belong to the Python RegEx or ‘re’ module and are used to modify strings.

#split(): This method is used to split a given string into a list.
#sub(): This method is used to find a substring where a regex pattern matches, and then it replaces the matched substring with a different string.
#subn(): This method is similar to the sub() method, but it returns the new string, along with the number of replacements.

#Q9.What is a map function in Python?
# ANS:- The map() function in Python has two parameters, function and iterable. The map() function takes a function as an argument and then applies that function to all the elements of an iterable, passed to it as another argument. It returns an object list of results.

#Q10.Name four of the main data types in Python?
# ANS:-Numbers, strings, lists, dictionaries, tuples, files, and sets are generally considered the main types of data.

#Q11.What does mapping mean and what kind of data type is based on mapping?
# ANS:-The term mapping refers to an object that maps keys to associated values. The Python dictionary is the only type of mapping in the base typeset. Mappings do not maintain any left-to-right position order; they support access to stored data by key, as well as type-specific method calls

#Q12.How would you convert JSON to Python objects?
# ANS:-The json library in Python can help you convert JSON data into Python objects. The process is known as decoding. You can use the json.loads() function to decode JSON data. This function takes a JSON string and returns a Python object.

#Q13.What are the two types of functions in Python?
# ANS:-There are two types of functions in Python: built-in functions and user-defined functions. Built-in functions are functions that are already defined in the Python language, such as the print() function. User-defined functions are functions that are created by the user, and they can be created to do anything that the user wants them to do.

#Q14.Do Python functions have return values? If yes, then how many can they have?
#ANS:- Yes, Python functions can have return values. They can have a single return value, or they can have multiple return values.

#Q15.What does the method object() do?
# ANS:-The method returns a featureless object that is base for all classes. This method does not take any parameters.
# Q16.Define self in Python.
#ANS:-Self is an instance of a class or an object in Python. It is included as the first parameter. It helps differentiate between the methods and attributes of a class with local variables

#Q17.What is the Pass statement?
# ANS:-A Pass statement in Python is used when we cannot decide what to do in our code, but we must type something to make it syntactically correct.

#Q18.Can we reverse a list in Python?
#ANS:-Yes, we can reserve a list in Python using the reverse() method. The code is as follows:

#def reverse(s):
# str = "" 
 #for i in s: 
  # str = i + str
  #return str
#Q19.Why do we need a break?
# ANS:-Break helps control the Python loop by breaking the current loop from execution and transferring the control to the next block
#Q20. What’s the advantage of using generators over lists in Python?
# ANS:-Generators are much more memory efficient than lists because they only store the values that are needed at the current moment, rather than storing all of the values upfront. This makes them ideal for situations where you need to process a large amount of data, because you won’t need to worry about your program running out of memory.