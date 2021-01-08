num1=int(input("entr no1"))
num2=int(input("entr no2"))
num3=int(input("entr no3"))

if(num1 > num2)&(num1 > num3):
    print("num1 is highest")
elif(num2>num1)&(num2>num3):
    print("no2 is highest")
elif(num3 > num1)&(num3 > num2):
    print("no3 is highest")
elif (num1 == num2)&(num1 == num3):
    print("3 numbers are equal")