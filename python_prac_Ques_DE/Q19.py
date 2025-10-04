'''
Check Balanced Parentheses
Create a function called is_balanced_parentheses that takes a string containing only parentheses, brackets, and curly braces as input and returns True if the parentheses are balanced and False otherwise. The parentheses are considered balanced if they are closed in the correct order. Your function should use only built-in Python tools.



>>> is_balanced_parentheses("()")
True
>>> is_balanced_parentheses("()[]{}")
True
>>> is_balanced_parentheses("(]")
False
>>> is_balanced_parentheses("([)]")
False
>>> is_balanced_parentheses("{[]}")
True

'''

def is_balanced_parentheses(s):
    # Your code here
    #{[}] 
    dict_map= {'(':')','[':']','{':'}'}
    stack=[]
    for char in s:
        ##just in case of opening bracket it'll append 
        if char in dict_map: 
            stack.append(char)
        
        ##if char is closig braces then Check if the popped opening bracket matches the current closing bracket    
        elif char in dict_map.values(): 
            if not stack:
                return False
                
               # Pop the last opening bracket    
            last_opened_bracket= stack.pop() #open bracket
            
             ## If it doesn't match the current closing bracket, return False
            if dict_map[last_opened_bracket] != char: #  # If it doesn't match the current closing bracket, it's unbalanced
                return False
    
    
    if stack:
        return False
    return True
            
            
        
            
    if stack:
        return False
    return True
        
            