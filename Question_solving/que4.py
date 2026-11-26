n= int(input("enter how many number array"))
array = []
for i in range (n):
    num = int(input("enter the element ")) 
    array.append(num)

print ("enter the element you want to search")
search_element = int(input())
found = False

for j in array:
    if j == search_element:
        print(f"your element is {j}")
        print(f"the index number of that element is {array.index(j)}")
        found = True
        
if found == False:
    print(f"your element {search_element} is not found in the array")
   
