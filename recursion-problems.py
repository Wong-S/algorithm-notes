# Q1: How to Find the sum of digits of a positive integer number using recursion


def sumOfDigits(n):

    # Number MUST be integer and MUST be positive
    assert (
        n >= 0 and int(n) == n
    ), "The number has to be positive integer only!"  # Step 3: Unintentional case

    if n == 0:  # Step 2: Base case
        return 0

    else:
        return int(n % 10) + sumOfDigits(int(n / 10))  # Step 1: Recursive case


print(sumOfDigits(1234))

# ============================

