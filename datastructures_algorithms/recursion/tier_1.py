# 01 Factorial Easy
# Compute n! recursively. What's the base case, and what should happen if n is 0?

def factorial(n):
    # Base case
    if n == 0:
        return 1
    elif n <=0:
        print("(-n)! is undefined")
        return None
    
    return n * factorial(n - 1)


# 02 Sum of 1 to N Easy
# Sum the first n natural numbers without a single loop.

def sum_of_natural_numbers(n):
    # Base case
    if n == 0:
        return 0
    elif n <=0:
        print("The natural numbers set -> 1, 2, 3, ..., N")
        return None
       
    return n + sum_of_natural_numbers(n - 1)

# 03 Naive power Easy
# Compute x to the power n the obvious recursive way. What's its time complexity?

def naive_power(x, n):
    # Base Case (Positive Integers/Natural Numbers)
    if n == 0:
        return 1
    
    # Negative numbers check
    if n < 0:
        print("n is outside the scope of this exercise.")    
        return None
    
    return x * naive_power(x, n - 1)

print(naive_power(2, -3))