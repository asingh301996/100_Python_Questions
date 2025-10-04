'''
Fibonacci Series
Write a program that generates the Fibonacci series up to a given number 'n'.

fibonacci(0) -> []

fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8]

fibonacci(23) -> [0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
        
    fib_series=[0,1]
    i=2
    while i<= n:
        next_num= fib_series[-1]+fib_series[-2]
        
        if next_num<n:
            fib_series.append(next_num)
            i+=1
        else:
            break
    return fib_series