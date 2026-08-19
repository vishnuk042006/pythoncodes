# Q8. Diamond Star Pattern
def diamond(N):
    lines = []
    for i in range(1, N + 1, 2):
        lines.append(" " * ((N - i) // 2) + "*" * i)
    for i in range(N - 2, 0, -2):
        lines.append(" " * ((N - i) // 2) + "*" * i)
    return "\n".join(lines)

if __name__ == "__main__":
    N = int(input("Enter odd N: "))
    print(diamond(N))
