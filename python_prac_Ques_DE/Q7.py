'''
Reverse a String
Create a function called reverse_string that takes a string as input and returns a new string with its characters reversed. Your function should use only built-in Python tools.



>>> reverse_string("Hello, World!")
"!dlroW ,olleH"
>>> reverse_string("Python")
"nohtyP"
>>> reverse_string("")
""
'''

#Sol 1 
def reverse_string(input_string):
    return (input_string[::-1])

#Sol 2
def reverse_string(input_string):
    reversed_str= ""
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str

#sol 3

def reverse_string(input_string):
    lst= list(input_string) #lst= ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!' ]
    #reverse_lst= lst[::-1]
    # step 2: reverse in-place
    lst.reverse()
    return "".join(lst)

# sol 4
def reverse_string(input_string):
    lst= list(input_string) #lst= ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!' ]
    left_ptr=0
    right_ptr = len(lst) -1
    while left_ptr< right_ptr:
        #swapping
        lst[left_ptr],lst[right_ptr] = lst[right_ptr],lst[left_ptr]
        left_ptr += 1
        right_ptr -= 1

    return "".join(lst) 


# Test cases
print(reverse_string("Hello, World!"))  # Output: "!dlroW ,olleH"
