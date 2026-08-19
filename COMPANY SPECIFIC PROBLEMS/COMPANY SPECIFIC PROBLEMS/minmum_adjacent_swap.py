N = int(input())
A = list(map(int, input().split()))

swaps = 0

for i in range(N):
    for j in range(i, N - 1):
        if A[j] % 2 == 0 and A[j + 1] % 2 == 1:
            A[j], A[j + 1] = A[j + 1], A[j]
            swaps += 1
            break

print(swaps)