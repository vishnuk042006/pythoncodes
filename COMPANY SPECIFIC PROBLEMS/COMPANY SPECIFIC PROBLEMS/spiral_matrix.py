# Q21. Spiral Matrix Traversal
def spiral_order(mat):
    if not mat:
        return []
    M, N = len(mat), len(mat[0])
    res = []
    t, b, l, r = 0, M - 1, 0, N - 1
    while t <= b and l <= r:
        for i in range(l, r + 1):
            res.append(mat[t][i])
        t += 1
        for i in range(t, b + 1):
            res.append(mat[i][r])
        r -= 1
        if t <= b:
            for i in range(r, l - 1, -1):
                res.append(mat[b][i])
            b -= 1
        if l <= r:
            for i in range(b, t - 1, -1):
                res.append(mat[i][l])
            l += 1
    return res

if __name__ == "__main__":
    M, N = map(int, input("Enter M and N: ").split())
    mat = [list(map(int, input().split())) for _ in range(M)]
    print(*spiral_order(mat))
