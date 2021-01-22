limit=int(input("enter limit"))

lst=list()
for i in range(0,limit):
    number=input("enter number")
    lst.append(number)
element=input("enter element you want to search ")
flag=0
cnt=1
for num in lst:
    if(element==num):
        flag+=1
        break
    else:
        pass
    cnt+=1
if flag==0:
    print("element not found")
else:
    print("element found",cnt)