num=int(input("entr num"))
res=0
while(num>0):
    digit=num%10
    res=res*10+digit
    num=num//10

print("res=",res)