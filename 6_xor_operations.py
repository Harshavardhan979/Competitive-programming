



LABSHEET6
n =  int(input("Enter the number of input"))
unique_number = 0
list_num = []
for i in range(0,n):
    a = int(input("enter the list elements"))
    list_num.append(a)
for i in list_num:
    unique_number = unique_number ^ i
print(unique_number)



n =  int(input("Enter the number of packets"))
unique_number = 0
list_num = []
for i in range(0,n):
    a = int(input("enter packet values"))
    list_num.append(a)
check_sum = int(input("Enter the check sum value"))
for i in list_num:
    unique_number = unique_number ^ i
if unique_number == check_sum:
    print("Ok")
else:
    print("ANOMALY")


