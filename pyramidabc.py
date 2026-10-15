# n = int(input("enter no. of rows: "))
# for i in range (n):
#     print('  ' *(n-i-1), end=" ")  # print spaces before the stars
#     for j in range (2*i+1):
#         print(chr(65+j), end=" ")
#     print()
#        A
#      A B C
#    A B C D E
#  A B C D E F G 

n = int(input("enter no. of rows: "))
for i in range (n):
    print('  ' *(n-i+1), end=" ")  # print spaces before the stars
    for j in range (2*i+1):
        if (j==0 or j==2*i or i==n-1):
            print(chr(65+j), end=" ")
        else:
            print(" ", end=" ")
    print()