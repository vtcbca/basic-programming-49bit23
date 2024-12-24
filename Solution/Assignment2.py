def fibonacci_iterative_terms(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def fibonacci_iterative_max_value(max_value):
    fib_sequence = []
    a, b = 0, 1
    while a < max_value:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
n_terms = 10
max_value = 100
print(f"Fibonacci sequence up to {n_terms} terms: {fibonacci_iterative_terms(n_terms)}")
print(f"Fibonacci sequence less than {max_value}: {fibonacci_iterative_max_value(max_value)}")
