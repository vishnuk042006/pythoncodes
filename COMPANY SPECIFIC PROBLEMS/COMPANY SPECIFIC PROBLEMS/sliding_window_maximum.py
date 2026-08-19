# Q27. Sliding Window Maximum
from collections import deque

def sliding_max(A, K):
    dq = deque()
    res = []
    for i, x in enumerate(A):
        while dq and dq[0] < i - K + 1:
            dq.popleft()
        while dq and A[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if i >= K - 1:
            res.append(A[dq[0]])
    return res

if __name__ == "__main__":
    N, K = map(int, input("Enter N and K: ").split())
    A = list(map(int, input("Enter array: ").split()))
    print(*sliding_max(A, K))
