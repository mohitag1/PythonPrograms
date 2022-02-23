#4)Python program to find the factorial of a number using recursion
num=7
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
       return( n* factorial(n-1))

factorial = factorial(num)
print("factorial of %d is %d" %(num,factorial))
    
