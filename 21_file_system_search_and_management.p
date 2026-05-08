# Labsheet 21 : LO1
# File System Structure and File Search

from collections import defaultdict

# Input number of parent-child relationships
n = int(input())

# Create adjacency list and hash table
adj_list = defaultdict(list)
hash_table = set()

# Input directory structure
for _ in range(n):
    parent, child = input().split()

    adj_list[parent].append(child)

    hash_table.add(parent)
    hash_table.add(child)

# Input file to search
search_query = input().strip()

# Print file system structure
print("File System Structure")

for directory in adj_list:
    children = " ".join(adj_list[directory])
    print(f"{directory} → {children}")

# Search file
if search_query in hash_table:
    print("Search Result: File Found")
else:
    print("Search Result: File Not Found")


# Labsheet 21 : LO2
# File Creation, Deletion and Search Operations

# Input number of commands
n = int(input())

# Create file index
file_index = {}

# Process commands
for _ in range(n):
    command = input().split()

    action = command[0]

    # Create file
    if action == "CREATE":
        directory, filename = command[1], command[2]

        file_index[filename] = directory

        print("File Created")

    # Delete file
    elif action == "DELETE":
        filename = command[1]

        if filename in file_index:
            del file_index[filename]
            print("File Deleted")
        else:
            print("File Not Found")

    # Find file
    elif action == "FIND":
        filename = command[1]

        if filename in file_index:
            print("File Exists")
        else:
            print("File Not Found")
