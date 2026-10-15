n = int(input("enter the number of elements in array"))
array =[]
for i in range (n):
    num = int(input("enter the elements"))
    array.append(num)
print(f"thr arrray is {array}")
newarray = []

for num in array:
    if num != 0:
        newarray.append(num)
for num in array:
    if num == 0:
        newarray.append(num)
print(f"the new array with arranged numbers{newarray}")