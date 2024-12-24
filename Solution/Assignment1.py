from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

# Example usage
n = 5
print(f"Factorial of {n} is {factorial_reduce(n)}")
