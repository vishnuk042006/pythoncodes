# Q16. Pascal's Triangle Row
def pascal_row(N):
    row = [1]
    for k in range(1, N):
        row.append(row[-1] * (N - k) // k)
    return row

if __name__ == "__main__":
    N = int(input("Enter row number N: "))
    print(*pascal_row(N))
