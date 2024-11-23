# reccursion in python
"""In Python, we know that a function can call other
functions. It is even possible for the function to call
itself. These types of construct are termed as recursive
functions."""

print("------------------------factorial----------------------------------")
#  factorial(n) = n * factorial(n-1)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1


print("-------------------ffffiiiibbbbbbooooo----------------------------------")


def fibo(n):

    f0 = 0
    f1 = 1

    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


# Test the function

print(fibo(10))

# In the above program, fibo(n) calls fibo(n-1) and fibo(n-2)
# This is a recursive call. The function calls itself. The recursion ends when n is less than
#  1 or equal to 1.

# The base cases are when n is 0 or 1. In these cases, the function returns n.
# For other values of n, the function calls itself with the arguments n-1 and n-2
