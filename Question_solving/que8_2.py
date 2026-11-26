# Logic: star only on the border: first row, last row,
# first column or last column. The inside stays blank.
print("\nPattern 2: Hollow square")
n = 5
for i in range(n):
    for j in range(n):
        # i == 0 / i == n-1 -> top and bottom edges
        # j == 0 / j == n-1 -> left and right edges
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    #i = 0 is the first row and i = n-1 is the last row 
    #likewise to the j for colomn 
    #so only there * will be printed baki it will be space 