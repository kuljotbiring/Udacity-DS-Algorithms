# fibonacci recursive pythonic easy
def new_fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# recursive method
"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""


def get_fib(position):
    # if user entered a negative number
    if position < 0:
        return -1

    # if user entered a 0 or 1
    if position == 0 or position == 1:
        return position

    # make recursive call adding the two values and working back down the sequence
    return get_fib(position - 1) + get_fib(position - 2)


# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))


# Call iterative version
print(new_fib(0))
print(new_fib(8))
