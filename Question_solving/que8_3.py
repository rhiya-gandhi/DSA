print("\nPattern 3: Diamond outline")
n = 5                                  # widest row is the n-th row
size = 2 * n - 1                       # total rows and total columns (9)
centre = n - 1                         # centre column index (4)
for i in range(size):
    # k = how far the stars are from the centre in this row
    # top half: k grows 0,1,2,3,4  | bottom half: k shrinks 3,2,1,0
    k = i if i < n else size - 1 - i
    left = centre - k                  # column of the left star
    right = centre + k                 # column of the right star
    for j in range(size):
        if j == left or j == right:    # print star only at the two edges
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()