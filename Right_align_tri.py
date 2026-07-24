for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")      #right aligned star triangle
    for k in range(i+1):
        print("*",end="")
    print()

for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")          #  pyramid
    for k in range(2*i+1):
        print("*",end="")
    print()