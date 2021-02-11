class employee:

    def __init__(self,id,name,desig,salary):  #using constructer  ie init
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary

    def print_employee(self):
        print(self.id,",",self.name,",",self.desig,",",self.salary)

    def __str__(self):
        return self.name


obj=employee(100,"manu","hr manager","35000")
obj.print_employee()
print(obj)

