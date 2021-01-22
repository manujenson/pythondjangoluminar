#values stored in dict in the form key value pair
#key must be unique

#adding new key valuepair


expenses={"jan20":30000,"feb20":25000,"march20":28000,"april20":25000,"may20":22000}
print(expenses["march20"])

#chk for june20
print("june20" in expenses)

#add new key
#june2=25000
expenses["june20"]=25000
print(expenses)

#reduce from expense or edit
print("march20" in expenses)
expenses["march20"]-=3000
print(expenses["march20"])

