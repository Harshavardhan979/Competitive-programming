
LABSHEET17


nodes = int(input("Enter number of nodes: "))
edges = int(input("Enter number of edges: "))

adj = [[] for _ in range(nodes)]

for _ in range(edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    adj[u].append(v)
    adj[v].append(u)

start = int(input("Enter start node: "))

bfs_visited = [False] * nodes
queue = [start]
bfs_visited[start] = True
bfs_result = []
head = 0

while head < len(queue):
    curr = queue[head]
    head += 1
    bfs_result.append(curr)
    for neighbor in adj[curr]:
        if not bfs_visited[neighbor]:
            bfs_visited[neighbor] = True
            queue.append(neighbor)

dfs_visited = [False] * nodes
stack = [start]
dfs_result = []

while stack:
    curr = stack.pop()
    if not dfs_visited[curr]:
        dfs_visited[curr] = True
        dfs_result.append(curr)
        for neighbor in adj[curr]:
            if not dfs_visited[neighbor]:
                stack.append(neighbor)

print("BFS Traversal:", bfs_result)
print("DFS Traversal:", dfs_result)
