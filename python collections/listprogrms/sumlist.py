lst=[2,5,6,7]

out=list()
tot=sum(lst)

for num in lst:
    out.append(tot-num)
print(out)