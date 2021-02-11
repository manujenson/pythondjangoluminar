#adding num

add=lambda num1,num2: num1+num2
print(add(10,20))

#sub

sub=lambda num1,num2: num1-num2
print(sub(50,20))

#cube of a num
cube=lambda num:num**3
print(cube(2))

#even no
even=lambda num:num%2==0
print(even(11))


#map(), filter(), reduce(),
lst=[1,2,3,4,5,6]
#squre
sqlist=list(map(lambda num:num**2,lst))
print(sqlist)

#
numlist=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst))
print(numlist)

#even
evens=list(filter(lambda num:num%2!=0,lst))
print(evens)

#upper
names=["india","pak","sa","aus"]
upplist=list(map(lambda name:name.upper(),names))
print(upplist)

#find starting wit a
acountry=list(filter(lambda name:name[0]=="a",names))
print(acountry)

#reduce
from functools import reduce

lst=[2,4,6,8]
sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)

#
lst=[10,11,12]
high=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(high)

#
low=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(low)

#