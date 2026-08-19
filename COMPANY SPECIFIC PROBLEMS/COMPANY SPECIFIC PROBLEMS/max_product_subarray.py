# Q29. Maximum Product Subarray
def max_product_subarray(A):
    max_p = min_p = res = A[0]
    for x in A[1:]:
        candidates = (x, max_p * x, min_p * x)
        max_p, min_p = max(candidates), min(candidates)
        res = max(res, max_p)
    return res

if __name__ == "__main__":
    N = int(input("Enter N: "))
    A = list(map(int, input("Enter array: ").split()))
    print(max_product_subarray(A))
