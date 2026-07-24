# num=1

# for i in range(10):
#     for j in range(i+1):
#         print(num,end=" ")
#         num+=1
#     print()                #Floyd's Triangle

for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end="")                     #Hollow Square Patter
        else:
            print(" ",end="")              
    print()
