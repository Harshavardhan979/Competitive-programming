
LABSHEET7

n = int(input("Enter the number of values"))
N = []
for i in range(0,n):
    a = int(input("Enter the values"))
    N.append(a)
print(N)


n = int(input("Enter the number of values"))
N = []
for i in range(0,n):
    a = int(input("Enter the values"))
    N.append(a)
for i in range(0,n):
    for j in range(i+1,n):
       if N[j] < N[i]:
           temp = N[i]
           N[i] = N[j]
           N[j] = temp
                      
print(N[2])
