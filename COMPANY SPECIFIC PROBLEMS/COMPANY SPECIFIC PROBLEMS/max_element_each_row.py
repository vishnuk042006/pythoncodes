# Q19. Maximum Element in Each Row of Matrix
def row_max(matrix):
    return [max(row) for row in matrix]

if __name__ == "__main__":
    M, N = map(int, input("Enter M and N: ").split())
    matrix = [list(map(int, input().split())) for _ in range(M)]
    for m in row_max(matrix):
        print(m)
