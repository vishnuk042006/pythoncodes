
from collections import defaultdict

def count_pairs(A, K):
    freq = defaultdict(int)
    count = 0
    for x in A:
        count += freq[K - x]
        freq[x] += 1
    return count

if __name__ == "__main__":
    N, K = map(int, input("Enter N and K: ").split())
    A = list(map(int, input("Enter array: ").split()))
    print(count_pairs(A, K))
