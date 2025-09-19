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


