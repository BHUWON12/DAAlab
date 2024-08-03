def subset_sum(S, d):
    result = []
    n = len(S)

    def backtrack(start, current_sum, current_subset):
        if current_sum == d:
            result.append(list(current_subset))
            return
        if current_sum > d:
            return
        for i in range(start, n):
            current_subset.append(S[i])
            backtrack(i + 1, current_sum + S[i], current_subset)
            current_subset.pop()

    backtrack(0, 0, [])
    return result

if __name__ == "__main__":
    S = [1, 2, 5, 6, 8]
    d = 9
    solutions = subset_sum(S, d)
    if solutions:
        print("Solutions:", solutions)
    else:
        print("No solution found.")
