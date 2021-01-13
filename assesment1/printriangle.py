num=int(input("enter no of row"))
for row in range(1,num)
    for col in range(1,num)
        if (row==num)|(row+col==num)|(col-row==num):
            print("*",end="")
        else:
            print(end=" ")

    print()