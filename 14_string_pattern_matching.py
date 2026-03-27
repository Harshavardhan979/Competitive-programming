

LABSHEET14



str1 = input("enter the string")
str2 = input("enter the pattern to match")
if str2 in str1:
    print("pattern found")
else:
    print("pattern not found")
    



str1 = input("Enter the string: ")
str2 = input("Enter the pattern to match: ")

n = len(str1)
m = len(str2)

count = 0

for i in range(0, n - m + 1):   
    j = 0
    while j < m and str1[i + j] == str2[j]:
        j += 1
    
    if j == m:  
        count += 1

print(count)

