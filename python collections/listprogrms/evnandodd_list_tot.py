#even no to even list
#odd to odd list
#find total of even and odd list

lst=[10,11,12,13,14,15,16,17]
evenlist=list()
oddlist=list()
for num in lst:
    if num%2==0:
        evenlist.append(num)

    else:
        oddlist.append(num)

print(oddlist)
print(evenlist)
print("oddsum",sum(oddlist))
print("even",sum(evenlist))

total=sum(lst)