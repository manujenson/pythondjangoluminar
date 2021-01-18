lst=[1,2,3,5]

num=int(input("enter num to find pairs"))
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]+lst[j]==num):
            print(lst[i],lst[j])
