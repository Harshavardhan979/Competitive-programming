
LABSHEET12

n = int(input("enter the number of elements"))
lis = []
for i in range(0,n):
    a = int(input("enter the elements"))
    lis.append(a)
min_ele = lis[0]
for i in lis:
    if i < min_ele:
        min_ele = i
print(f"minimum element is { min_ele}")



n = int(input("enter the number of cars"))
lis = []
for i in range(0,n):
    a = int(input("enter the speeds of cars"))
    lis.append(a)
distance = int(input("enter the distance to be covered"))
min_ele = lis[0]
for i in lis:
    if i < min_ele:
        min_ele = i
max_time = distance/min_ele
print(f"minimum speed is { min_ele}")
print(f"maximum time  is { max_time}")
