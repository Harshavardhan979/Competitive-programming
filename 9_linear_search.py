

LABSHEET9

n = int(input("Enter the number of marks")) 
arr = []
for i in range(0,n):
    a = int(input("Enter number of marks"))
    arr.append(a)
x = int(input("enter the element which you want to search"))
for i in range(0,len(arr)):
    if arr[i] == x:
        print(f"element found at {i} index")
        break
    elif i != len(arr)-1:
        continue
    else:
        print("element not found")


n = int(input("Enter the number of marks")) 
arr = []
for i in range(0,n):
    a = int(input("Enter number of marks"))
    arr.append(a)
x = int(input("enter the element which you want to search"))
k = int(input("enter the entries"))
for i in range(0,len(arr)+1):
    if arr[i] == x:
        if i <= k:
            print("valid access")
        else:
            print("late acces")
        break
    elif i != len(arr)-1:
        continue
    else:
        print("access id not found")
