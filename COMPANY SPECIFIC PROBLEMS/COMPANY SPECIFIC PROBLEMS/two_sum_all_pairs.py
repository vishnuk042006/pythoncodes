# Q28. Two Sum - All Unique Pairs
def all_pairs(A, K):
    seen = set()
    pairs = set()
    for x in A:
        if K - x in seen:
            pairs.add((min(x, K - x), max(x, K - x)))
        seen.add(x)
    return sorted(pairs)

if __name__ == "__main__":
    N, K = map(int, input("Enter N and K: ").split())
    A = list(map(int, input("Enter array: ").split()))
    pairs = all_pairs(A, K)
    if not pairs:
        print(-1)
    else:
        for a, b in pairs:
            print(a, b)
