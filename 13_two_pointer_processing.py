
LABSHEET13

n = int(input("enter number of elements"))
nums = []
res = []
left=0 
right = n - 1
for i in range(0,n):
    a = int(input("enter the elements"))
    nums.append(a)
while left <= right:
    res.append(nums[left])
    res.append(nums[right])
    left = left +1
    right = right -1
print(res)
    


n = int(input("enter number of elements"))
lengths = []
speeds = []
left=0 
right = n - 1
res = []
for i in range(0,n):
    a = int(input("enter the elements"))
    lengths.append(a)
for i in range(0,n):
    b = int(input("enter the elements"))
    speeds.append(b)

while left <= right:
    res.append(lengths[left]/speeds[left])
    res.append(lengths[right]/speeds[right])
    left = left +1
    right = right -1
min_speed = res[0]
for i in res:
    if i < min_speed:
        min_speed = i
print(min_speed)
    



