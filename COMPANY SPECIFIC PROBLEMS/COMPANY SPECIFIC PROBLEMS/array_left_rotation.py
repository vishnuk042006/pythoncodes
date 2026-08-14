# Q5. Array Left Rotation
def left_rotate(A, K):
    N = len(A)
    K %= N
    return A[K:] + A[:K]

if __name__ == "__main__":
    N, K = map(int, input("Enter N and K: ").split())
    A = list(map(int, input("Enter array: ").split()))
    print(*left_rotate(A, K))
