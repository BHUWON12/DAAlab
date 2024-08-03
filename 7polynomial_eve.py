import time

def brute_force_polynomial(coeffs, x):
    result = 0
    for i, coeff in enumerate(coeffs):
        result += coeff * (x ** i)
    return result

def horners_rule(coeffs, x):
    result = 0
    for coeff in reversed(coeffs):
        result = result * x + coeff
    return result

# Example coefficients for polynomial P(x) = 2x^3 + 3x^2 + 4x + 5
coeffs = [5, 4, 3, 2]
x = 2

# Measure performance of brute-force method
start_time = time.time()
bf_result = brute_force_polynomial(coeffs, x)
bf_time = time.time() - start_time

# Measure performance of Horner's rule
start_time = time.time()
hr_result = horners_rule(coeffs, x)
hr_time = time.time() - start_time

print(f"Brute-Force Result: {bf_result}, Time: {bf_time:.10f} seconds")
print(f"Horner's Rule Result: {hr_result}, Time: {hr_time:.10f} seconds")
