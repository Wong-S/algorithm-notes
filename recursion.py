# TO increase stack memory.....
# import sys
# sys.setrecursionlimit(1000)

# =================


def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")

    else:
        recursiveMethod(n - 1)
        print(n)


# =============================
# Factorial
# n! = n * (n-1)!


def factorial(n):
    # Step 3: Unintentional case -- factorial only takes positive numbers, so deal with negatives using assert method.
    # Make sure it's a positive number AND an integer. If not, it'll throw an exception. We are forcing "n" to not be a non negative integer
    # Note: Running the function with floats will throw an error
    assert n >= 0 and int(n) == n, "The number must be positive integer only!"

    if n in [0, 1]:  # Step 2: Base case
        return 1
    else:
        return n * factorial(n - 1)  # Step 1: Recursive case


print(factorial(3))
