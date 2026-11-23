# Butterfly Star Pattern
n = 5

# Upper Half
for i in range(1, n+1):  # Loop from 1 to 5
    for j in range(i):  # Print increasing stars
        print("*", end=" ")
    for j in range(2*(n-i)):  # Print decreasing spaces
        print(" ", end=" ")
    for k in range(i):  # Print increasing stars
        print("*", end=" ")
    print()  # Move to next line

# Lower Half
for i in range(n-1, 0, -1):  # Loop from 4 to 1
    for j in range(i):  # Print decreasing stars
        print("*", end=" ")
    for j in range(2*(n-i)):  # Print increasing spaces
        print(" ", end=" ")
    for k in range(i):  # Print decreasing stars
        print("*", end=" ")
    print()