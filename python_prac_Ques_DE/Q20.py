'''
Find the Maximum Class Edition
Similarly to the previous exercise, find the maximum number of a list. This time, use a class instead. When initializing MaxNumberFinder you will need to provide nums as an argument



finder = MaxNumberFinder([1,3,4,2])
finder.find_max_number() #output 4
'''

class MaxNumberFinder:
    def __init__(self, nums):
        # your code here
        self.nums= nums   # Store the list in the object
        

    def find_max_number(self):
        # your code here
        if not self.nums:
            return None
            
        max_no= self.nums[0] # Assume the first number is max
        
        for no in self.nums:
            if no > max_no:
                max_no= no
                
        return max_no
    
    #OR
    
class MaxNumberFinder:
    def __init__(self, nums):
        # your code here
        self.nums= nums   # Store the list in the object
        if self.nums:
            max_no= max(self.nums)
            return max_no
        else:
            return None
        