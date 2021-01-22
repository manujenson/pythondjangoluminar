lst=[[10,20],[21,22],[51,52],[53,54,55,56]]

numlist=[]
for sublist in lst:

    for num in sublist:
        numlist.append(num)
print(numlist)