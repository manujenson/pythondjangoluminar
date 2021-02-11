num1=[5,4,6,2,5,9]
num2=[1,2,3,4,9]
common=list(filter(lambda n:n in num2,num1))
print(common)