'''
Calculate Sum of Digits
Write a function called sum_of_digits that takes a positive integer
 as an argument and returns the sum of its digits.
 Further string manipulation.
'''

def sum_of_digits(num: int):
    # num will be an integer
    total=0
    while num > 0:
        num_last = num%10
        total = total + num_last
        num = num//10
    return total


