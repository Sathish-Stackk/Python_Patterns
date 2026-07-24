for i in range(5):
    for j in range(6):           
        print("*",end=" ")      # square pattern
    print()

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")      # Right triangle
    print()


for i in range(5):
    for j in range(5-i):
        print("*",end=" ")      # inverted pattern
    print()


for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")    # Number Triangle
    print()


for i in range(5):
    for j in range(5-i):
        print(5-j,end=" ")     #Inverted num
    print() 

for i in range(5):
    for j in range(i+1):
        print(i+1,end=" ")      # Repeated num Traingle
    print()

for i in range(5):
    for j in range(i+1):
        print(chr(65+j),end="")     #Alphabet triangle #ascii values
    print()

