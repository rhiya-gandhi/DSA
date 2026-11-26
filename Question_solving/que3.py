n=int(input("enter how many elements of array"))
array =[]
for i in range (n):
    num = int(input("enter the element"))
    array.append(num)
print (f"array is {array}")
even = 0
odd = 0 
for num in array:
    if num % 2 ==0:
        even += 1
    else:
        odd += 1
print (f"even numbers count {even}")
print (f"odd numbers count {odd}")
