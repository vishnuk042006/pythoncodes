# LC2. Merge Two Sorted Arrays
def merge_sorted(A, B):
    res = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    return res + A[i:] + B[j:]

if __name__ == "__main__":
    A = list(map(int, input("Enter array A: ").split()))
    B = list(map(int, input("Enter array B: ").split()))
    print(*merge_sorted(A, B))
