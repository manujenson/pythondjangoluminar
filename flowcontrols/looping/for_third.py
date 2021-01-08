#prime or not

num=int(input("entr no"))
flg=0
if num==1:
    print("not prime")
else:
    for i in range(2,num):

        if(num%i==0):
            flg=flg+1
            break

        else:
            flg=0

    if flg==0:
        print("prime")
    else:
        print("not prime")