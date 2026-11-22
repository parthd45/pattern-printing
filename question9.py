# Diamond Star Pattern
n = 5

# Upper Half (Normal Pyramid)
for i in range(1, n+1):  # Loop from 1 to 5
    for j in range(n-i):  # Print decreasing spaces
        print(" ", end=" ")
    for k in range(2*i-1):  # Print increasing stars
        print("*", end=" ")
    print()  # Move to next line

# Lower Half (Inverted Pyramid)
for i in range(n-1, 0, -1):  # Loop from 4 to 1
    for j in range(n-i):  # Print increasing spaces
        print(" ", end=" ")
    for k in range(2*i-1):  # Print decreasing stars
        print("*", end=" ")
    print()  # Move to next line