'''
Create a function called remove_duplicates that takes a list of elements as input and returns a new list with duplicates removed. Your function should use only built-in Python tools and should maintain the original order of elements while removing duplicates.

>>> remove_duplicates([1, 2, 2, 3, 4, 4, 5])
[1, 2, 3, 4, 5]
>>> remove_duplicates(['apple', 'banana', 'apple', 'cherry'])
['apple', 'banana', 'cherry']
>>> remove_duplicates([1, 2, 3])
[1, 2, 3]
>>> remove_duplicates([])
[]
 
'''

def remove_duplicates(input_list):
    # Your code here
    #return list(set(input_list)) # set cannot be used as order will matter here 
    unique_dict= {}
    result=[]
    
    for item in input_list:
        if item not in unique_dict:
            unique_dict[item]= 1 # Set the count to 1 if it's the first occurrence
            result.append(item)
             
        else:
            unique_dict[item] += 1 # Increment the count if the item is already in the dictionary
# Now, return a list of elements that have a count of 1 (no duplicates)
    return result  
    
#OR 
    result=[]
    
    for items in input_list:
        if items not in result:
            result.append(items)
    return result

