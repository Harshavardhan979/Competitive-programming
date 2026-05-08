# Labsheet 20 : LO1
# Preorder Traversal in Binary Tree

# Input number of nodes
n = int(input())

# Create tree dictionary
tree = {}
root = None

# Input tree nodes
for i in range(n):
    node, left, right = map(int, input().split())

    tree[node] = (left, right)

    if i == 0:
        root = node

# Preorder Traversal Function
def preorder_traversal(current_node):
    if current_node == -1:
        return

    print(current_node, end=" ")

    left_child, right_child = tree[current_node]

    preorder_traversal(left_child)
    preorder_traversal(right_child)

# Print preorder traversal
print("File System Traversal (Preorder)")
preorder_traversal(root)
print()


# Labsheet 20 : LO2
# Preorder, Inorder and Postorder Traversals

# Input number of nodes
n = int(input())

# Create tree dictionary
tree = {}
root = None

# Input tree nodes
for i in range(n):
    node, left, right = map(int, input().split())

    tree[node] = (left, right)

    if i == 0:
        root = node

# Preorder Traversal
def preorder(node):
    if node == -1:
        return []

    left, right = tree[node]

    return [node] + preorder(left) + preorder(right)

# Inorder Traversal
def inorder(node):
    if node == -1:
        return []

    left, right = tree[node]

    return inorder(left) + [node] + inorder(right)

# Postorder Traversal
def postorder(node):
    if node == -1:
        return []

    left, right = tree[node]

    return postorder(left) + postorder(right) + [node]

# Print traversals
print("Preorder Traversal", *preorder(root))
print("Inorder Traversal", *inorder(root))
print("Postorder Traversal", *postorder(root))
