# Total number of rows
n = 5
# Outer loop controls rows
for i in range(1, n + 1):
    for j in range(n - i):# Print spaces before stars
        print(" ", end=" ")
    for j in range(2 * i - 1):    # Print odd number of stars 
        print("*", end=" ")
    print()# Move to next row