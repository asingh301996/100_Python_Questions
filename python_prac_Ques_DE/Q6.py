'''
Find Unique Elements
Find the number of unique elements of a list: In: [1,3,4,5,6,7] Out: 6  
In: [1,1,3,4,5,5,6,7] Out: 6 (1 and 5 are duplicated and should be counted once)
'''

def find_unique_elements(lst):
    # # your code here
    # dict_unique_no = {}
    # for num in lst:
    #     if num not in dict_unique_no:
    #         dict_unique_no[num] = 1
    #     else:
    #         dict_unique_no[num] += 1
    
    # return len(dict_unique_no)
    # OR
    set_unique_no= set(lst)
    return (len(set_unique_no))