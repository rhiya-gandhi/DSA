n = int(input("enter the number of integers in array "))
array = []
print(f"enter {n} numbers: ")

for i in range (n):
    num = int(input("enter the element "))
    array.append(num)
print (f"array is {array}")

largest = float('-inf') #you can also innitialize it to zero but there can be negative numbers as well so have initialized to infinity
second_largest = float('-inf')
smallest = float('inf')
second_smallest = float('inf')

for num in array:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

    if num > smallest:
        second_smallest = smallest
        smallest = num 
    elif num < second_smallest and num != smallest:
        second_smallest = num

    print(f"largest number is {largest}")
    print(f"second largest number is {second_largest}")
    print(f"smallest number is {smallest}")
    print(f"second smallest number is {second_smallest}")


