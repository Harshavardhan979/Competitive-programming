
LABSHEET8

n = int(input("Enter the number of marks")) 
arr = []
for i in range(0,n):
    a = int(input("Enter number of marks"))
    arr.append(a)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            middle.append(i)
        else:
            right.append(i)
            

    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort(arr))
