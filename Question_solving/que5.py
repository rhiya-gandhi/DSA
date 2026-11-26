n= int(input("enter how many number in array"))
array = []
for i in range (n):
    num = int(input("enter the elements in the array"))
    array.append(num)
print(f"array is {array}")
reverse_array = array[::-1]
print(f"reversed array is {reverse_array}")
