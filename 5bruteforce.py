import time

# Brute-force Algorithm for Power Calculation
def power_brute_force(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

# Divide and Conquer Algorithm for Power Calculation
def power_divide_and_conquer(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = power_divide_and_conquer(a, n // 2)
        return half_power * half_power
    else:
        half_power = power_divide_and_conquer(a, (n - 1) // 2)
        return a * half_power * half_power

if __name__ == "__main__":
    a = 2
    n = 10
    print(f"{a}^{n} using brute-force: {power_brute_force(a, n)}")
    print(f"{a}^{n} using divide and conquer: {power_divide_and_conquer(a, n)}")

    # Measuring time for different n values
    n_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    bf_times = []
    dc_times = []

    for n in n_values:
        start_time = time.time()
        power_brute_force(a, n)
        end_time = time.time()
        bf_times.append((end_time - start_time) * 1000)  # Convert to milliseconds

        start_time = time.time()
        power_divide_and_conquer(a, n)
        end_time = time.time()
        dc_times.append((end_time - start_time) * 1000)  # Convert to milliseconds

    # Plotting the results
    import matplotlib.pyplot as plt

    plt.plot(n_values, bf_times, '-o', label='Brute-force')
    plt.plot(n_values, dc_times, '-o', label='Divide and Conquer')
    plt.xlabel("Exponent (n)")
    plt.ylabel("Time Taken (milliseconds)")
    plt.title("Power Calculation Time Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()
