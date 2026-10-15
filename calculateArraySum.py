n=int(input("enter how integers you want "))
a = [] 
print (f"Enter {n} numbers")
for i in range (n):
    element = int(input(f"element {i+1}: "))
    a.append(element) #array madhe elements store honar
total = 0
for num in a:
    total += num
print("total of array is ", total)
    



    