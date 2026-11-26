n = int(input("enter how many integers you want "))
array = []
print(f"enter {n} numbers: ")
for i in range (n):
    num = int(input("enter the elements "))
    array.append(num)
unique = []
for num in array:
    if num not in unique:
        unique.append(num)
print(f"original array is {array}")
print(f"unique elemets array is {unique}")