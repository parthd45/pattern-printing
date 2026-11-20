#Inverted Right Angle Triangle
for i in range(5,0,-1):# Outer loop controls rows (5 to 1)
    for j in range(i): # Inner loop prints stars according to current row number
        print("*",end=" ")# Print star followed by one space
        # end=" " keeps stars on the same line
    print()