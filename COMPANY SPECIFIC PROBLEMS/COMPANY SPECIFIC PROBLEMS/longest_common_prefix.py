# Q17. Longest Common Prefix
def longest_common_prefix(words):
    words = sorted(words)
    a, b = words[0], words[-1]
    res = ''
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        res += a[i]
        i += 1
    return res

if __name__ == "__main__":
    N = int(input("Enter N: "))
    words = [input() for _ in range(N)]
    print(longest_common_prefix(words))
