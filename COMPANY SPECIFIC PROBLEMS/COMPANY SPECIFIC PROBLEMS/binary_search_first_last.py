# Q15. Binary Search - First & Last Occurrence
import bisect

def first_last(A, T):
    lo = bisect.bisect_left(A, T)
    hi = bisect.bisect_right(A, T) - 1
    if lo > hi or A[lo] != T:
        return -1, -1
    return lo, hi

if __name__ == "__main__":
    A = list(map(int, input("Enter sorted array: ").split()))
    T = int(input("Enter target: "))
    print(*first_last(A, T))
