import time
import matplotlib.pyplot as plt

def evaluate_polynomial_brute_force(coefficients, x):
    n = len(coefficients)
    result = 0
    for i in range(n):
        result += coefficients[i] * (x ** i)
    return result

#### Horner’s Rule
def evaluate_polynomial_horner(coefficients, x):
    n = len(coefficients)
    result = coefficients[n - 1]
    for i in range(n - 2, -1, -1):
        result = result * x + coefficients[i]
    return result

def measure_polynomial_evaluation(coefficients, x):
    start = time.time()
    evaluate_polynomial_brute_force(coefficients, x)
    end = time.time()
    brute_force_time = (end - start) * 1000

    start = time.time()
    evaluate_polynomial_horner(coefficients, x)
    end = time.time()
    horner_time = (end - start) * 1000

    return brute_force_time, horner_time

coefficients = [1, 2, 3, 4, 5]  # Example coefficients for polynomial 1 + 2x + 3x^2 + 4x^3 + 5x^4
x = 2  # Example value of x
n_values = list(range(1, 1001))
brute_force_times = []
horner_times = []

for n in n_values:
    coeffs = [i for i in range(n)]
    bf_time, hr_time = measure_polynomial_evaluation(coeffs, x)
    brute_force_times.append(bf_time)
    horner_times.append(hr_time)

plt.plot(n_values, brute_force_times, label='Brute-force')
plt.plot(n_values, horner_times, label="Horner's Rule")
plt.xlabel('Number of terms in polynomial')
plt.ylabel('Time taken (milliseconds)')
plt.title('Polynomial Evaluation Time Complexity')
plt.legend()
plt.grid(True)
plt.show()
