#Right-Angled Triangle pattern
for i in range(1,6):# Outer loop controls the number of rows (1 to 5)
    for j in range(i):# Inner loop prints stars according to the current row number
        print("*",end=" ")# Print star followed by one space
        # end=" " keeps stars on the same line
    print()