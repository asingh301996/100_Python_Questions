'''
Find the Missing Number
Write a function called find_missing_number that takes a list of unique integers. The list contains all numbers from 0 to n except one missing number, where n is the number the list would have if no numbers were missing (i.e. n = len(list)).

Your task is to identify and return the missing number.

You may assume:

The input list contains no duplicates.

The input list is unordered.

The list is missing exactly one number from the complete sequence.



>>> find_missing_number([0, 1, 3])
2
>>> find_missing_number([4, 1, 3, 2, 0, 6, 7, 5])
8
>>> find_missing_number([9, 7, 2, 1, 0, 6, 8, 4, 5, 3])
10
>>> find_missing_number([])
0
'''

# def find_missing_number(nums):
#     # Your code here
#     sorted_nums=nums.sort()
#     n=len(nums)
#     print (sorted_nums)




# print(find_missing_number([0, 1, 3]))


nums= [4, 1, 3, 2, 0, 6, 7, 5]
sorted_nums=nums.sort()
n=len(nums)
print (sorted_nums)