def power_bruteforce(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result

def power_divide_conquer(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power_divide_conquer(a * a, n // 2)
    else:
        return a * power_divide_conquer(a * a, n // 2)

# Main Code
a, n = map(int, input("Enter the value of a and n: ").split())

result_brute = power_bruteforce(a, n)
result_divide_conquer = power_divide_conquer(a, n)

print("Result using brute force:", result_brute)
print("Result using divide and conquer:", result_divide_conquer)