# #alphabet pattern
# n= int(input("enter no. of rows: "))
# for i in range (n):
#     for j in range (i+1):
#         print(chr(65+j), end=" ") 
#     print()
#i is same for every value of j 
# A
# A B
# A B C
# A B C D
# A B C D E 
    
#alphabet pattern 2nd
n= int(input("enter no. of rows: "))
num = 0
for i in range (n):
    for j in range (i+1):
        print(chr(65+num), end=" ")  # num will be incremented by 1 after every row
        num +=1
    print()