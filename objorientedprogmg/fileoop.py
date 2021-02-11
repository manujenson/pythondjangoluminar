
class employee:

    def __init__(self,id,name,desig,exp,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary

    def __str__(self):
        return self.name

f=open("employe.txt","r")
emplist=[]
salist=[]
desiglist=[]
for lines in f:
    id,name,desig,exp,salary=lines.rstrip("\n").split(",")
    emplist.append(employee(id,name,desig,exp,salary))

#name of emp
for employee in emplist:
    print(employee)

#higst sal
for employee in emplist:
    salist.append(employee.salary)
print(max(salist))

#desg develp whose lowst sal

#print employee details whose desig developer
devop=list(filter(lambda emp:emp.desig=="developer",emplist))
for emp in devop:
    print(emp)

#no of employe as developr
cnt=len(list(filter(lambda emp:emp.desig=="developer",emplist)))
print(cnt)

#print employe detail who have higst salry
maxsal=max(list(map(lambda emp:emp.salary,emplist)))
print(maxsal)