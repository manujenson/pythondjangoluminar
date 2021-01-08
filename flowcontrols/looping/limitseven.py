#read lower and upper limit
#print all even no in this limit

lowlimit=int(input("entr limit"))
upperlimit=int(input("entr limit"))

while(lowlimit<=upperlimit):
    if(lowlimit %2==0):
        print(lowlimit)
    lowlimit+=1
