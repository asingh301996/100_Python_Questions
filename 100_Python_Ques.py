'''1.FUNCTION 
- block of code outside of class'''
def add(a,b):
    return a+b
print(add(2,3))


'''2. METHOD
- it's a functio associated with an object.
method is defined inside the classes and called using dott notation'''
name="anks"
print (name.upper()) #upper is a method

''' ARGUMENTS VS PARAMETERS'''
def greet(name): #name is parameter
    return "Hello " + name
result = (greet("Anks")) #Anks is argument
print(result)


'''3. TYPES OF ARGUMENTS'''
#1. Positional arguments
def subtract(a,b=1):
    return a-b
print(subtract(5,2)) #5 and 2 are positional arguments  

#2. Keyword arguments
def multiply(a,b):
    return a*b
print(multiply(b=4,a=3)) #keyword arguments

#3. Default arguments
def divide(a,b=2):
    return a/b
print(divide(8)) #b takes default value 2
print(divide(8,4)) #b takes value 4

#4. Variable-length arguments
def add_all(*args):
    return sum(args)
print(add_all(1,2,3,4,5), "-------------args") #args is a tuple  

def multiply_all(**kwargs):
    result = 1
    for value in kwargs.values(): #{1st value=2, 2nd value=3, 3rd value=4}
        result *= value
    return result
print(multiply_all(a=2,b=3,c=4)) # this will create a dict -> {'a':2,'b':3,'c':4 }--> kwargs is a dictionary 

#5. Positional-only arguments (Python 3.8+)
def pos_only(a, b, /):
    return a + b
print(pos_only(2, 3))  # Valid
# print(pos_only(a=2, b=3))  # Invalid, will raise TypeError

#6. Keyword-only arguments (Python 3+)
def kw_only(*, a, b):
    return a + b
# print(kw_only(2, 3))  # Invalid, will raise TypeError
print(kw_only(a=2, b=3))  # Valid 

#7. Combination of all types
def complex_func(a, b=2, *args, c, d=4, **kwargs):
    print(f"a: {a}, b: {b}, args: {args}, c: {c}, d: {d}, kwargs: {kwargs}")
complex_func(1, 3, 5, 7, c=6, e=8, f=9) 
'''a=1, b=3, args=(5,7), c=6, d=4, kwargs={'e':8,'f':9}
# Note: Positional-only arguments must come before regular positional arguments,
# and keyword-only arguments must come after *args.
# Also, default values can be provided for both positional and keyword-only arguments.
# Mixing these types allows for flexible function definitions that can handle a variety of input scenarios.'''

#8. Annotated arguments (Python 3+)
def annotated_func(a: int, b: str = "default") -> str:
    return f"{a} - {b}"
print(annotated_func(5))  # Output: "5 - default"
print(annotated_func(10, "custom"))  # Output: "10 - custom"
'''# Annotations provide a way to attach metadata to function arguments and return values.
# They can be used for type hints, documentation, or other purposes.
# However, they do not enforce any type checking at runtime.    '''

#9. Lambda functions (Anonymous functions)
add_lambda = lambda x, y: x + y
print(add_lambda(3, 4))  # Output: 7
'''Lambda functions are small anonymous functions defined using the lambda keyword.
# They can take any number of arguments but can only have a single expression.
# They are often used for short, throwaway functions, especially in higher-order functions like map, filter, and reduce.'''

#10. Recursive functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120
''' Recursive functions are functions that call themselves in order to solve a problem.
# They typically have a base case to terminate the recursion and a recursive case to continue the process.
# They are often used for problems that can be broken down into smaller, similar subproblems.'''

#11. Higher-order functions
def apply_func(func, value):
    return func(value)  
print(apply_func(lambda x: x * 2, 5))  # Output: 10
'''Higher-order functions are functions that can take other functions as arguments or return functions as their result.
# They are commonly used in functional programming and can help create more abstract and reusable code.
# Examples of higher-order functions in Python include map, filter, and reduce.'''

#12. Generator functions
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for number in count_up_to(5):
    print(number)  # Output: 1, 2, 3, 4, 5
'''# Generator functions use the yield keyword to produce a series of values over time, instead of returning a single value.
# They are useful for working with large datasets or streams of data, as they generate values on-the-fly and can be more memory efficient than returning a list.'''

#13.    Nested functions        
def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x) + 3
print(outer_function(5))  # Output: 13
'''# Nested functions are functions defined within other functions.
# They can be used to encapsulate functionality and create closures, where the inner function has access to the variables of the outer function.
# They are often used for organizing code and creating helper functions that are not needed outside the outer function.'''

#14.    Partial functions (using functools.partial)
from functools import partial
def power(base, exponent):
    return base ** exponent
square = partial(power, exponent=2)
print(square(5))  # Output: 25
'''# Partial functions allow you to fix a certain number of arguments of a function and generate a new function.
# They are useful for creating specialized versions of functions with some arguments pre-filled.
# The functools.partial function is used to create partial functions in Python.    '''                     

#15.    Asynchronous functions (using async/await)
import asyncio
async def async_function():
    print("Start")
    await asyncio.sleep(1)
    print("End")
asyncio.run(async_function())
'''# Asynchronous functions are defined using the async keyword and can use the await keyword to pause execution until an awaited task is complete.
# They are used for concurrent programming, allowing you to write code          
# that can perform other tasks while waiting for I/O operations or other long-running tasks to finish. without blocking the main thread.
# The asyncio library provides tools for working with asynchronous code in Python.    '''  

'''16. DELETE & REMOVE() '''
# delete() --> used with index
# remove() --> used with value
my_list = [10, 20, 30, 40, 50]

# Using del to remove an element by index
del my_list[2]  # Removes the element at index 2 (30)
print("After del:", my_list)  # Output: [10, 20, 40, 50]

# Using remove() to remove an element by value
my_list.remove(40)  # Removes the first occurrence of the value 40
print("After remove():", my_list)  # Output: [10, 20, 50]

# Note: If the value to be removed is not found, remove() will raise a ValueError.
# del can also be used to delete variables or slices of a list. 
# For example:
a = 10
del a  # Deletes the variable 'a'
# print(a)  # This will raise a NameError since 'a' is deleted

my_list = [10, 20, 30, 40, 50]
del my_list[1:3]  # Removes elements from index 1 to 2
print("After del slice:", my_list)  # Output: [10, 40, 50]
# In summary, use del when you know the index of the element you want to remove,
# and use remove() when you know the value of the element you want to remove.   

'''17. Diff B/W FOR & WHILE LOOP'''
# For Loop
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
''' FOR looop works well with lists, strings and ranges'''


# While Loop   
''' While Loop is when unknown about the number of iterations'''
count = 0
while count < 5:
    print(count)  # Output: 0, 1, 2, 3, 4
    count += 1


'''18. CONDITIONAL STATEMENT IN PYTHON'''
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative") 


'''19. BREAK, CONTINUE, PASS'''
# Break - stops loop entirely & Exits the loop
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)  # Output: 0, 1, 2, 3, 4

# Continue - skips current iteration & continues with next iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Output: 1, 3, 5, 7, 9

# Pass - does nothing, used as a placeholder
for i in range(5):
    if i == 3:
        pass  # Placeholder, does nothing
    print(i)  # Output: 0, 1, 2, 3, 4


'''20.  Python LISTS usage'''
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying elements
my_list[1] = 20
print(my_list)  # Output: [1, 20, 3, 4, 5]

# Adding elements
my_list.append(6)
print(my_list)   # Output  : [1, 20, 3, 4 , 5, 6]

# Removing elements
my_list.remove(3)
print(my_list)  # Output: [1, 20, 4, 5, 6]  

# Slicing
print(my_list[1:4])  # Output: [20, 4, 5]
# Iterating
for item in my_list:
    print(item) # Output: 1, 20, 4, 5, 6

# List comprehension - 
'''my_list is an existing list, e.g. [1, 20, 4, 5, 6].
x**2 means "take each item x from my_list and square it".
for x in my_list means "do this for every item in my_list".
The whole thing [x**2 for x in my_list] creates a new list of squared values.'''
squared = [x**2 for x in my_list]
print(squared)  # Output: [1, 400, 16, 25, 36]  

# Length of list
print(len(my_list))  # Output: 5

# Check if element exists    
print(20 in my_list)  # Output: True

# Clear the list
my_list.clear()
print(my_list)  # Output: []  # Output: []  

# Nested lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[1][0])  # Output: 3   # Output: 3

# Copying a list
copy_list = my_list.copy()
print(copy_list)  # Output: [] 

# Extending a list
my_list.extend([7, 8, 9])
print(my_list)  # Output: [7, 8, 9]  # Output: [7, 8, 9]

# Reversing a list
my_list.reverse()
print(my_list)  # Output: [9, 8, 7]

# Sorting a list
my_list.sort()      
print(my_list)  # Output: [7, 8, 9]  # Output: [7, 8, 9]

# Finding the index of an element
index = my_list.index(8)
print(index)  # Output: 1  # Output: 1

# Counting occurrences of an element
count = my_list.count(7)
print(count)  # Output: 1  # Output: 1

# Inserting an element at a specific position
my_list.insert(1, 10)
print(my_list)  # Output: [7, 10, 8, 9]  # Output: [7, 10, 8, 9]

# Pop an element from the list
popped_element = my_list.pop()
print(popped_element)  # Output: 9  # Output: 9
print(my_list)  # Output: [7, 10, 8]  # Output: [7, 10, 8]

# Finding the maximum and minimum values
max_value = max(my_list)
min_value = min(my_list)
print(max_value, min_value)  # Output: 10 7  # Output: 10 7

# Summing all elements in the list      
total = sum(my_list)
print(total)  # Output: 25  # Output: 25

# Converting a list to a string
list_as_string = ', '.join(map(str, my_list))
print(list_as_string)  # Output: "7, 10, 8"  # Output: "7, 10, 8"

# Converting a string to a list
string_as_list = list_as_string.split(', ')
print(string_as_list)  # Output: ['7', '10', '8']  # Output: ['7', '10', '8']

# List comprehension with condition
even_numbers = [x for x in my_list if x % 2 == 0]
print(even_numbers)  # Output: [10, 8]  # Output: [10, 8]

# Nested list comprehension
flattened = [num for sublist in nested_list for num in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]  # Output: [1, 2, 3, 4, 5, 6]

# Using enumerate to get index and value
for index, value in enumerate(my_list):
    print(index, value)
# Output: 0 7, 1 10, 2 8

# Using zip to combine two lists
list1 = [1, 2, 3] 
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# List comprehension with function
def square(x):
    return x * x
squared_with_func = [square(x) for x in my_list]
print(squared_with_func)  # Output: [49, 100, 64]  # Output: [49, 100, 64]

# Using filter to filter elements
filtered = list(filter(lambda x: x > 8, my_list))
print(filtered)  # Output: [10]  # Output: [10]

# Using map to apply a function to all elements
mapped = list(map(lambda x: x * 2, my_list))
print(mapped)  # Output: [14, 20, 16]  # Output: [14, 20, 16]

'''List comprehension with multiple conditions '''  

# Find numbers that are even and greater than 7
complex_condition = [x for x in my_list if x % 2 == 0 and x > 7]
print(complex_condition)  # Output: [10, 8]  # Output: [10, 8]

# Using any() and all()
any_greater_than_9 = any(x > 9 for x in my_list)
all_greater_than_5 = all(x > 5 for x in my_list)
print(any_greater_than_9, all_greater_than_5)  # Output: True True  

# Using list comprehension to create a list of tuples
tuples_list = [(x, x**2) for x in my_list]
print(tuples_list)  # Output: [(7, 49), (10, 100), (8, 64)]  # Output: [(7, 49), (10, 100), (8, 64)]

# Using list comprehension to flatten a nested list
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]  # Output: [1, 2, 3, 4, 5, 6]

# Using list comprehension to create a list of characters from a string
string = "hello"
char_list = [char for char in string]
print(char_list)  # Output: ['h', 'e', 'l', 'l', 'o']  # Output: ['h', 'e', 'l', 'l', 'o']

# Using list comprehension to create a list of ASCII values of characters in a string
ascii_values = [ord(char) for char in string]
print(ascii_values)  # Output: [104, 101, 108, 108, 111]  # Output: [104, 101, 108, 108, 111]

# Using list comprehension to create a list of even squares
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]  # Output: [0, 4, 16, 36, 64]

# Using list comprehension to create a list of words with more than 3 letters
words = ["apple", "is", "a", "fruit"]
long_words = [word for word in words if len(word) > 3]
print(long_words)  # Output: ['apple', 'fruit']  # Output: ['apple', 'fruit']

# Using list comprehension to create a list of tuples with index and value 
indexed_list = [(index, value) for index, value in enumerate(my_list)]
print(indexed_list)  # Output: [(0, 7), (1, 10), (2, 8)]  # Output: [(0, 7), (1, 10), (2, 8)]

# Using list comprehension to create a list of unique elements
unique_elements = list(set(my_list))
print(unique_elements)  # Output: [7, 8, 10]

'''21. SETS'''
'''# Sets are unordered collections of unique elements.
# They are defined using curly braces {} or the set() function.
# Sets do not allow duplicate values and do not maintain any specific order.
# Sets are mutable, meaning you can add or remove elements after creation.
# Common operations on sets include union, intersection, difference, and symmetric difference.
# Sets are useful for membership testing, removing duplicates from a list, and performing mathematical set operations'''

my_set= {1,2,3}
print(my_set)  # Output: {1, 2, 3}  

my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}    

my_set.discard(5)  # Does not raise an error if 5 is not found
print(my_set)  # Output: {1, 3, 4}

print(3 in my_set)  # Output: True
print(len(my_set))  # Output: 3

another_set = {3, 4, 5}
print(my_set.union(another_set))  # Output: {1, 3, 4, 5}

print(my_set.intersection(another_set))  # Output: {3, 4}

print(my_set.difference(another_set))  # Output: {1}

print(my_set.symmetric_difference(another_set))  # Output: {1, 5}
my_set.clear()

print(my_set)  # Output: set()

# Set comprehension
squared_set = {x**2 for x in range(5)}
print(squared_set)  # Output: {0, 1, 4, 9, 16}

# Frozenset - immutable version of set
frozen = frozenset([1, 2, 3])
print(frozen)  # Output: frozenset({1, 2, 3})

frozen.add(4)  # This will raise an AttributeError since frozenset is immutable
print(frozen)  # Output: frozenset({1, 2, 3})

'''22. CLASS & OBJECTS '''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
person1=Person("alice", 28)
    
class Cars:
    def __init__(self, model, year):
        self.model=model
        self.year=year

# Now, outside the class, make your car and print
my_car = Cars("Exter", 2021)
print(f"My car is {my_car.year} from year {my_car.year}")

'23. INHERITANCE'

class Robot:
    def fly(self, name):
        print(f"{name} can fly!")

class HumanoidRobot(Robot): #HumanoidRobot is child class & Robot is parent class (HumanoidRobot inherits from Robot)
    def talk(self):
        print(f"I can talk like humans!")

# making humanoid robot 
hero=  HumanoidRobot()
hero.talk() # Output: I can talk like humans!
hero.fly("Robo") # Output: Robo can fly!

'24. POLYMORPHISM'
'''Polymorphism is a big word, but it’s actually simple!
Imagine you have lots of different toys: a robot, a car, and a dog. You want to tell all your toys to "move."

1. The robot walks.
2. The car drives.
3. The dog runs.
'''

class Robot:
    def move(self):
        print("Robot walks")

class Car:
    def move(self):
        print("Car drives")

class Dog:
    def move(self):
        print("Dog runs")

# Now, you can use them all in the same way!
toys = [Robot(), Car(), Do      g()]
for toy in toys:
    toy.move()


'24.  ABSTRACTION'
'''Abstraction means showing only the essential features 
and hiding the unnecessary details. It helps reduce complexity 
and allows you to focus on what an object does, not how it does it.'''
class RemoteControl:
    def turn_on(self):
        print("TV is now ON")
remote = RemoteControl()
remote.turn_on()  # You just press the button!
        '''We dont always need parameters in the method or constructor because:
        We want to focus on what the object can do, not how it does it.
        The details (like how the toy works) are hidden inside the class.'''



'25. ENCAPSULATION'
 '''Encapsulation is a concept in object-oriented programming that hides the internal details 
 of a class and protects data from outside access. 
 In Python, we use private variables (with a single or double underscore _ or __)
   to indicate that they should not be accessed directly from outside the class.'''

class Person:
    def __init__(self, name):
        self.__name = name  # private variable
    
    def get_name(self):
        return self.__name  # public method to access private variable

'26. WHAT IS if __name__ == "__main__" STATEMENT USED FOR?'

 '''control the execution of code in Python scripts. 
 When a Python file is run directly, the special built-in 
 variable __name__ is set to "__main__".However, when that file is imported as a module
into another script, __name__ is set to the module's name instead.'''
    '''This allows developers to write code that acts differently depending on whether it’s run directly or imported. 
    It’s commonly used to encapsulate the script’s entry point'''

    def main():
        print("Running as a script")

    if __name__ == "__main__":
        main()


'27. WHAT IS A defaultdict IN PYTHON?'
  '''Normally, if you try to get a value for a key that doesnt exist in a regular dictionary, Python gives you an error.
But with a defaultdict, if the key doesnt exist, it automatically creates it with a default value!'''
from collections import defaultdict

# Create a defaultdict with default value 0
my_dict = defaultdict(int)

my_dict["apple"] += 1  # No error! "apple" gets value 1
print(my_dict["apple"])  # Output: 1
print(my_dict["banana"]) # Output: 0 (created automatically)

'28. HOW DOES PYTHON HANDLE MEMORY MANAGEMENT?'
'''Automatic Memory Management (Garbage Collection)
Python uses a built-in garbage collector that manages memory for you.
It mainly works through:
1. Reference Counting
2. Generational Garbage Collection (for cyclic references)'''
import sys

a = []          # an empty list
b = a           # another reference to the same list
print(sys.getrefcount(a))  # count how many references point to 'a', Once no references exist, Python automatically frees the memory.

'''2. Garbage Collection for Cyclic References
Reference counting fails when objects reference each other (cycles). 
Python’s garbage collector handles this.'''

import gc

class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()

a.ref = b
b.ref = a   # creates a cycle

del a
del b

print(gc.collect())  # manually trigger garbage collection

'''. Memory Allocation
 Python uses a private heap space for memory allocation.
 All Python objects and data structures are stored in this heap.
 The Python memory manager handles the allocation of this heap space.
 # Python also has an inbuilt memory allocator for small objects to optimize performance.
 # This allocator manages memory in blocks of various sizes to reduce fragmentation and improve allocation speed.
 # For larger objects, Python relies on the underlying system’s memory allocator.'''
import sys

x = 10
y = "hello"
z = [1, 2, 3, 4, 5]

print(sys.getsizeof(x))  # memory size of integer
print(sys.getsizeof(y))  # memory size of string
print(sys.getsizeof(z))  # memory size of list (just container, not elements!)


'29. WHAT IS A PACKAGE IN PYTHON?'
''' package in Python is a collection of modules organized in directories.
It allows you to group related modules together.
A package is a folder that contains an __init__.py file,
 which tells Python that the folder should be treated as a package. Example structure:
  ex --- :
mypackage/
│
├── __init__.py
├── module1.py
└── module2.py
'''

'30. WHAT IS THE PURPOSE OF __INIT__.PY IN PYTHON PACKAGES?'
'''
The __init__.py file in Python marks a directory as a package so that its modules can be imported. 
Without this file, Python won’t recognize the folder as a package in older versions (though in modern Python, it’s optional).
This file can be empty or contain initialization code for the package.
For example, you might import key modules or define variables inside it:

# __init__.py
from .module1 import function1
'''


'31. EXCEPTION HANDLING IN PYTHON'
'Exception handling in Python is done using the try, except, else, and finally blocks.'
'This allows your program to continue running even if something goes wrong. '
''' 1. try block contains code that might raise an error.
    2. except block handles the error.
    3. else runs if no error occurs.
    4. finally always runs, useful for cleanup.'''
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("No errors occurred.")
finally:
    print("This will always run.")


'32.WHAT ARE PYTHON DECORATORS?'
'''
Step 1: What’s a function?
A function is just some work you can ask Python to do.'''

def greet():
    print("Hello!")


' If you call greet(), Python does the work'
#Hello! That’s it — plain and simple.

'''🟢 Step 2: What if I want to add extra work?
Suppose every time before greeting, I want to clap my hands 👏, and after greeting, I want to say bye 👋.
Normally, I would rewrite the function:'''

def greet():
    print("👏 Clap Clap")
    print("Hello!")
    print("👋 Bye Bye")

'''
But what if I don’t want to touch greet()?
What if I want to keep it clean and reusable?

🟢 Step 3: Wrapper Idea
Instead of changing greet(), I can wrap it inside another function that adds extra work.'''

def add_extras(func):
    def wrapper():
        print("👏 Clap Clap")   # extra work before
        func()                 # original function
        print("👋 Bye Bye")    # extra work after
    return wrapper

'''
Here’s what’s happening:
func is the function we want to decorate (like greet)
wrapper is a new function that:
Does extra stuff before
Runs the real function
Does extra stuff after

🟢 Step 4: Decorating the Function
Now we decorate greet with add_extras:'''

@add_extras
def greet():
    print("Hello!")


'This is the same as writing:'

greet = add_extras(greet)

'''🟢 Step 5: Running It

When we call greet() now:'''



''' Dry Run (step by step):

Python sees @add_extras → replaces greet with wrapper
We call greet() → really calling wrapper()
wrapper() prints “Clap Clap”
Calls the original greet() → prints “Hello!”
Prints “ Bye Bye”

Output:

Clap Clap
Hello!
Bye Bye

'''
#func is the function we want to decorate (like greet)
# wrapper is a new function that:
#Does extra stuff before
# Runs the real function
# Does extra stuff after

'33. WHAT IS THE DIFFERENCE BETWEEN A SHALLOW COPY AND A DEEP COPY?'
'A shallow copy creates a new object, but inserts references into it to the objects found in the original.'
'A deep copy creates a new object and recursively adds copies of nested objects found in the original.'
import copy
original = [1, 2, [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
shallow[2][0] = 'X'
print(original)  # Output: [1, 2, ['X', 4]]
print(shallow)   # Output: [1, 2, ['X', 4]]
print(deep)      # Output: [1, 2, [3, 4]]


'34. WHAT IS A COUNTER IN PYTHON?'
'''A Counter is like a tally counter you use in a cricket match 🏏 or when counting chocolates 🍫.
It counts how many times each item appears.
'''
#example 1
from collections import counter 

fruits= ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
count= counter(fruits)
print(count)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 2})

#example 2
word = "balloon"
letter_count = Counter(word)
print(letter_count)
# Output: Counter({'l': 2, 'o': 2, 'b': 1, 'a': 1, 'n': 1}) 

#example 3
from collections import Counter

fruits = ["apple", "banana", "apple", "grape", "banana", "apple"]
count = Counter(fruits)

print(count.most_common())
# Output: [('apple', 3), ('banana', 2), ('grape', 1)]
print(count.most_common(1))   # top 1 item output: [('apple', 3)]
print(count.most_common(2))   # top 2 items output: [('apple', 3), ('banana', 2)]
print(count.elements())  # Output: <itertools.chain object at ...>

'35. WHAT IS THE LEGB RULE IN PYTHON?'

'''LEGB stands for Local → Enclosing → Global → Built-in, and it defines the order in which Python searches for variables:

    - Local: Names inside the current function.
    - Enclosing: Names in outer (but not global) functions if nested.
    - Global: Names defined at the top-level of a script or module.
    - Built-in: Python’s predefined names like len() or str.
'''

x = "global" # Global scope
def outer():
    x = "enclosing"     # Enclosing scope
    def inner():
        x = "local"  # Local scope
        print(x)
    inner()
outer()  # prints "local"
print(x)  # prints "global" 
print(len("hello"))  # Built-in scope, prints 5
# In this example:
# The inner function prints "local" because it finds x in its local scope first.
# The outer function has its own x, but inner() doesn’t use it.
# The print(x) outside any function accesses the global x.
# The len() function is a built-in function, so it’s found in the built-in scope. 
     

'36. HOW CAN YOU HANDLE FILE OPERATIONS IN PYTHON?'

#Python provides easy ways to work with files using built-in functions 
# like open(), read(), write(), and close().
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "w") as file:
    file.write("Hello, Python!")

'37. WHAT IS METHOD RESOLUTION ORDER (MRO) IN PYTHON?'
'Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes.'

print(ClassName.__mro__) 


class A: pass 
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)

'38.WHAT ARE PYTHON MAGIC METHODS?'

'Magic methods are special methods in Python that start and end with double underscores (__). '
'They allow you to define how your objects behave with built-in operations like addition,'
' string representation, and more. By implementing these methods, '
'you can make your custom classes work seamlessly with Pythons syntax and built-in functions.'
#Some common magic methods are:
'''
    __init__: Constructor, called when an object is created.
    __str__: Returns a string representation of the object.
    __len__: Returns the length using len().
    __add__: Defines behavior for + operator '''

class Book:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return f"Book: {self.title}"
book = Book("Python 101")
print(book)  # Output: Book: Python 101

'39. RECURSION IN PYTHON'
'Recursion is when a function calls itself to solve a smaller part of a problem.'
5!=1*2*3*4*5=120
def factorial:
    if n==0:
        return 1
    else:
        factoriral(n-1) * n
print(factorial(5))  # Output: 120
'''Every recursive function must have a base case to prevent infinite recursion. 
Python limits recursion depth by default (about 1000 calls).
You can check it using sys.getrecursionlimit() & set it using sys.setrecursionlimit(new_limit)
'''

'39. WHAT IS PYTHON MODULES AND HOW TO CREATE THEM?'
'''A module in Python is a file containing Python code (functions, classes, variables) that can be reused in other Python programs. 
Modules help organize code and promote code reuse.'''
# To create a module, simply create a Python file with a .py extension.
# For example, create a file named math_utils.py with the following content:
def add(a,b):
    return a+b
'You can use it in another file like this:'

import math_utils
print(math_utils.add(2, 3))

'40. WHAT ARE WEAK REFERENCES IN PYTHON?'
'''A weak reference is a reference to an object that does not prevent it from being garbage collected.
This is useful when you want to reference an object without increasing its reference count,
 allowing it to be cleaned up when no strong references exist.'''
import weakref  
class MyClass:
    def __init__(self, name):
        self.name = name    
obj = MyClass("example")
weak_ref = weakref.ref(obj)
print(weak_ref())  # Output: <__main__.MyClass object at ...>
del obj
print(weak_ref())  # Output: None (object has been garbage collected)
'''Weak references are often used in caching and memoization scenarios,
 where you want to keep track of objects without preventing their cleanup.'''   

'41. WHAT IS THE SUPER() FUNCTION IN PYTHON?'
'''The super() function in Python is used to call a method from a parent class.
It is commonly used in inheritance to access methods and properties of a base class from a derived class.'''
class Parent:
    def greet(self):
        return "Hello from Parent"
class Child(Parent):
    def greet(self):
        parent_greet = super().greet()  # Call the parent class method
        return f"{parent_greet} and Child"
child = Child()
print(child.greet())  # Output: Hello from Parent and Child
'''Using super() is especially useful in multiple inheritance scenarios,
as it helps ensure that the correct method resolution order (MRO) is followed.'''
    
    'TYPE 1: Single Inheritance'
class Parent:
    def hello(self):
        return "Hey kiddo!"
class Child(Parent):
    def trying_hello(self):
        #call the parent class method
        parent_hello = super().hello()
        return parent_hello + "hey mamma"
    
child_try = Child()
print(child_try.trying_hello())  # Output: Hey kiddo! hey mamma
    
    'TYPE 2: ADDING CONSTRUCTOR __INIT__ '
class Parent:
    def __init__(self):
        self.toy="car"
class Child:
    def __init__(self):
        super().__init__()
        self.game="lego"
child = Child()
print(child.toy)  # Output: car
print(child.game)  # Output: lego   

    'TYPE 3: MULTIPLE PARENTS SUPER() HELPS
class Mom:
    def skills(self):
        return "Cooking"

class Dad:
    def skills(self):
        return "Driving"

class Child(Mom, Dad):
    def skills(self):
        parent_skill = super().skills()
        return parent_skill + " + Painting"

c = Child()
print(c.skills())  # Output: Cooking + Painting

'42. MRO = METHOD RESOLUTION ORDER'
'Its just the order in which Python looks for methods/attributes when you call them on an object'
'''Child inherits from Parent
So, when Python looks for something on Child, the MRO is:
Child → Parent → object
Python checked:
“Who comes after Child in the MRO?” → That’s Parent.
So Parent.__init__ got called.
If Parent also had a super(), Python would continue further along the MRO.'''

print(Child.__mro__) # Output : (<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>)

'43. WHAT IS COLLECTIONS.DEQUE AND WHY IS IT BETTER THAN A LIST FOR SOME USE CASES?'
'collections.deque (double-ended queue) is a data structure that allows you to add or remove elements from both ends efficiently.'
'deque has doubly linked list internally allowing O(1) operations on both ends'

from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)  # fast insert at the beginning
dq.pop()          # fast removal from end
'It is ideal for queue and stack implementations, sliding windows, and breadth-first searches.'


'44.  WHAT IS THE DIFFERENCE BETWEEN @STATICMETHOD AND @CLASSMETHOD IN PYTHON?'
'''
'@staticmethod is a method that does not receive an implicit first argument (neither self nor cls).
 It behaves like a regular function but belongs to the class’s namespace. 
 It cannot access or modify class or instance state. refer pointer 32
'''
class MyClass:
    @staticmethod
    def static_method():
        return "I am a static method"
print(MyClass.static_method())  # Output: I am a static method

'@classmethod, on the other hand, receives the class (cls) as its first argument.'
'It can access and modify class state that applies across all instances of the class.'
class MyClass:
    class_variable = "I am a class variable"
    
    @classmethod
    def class_method(cls):
        return f"{cls.class_variable} accessed via class method"
print(MyClass.class_method())  # Output: I am a class variable accessed via class method    

'45. WHAT IS PYTHON ANNOTATIONS or TYPE HINT'

'''Python annotations, also known as type hints,
 are a way to specify the expected data types of function arguments and return values.'''
example:
def greet(name: str) -> str:
    return f"Hello, {name}!"        
#or 
def add(a: int, b: int) -> int:
    return a + b
'In this example, the greet function expects a string argument and returns a string.'


'46. HOW DOES EXCEPTION HANDLING WORK IN PYTHON?'
'''
Exception handling in Python is done using try, except, finally, and else blocks.
 It helps your program handle unexpected errors without crashing.
   You wrap the code that might throw an error in a try block, 
   then use except to handle specific or general exceptions.
'''
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This will always run.")
else:
    print("No errors occurred.")  # Output: Cannot divide by zero. This will always run.    
# The finally block always runs, whether an exception occurred or not.
# The else block runs only if no exceptions were raised in the try block.


'47.  WHAT IS A TERNARY OPERATOR IN PYTHON?'
'''A ternary operator in Python is a concise way to write an if-else statement in a single line.
    It allows you to assign a value to a variable based on a condition.'''
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
'''In this example, if age is 18 or older, status is set to "Adult"; otherwise, it is set to "Minor".'''        

'48. WHAT ARE PYTHON ASSERTIONS?'
'''Assertions are a way to test if a condition is true during development.
 If the condition is false, an AssertionError is raised, which helps catch bugs early.'''
x = 10
assert x > 0, "x should be positive"  # No error, as x is positive
assert x < 0, "x should be negative"  # Raises AssertionError: x should be negative
'''Assertions are typically used for debugging and should not be used for regular error handling in production code.''' 

'49. WHAT IS THE DIFFERENCE BETWEEN A LIST AND A TUPLE IN PYTHON?  '
'''Lists and tuples are both used to store collections of items in Python,
 but they have some key differences:
1. Mutability:
   - Lists are mutable, meaning you can change, add, or remove elements after creation.
   - Tuples are immutable, meaning once they are created, their elements cannot be changed.
2. Syntax:
   - Lists are defined using square brackets [].
   - Tuples are defined using parentheses ().
3. Performance:
   - Tuples are generally faster than lists for certain operations due to their immutability.'''
# Example of a list
my_list = [1, 2, 3]
my_list[0] = 10  # Modifying the first element
my_list.append(4)  # Adding an element
print(my_list)  # Output: [10, 2, 3, 4]     

# Example of a tuple
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise a TypeError
# my_tuple.append(4)  # This would also raise an AttributeError
print(my_tuple)  # Output: (1, 2, 3)
# Tuples can be used as keys in dictionaries, while lists cannot
my_dict = {my_tuple: "value"}
print(my_dict)  # Output: {(1, 2, 3): 'value


'50. WHAT IS THE WITH STATEMENT IN PYTHON AND WHY IS IT USED?'
'''The with statement in Python is used to wrap the execution of a block of code within methods defined by a context manager.
 It is commonly used for resource management, such as file handling, where it ensures that resources are properly acquired and released.'''
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: (contents of example.txt)
'''In this example, the with statement automatically handles opening and closing the file.
 Even if an error occurs while reading the file, it will still be closed properly.'''   

' 51. WHAT AR ETHE BENFTS OF USING PYTHON?'
'''
1. Easy to Learn and Use: Python has a simple syntax that is easy to read and write, making it accessible for beginners.
2. Versatile: Python can be used for web development, data analysis, artificial intelligence, scientific computing, automation, and more.
3. Large Standard Library: Python comes with a vast standard library that provides modules and functions for various tasks, reducing the need to write code from scratch.
4. Strong Community Support: Python has a large and active community that contributes to a wealth of resources, tutorials, and third-party libraries.
5. Cross-Platform: Python is available on multiple operating systems, including Windows, macOS, and Linux, allowing for easy portability of code.
6. Integration Capabilities: Python can easily integrate with other languages and technologies, making it suitable for a wide range of applications.
7. High Productivity: Python’s simplicity and extensive libraries enable developers to write code quickly and efficiently, leading to faster development cycles.
8. Support for Multiple Programming Paradigms: Python supports procedural, object-oriented, and functional programming styles, providing flexibility in coding approaches.
9. Strong in Data Science and Machine Learning: Python has become the go-to language for data science and machine learning due to libraries like NumPy, pandas, TensorFlow, and scikit-learn.
10. Extensive Frameworks: Python has powerful frameworks like Django and Flask for web development, making it easier to build robust applications.
''' 

'52. WHAT BUILT IN DATA TYPES in PYTHON'
'''
1. Numeric Types: int, float, complex
2. Sequence Types: list, tuple, range
3. Text Type: str
4. Set Types: set, frozenset
5. Mapping Type: dict
6. Boolean Type: bool
7. Binary Types: bytes, bytearray, memoryview
'''


'53. HOW TO MANAGE PACKAGES IN PYTHON? '
'''Package management in Python is typically done using tools like pip and virtual environments.'''
# Using pip to install a package
!pip install package_name
# Using pip to uninstall a package
!pip uninstall package_name
# Creating a virtual environment
!python -m venv myenv
# Activating a virtual environment (Windows)'
!myenv\Scripts\activate
# Activating a virtual environment (macOS/Linux)
!source myenv/bin/activate
# Deactivating a virtual environment
!deactivate
'''Virtual environments help isolate project dependencies, ensuring that each project can have its own set of packages without conflicts.'''

'54. HOW TO WORK WITH DATES AND TIMES IN PYTHON?'
'''Python provides the datetime module to work with dates and times.'''
from datetime import datetime, timedelta        
# Getting the current date and time
now = datetime.now()
print(now)  # Output: Current date and time
# Creating a specific date
specific_date = datetime(2023, 1, 1)
print(specific_date)  # Output: 2023-01-01 00:00:00
# Formatting dates
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # Output: Formatted current date and time
# Parsing dates from strings
parsed_date = datetime.strptime("2023-01-01", "%Y-%m-%d")
print(parsed_date)  # Output: 2023-01-01 00:00:00
# Date arithmetic
tomorrow = now + timedelta(days=1)
print(tomorrow)  # Output: Date and time for tomorrow
yesterday = now - timedelta(days=1)
print(yesterday)  # Output: Date and time for yesterday
# Getting the difference between two dates
date_diff = specific_date - now
print(date_diff.days)  # Output: Number of days between specific_date and now   '

     
' 54. What is Scope?'
'''Python decides where to look for variables using the LEGB rule:
Local (L) → Inside the current function.
Enclosing (E) → In the function that wrapped around the current one.
Global (G) → Defined at the top level of the file.
Built-in (B) → Predefined names in Python (like len, print, max).'''

x = "global"   # Global scope

def outer():
    x = "enclosing"   # Enclosing scope
    def inner():
        x = "local"   # Local scope
        print(x)      # Python looks for x here first
    inner()

outer()
print(x)  # Uses global
print(len("hello"))  # Built-in


'55. WHAT IS THE DIFFERENCE BETWEEN Tuple & LIST?'
'''Lists are mutable, meaning you can change, add, or remove elements after creation.
Tuples are immutable, meaning once they are created, their elements cannot be changed.
Lists are defined using square brackets [].
Tuples are defined using parentheses ().
Tuples are generally faster than lists for certain operations due to their immutability.'''
# Example of a list
my_list = [1, 2, 3]
my_list[0] = 10  # Modifying the first element
my_list.append(4)  # Adding an element
print(my_list)  # Output: [10, 2, 3, 4]

# Example of a tuple
my_tuple = (1, 2, 3)            
# my_tuple[0] = 10  # This would raise a TypeError
# my_tuple.append(4)  # This would also raise an AttributeError
print(my_tuple)  # Output: (1, 2, 3)
# Tuples can be used as keys in dictionaries, while lists cannot
my_dict = {my_tuple: "value"}
print(my_dict)  # Output: {(1, 2, 3): 'value'}  
