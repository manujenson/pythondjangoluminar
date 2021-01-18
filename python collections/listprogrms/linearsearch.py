lst=[2,5,6,7]

out=list()
tot=sum(lst)

for num in lst:
    out.append(tot-num)
element=int(input("enter element "))
flag=0
cnt=0
for num in lst:
    if(element==num):
        flag+=1
        break
    else:
        pass
    cnt+=1
if flag==0:
    print("not found")
else:
    print("found")