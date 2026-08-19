# Q24. Lexicographically Smallest Array - One K-Distance Swap
def smallest_with_one_swap(A, K):
    A = A[:]
    N = len(A)
    for i in range(N):
        mn = A[i]
        idx = i
        for j in range(i + 1, min(i + K + 1, N)):
            if A[j] < mn:
                mn = A[j]
                idx = j
        if idx != i:
            A[i], A[idx] = A[idx], A[i]
            break
    return A

if __name__ == "__main__":
    N, K = map(int, input("Enter N and K: ").split())
    A = list(map(int, input("Enter array: ").split()))
    print(*smallest_with_one_swap(A, K))
