# 01 Factorial Easy
# Compute n! recursively. What's the base case, and what should happen if n is 0?

def factorial(n):
    # Base case
    print(n)
    if n == 0:
        return 1
    
    return n * factorial(n - 1)


# 02 Sum of 1 to N Easy
# Sum the first n natural numbers without a single loop.

def sum_of_natural_numbers(n):
    # Base case
    if n == 0:
        return 0
       
    return n + sum_of_natural_numbers(n - 1)