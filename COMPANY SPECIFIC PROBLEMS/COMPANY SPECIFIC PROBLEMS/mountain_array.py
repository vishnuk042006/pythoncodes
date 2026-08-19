
def min_changes(A):
    N = len(A)
    dist = [min(i, N - 1 - i) for i in range(N)]
    candidates = set(A[i] - dist[i] for i in range(N))
    best = 0
    for V in candidates:
        matches = sum(1 for i in range(N) if A[i] == V + dist[i])
        best = max(best, matches)
    return N - best

if __name__ == "__main__":
    N = int(input("Enter N: "))
    A = list(map(int, input("Enter array: ").split()))
    print(min_changes(A))
