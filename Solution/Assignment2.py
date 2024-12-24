def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    if i > math.sqrt(n):
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)

# Example usage
n = 29
print(f"Is {n} prime? {is_prime_recursive(n)}")
