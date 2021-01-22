employe={"id":100,"ename":"ajay","exp":2,"salary":35000}

if("salary" in employe):
    print(employe["salary"])

#employe name print
print(employe["ename"])

#gender
if("gender" in employe):
    print("exit")
else:
    employe["gender"]="male"
print(employe)

#if employe salary<35000 &5000 or more
if(employe["salary"]<=35000):
    employe["salary"]+=5000
print(employe)
