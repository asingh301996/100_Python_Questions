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
print(multiply_all(a=2,b=3,c=4)) ''' this will create a dict -> {'a':2,'b':3,'c':4 }--> kwargs is a dictionary   ''' 

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

'''DELETE & REMOVE() '''
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

 




