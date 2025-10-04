'''
Check for Prime Numbers
Create a function called is_prime that takes an integer as input and returns True if the number is prime and False otherwise. Your function should use only built-in Python tools.



>>> is_prime(5)
True
>>> is_prime(17)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
'''
def is_prime(number):
    # Your code here
    if number<=1:
        return False
    for i in range (2,(int(number**0.5)+1)):
            if number % i ==0:
                return False
     
    return True   

        
    
    
