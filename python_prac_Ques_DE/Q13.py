'''
Calculate Average
Write a Python program that calculates the average of a list of numbers.

In:  [5, 10, 15, 20]

Out:  12.5

If the list is empty, return 0
'''

def calculate_average(numbers):
    if len(numbers)<= 0 :
        return 0
    else :
        average_list= sum(numbers)/len(numbers)
        return average_list