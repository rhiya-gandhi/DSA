n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# n = int(input("Enter size: "))
# mid = n // 2
# for i in range(n):
#     for j in range(n):
#         if i == mid or j == mid:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()   