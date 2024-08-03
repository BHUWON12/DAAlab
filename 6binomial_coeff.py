import time

# Brute-force Algorithm for Binomial Coefficient
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def binomial_coefficient_brute_force(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Dynamic Programming Algorithm for Binomial Coefficient
def binomial_coefficient_dynamic(n, k):
    # Initialize a table to store intermediate results
    C = [[0 for x in range(k + 1)] for x in range(n + 1)]

    # Calculate value of binomial coefficient
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base cases
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                # Calculate value using previously stored values
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    
    return C[n][k]

if __name__ == "__main__":
    n = 5
    k = 2
    print(f"C({n}, {k}) using brute-force: {binomial_coefficient_brute_force(n, k)}")
    print(f"C({n}, {k}) using dynamic programming: {binomial_coefficient_dynamic(n, k)}")

    # Measuring time for different n values
    n_values = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    k = 2  # Fixed k value for simplicity
    bf_times = []
    dp_times = []

    for n in n_values:
        start_time = time.time()
        binomial_coefficient_brute_force(n, k)
        end_time = time.time()
        bf_times.append((end_time - start_time) * 1000)  # Convert to milliseconds

        start_time = time.time()
        binomial_coefficient_dynamic(n, k)
        end_time = time.time()
        dp_times.append((end_time - start_time) * 1000)  # Convert to milliseconds

    # Plotting the results
    import matplotlib.pyplot as plt

    plt.plot(n_values, bf_times, '-o', label='Brute-force')
    plt.plot(n_values, dp_times, '-o', label='Dynamic Programming')
    plt.xlabel("n")
    plt.ylabel("Time Taken (milliseconds)")
    plt.title("Binomial Coefficient Calculation Time Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()
