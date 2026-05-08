# Labsheet 26 : LO1
# Disjoint Set Union using Union and Find Operations

# Input number of nodes
n = int(input())

# Input number of operations
m = int(input())

# Parent array
parent = list(range(n + 1))

# Find function with path compression
def find(i):
    if parent[i] == i:
        return i

    parent[i] = find(parent[i])

    return parent[i]

# Union function
def union(i, j):
    root_i = find(i)
    root_j = find(j)

    if root_i != root_j:
        parent[root_j] = root_i

# Perform operations
for _ in range(m):
    parts = input().split()

    if parts[0] == "union":
        union(int(parts[1]), int(parts[2]))

    elif parts[0] == "find":
        print(find(int(parts[1])))


# Labsheet 26 : LO2
# Connectivity Checking using Disjoint Set Union

# Input number of nodes
n = int(input())

# Input number of operations
m = int(input())

# Parent and rank arrays
parent = list(range(n + 1))
rank = [0] * (n + 1)

# Find function with path compression
def find(i):
    if parent[i] == i:
        return i

    parent[i] = find(parent[i])

    return parent[i]

# Union by rank
def union(i, j):
    root_i = find(i)
    root_j = find(j)

    if root_i != root_j:

        if rank[root_i] < rank[root_j]:
            parent[root_i] = root_j

        elif rank[root_i] > rank[root_j]:
            parent[root_j] = root_i

        else:
            parent[root_i] = root_j
            rank[root_j] += 1

# Perform operations
for _ in range(m):
    parts = input().split()

    op = parts[0]
    a = int(parts[1])
    b = int(parts[2])

    if op == "union":
        union(a, b)

    elif op == "check":

        if find(a) == find(b):
            print("Connected")

        else:
            print("Not Connected")
