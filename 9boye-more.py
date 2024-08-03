def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)

    if m == 0:
        return 0

    last_occurrence = {}
    for i in range(m):
        last_occurrence[pattern[i]] = i

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            print("Pattern occurs at position", s)
            s += (m - last_occurrence.get(text[s + m], -1))
        else:
            s += max(1, j - last_occurrence.get(text[s + j], -1))

if __name__ == "__main__":
    text = "ABAAABCD"
    pattern = "ABC"
    boyer_moore(text, pattern)
