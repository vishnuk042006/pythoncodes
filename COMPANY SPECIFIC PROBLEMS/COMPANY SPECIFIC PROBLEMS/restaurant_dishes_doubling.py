
from collections import Counter
def max_dishes(A):
    freq = sorted(Counter(A).values())  
    best = 0
    for s in set(freq):
        total = 0
        req = s
        for val in freq:
            if val >= req:
                total += req
                req *= 2
        best = max(best, total)
    return best

if __name__ == "__main__":
    N = int(input("Enter N: "))
    A = [int(input()) for _ in range(N)]
    print(max_dishes(A))
