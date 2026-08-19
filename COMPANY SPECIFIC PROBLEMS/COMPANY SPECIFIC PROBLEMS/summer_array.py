# Q2. Summer Array - Minimum Adjacent Swaps (all evens on one side, odds on other)
def min_swaps(A):
    A = A[:]
    N = len(A)
    swaps = 0
    for i in range(N):
        for j in range(i, N - 1):
            if A[j] % 2 == 0 and A[j + 1] % 2 == 1:
                A[j], A[j + 1] = A[j + 1], A[j]
                swaps += 1
                break
    return swaps

if __name__ == "__main__":
    N = int(input("Enter N: "))
    A = list(map(int, input("Enter array: ").split()))
    print(min_swaps(A))
