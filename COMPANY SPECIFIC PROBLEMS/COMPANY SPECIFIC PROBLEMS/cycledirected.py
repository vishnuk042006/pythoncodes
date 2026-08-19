# LC5. Detect Cycle in Directed Graph
def has_cycle(V, edges):
    g = [[] for _ in range(V)]
    for u, v in edges:
        g[u].append(v)
    color = [0] * V  # 0=white, 1=gray, 2=black

    def dfs(u):
        color[u] = 1
        for v in g[u]:
            if color[v] == 1:
                return True
            if color[v] == 0 and dfs(v):
                return True
        color[u] = 2
        return False

    return any(dfs(i) for i in range(V) if color[i] == 0)

if __name__ == "__main__":
    V, E = map(int, input("Enter V and E: ").split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]
    print(has_cycle(V, edges))
