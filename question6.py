#Right-Aligned Triangle pattern
n=5
for i in range(1,n+1):#outer loop till 1 to 5 
    for j in range(n - i):
        print(" ", end=" ")#printing space
    for j in range(i):
        print("*",end=" ")#print star
    print()