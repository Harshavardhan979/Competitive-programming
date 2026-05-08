# Labsheet 17 : LO1
# BFS and DFS Traversal in Graph

from collections import defaultdict, deque

# Input number of nodes and edges
n, e = map(int, input().split())

# Create graph
graph = defaultdict(list)

# Input edges
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Input starting node for traversal
start_node = int(input())

# BFS Traversal Function
def bfs(start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

# DFS Traversal Function
def dfs(start):
    visited = set()
    order = []

    def traverse(node):
        visited.add(node)
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                traverse(neighbor)

    traverse(start)
    return order

# Print BFS and DFS Traversal
print("BFS Traversal:", *(bfs(start_node)))
print("DFS Traversal:", *(dfs(start_node)))




# Labsheet 17 : LO2
# Check Path Existence in Graph using DFS

# Input source and destination
source, destination = map(int, input().split())

visited = set()

# Function to check path existence
def has_path(node):
    if node == destination:
        return True

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_path(neighbor):
                return True

    return False

# Print result
if has_path(source):
    print("Path Exists")
else:
    print("No Path Exists")
