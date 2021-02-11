class person:

    def setperson(self,age,name):
        self.age=age
        self.name=name

    def printperson(self):
        print("name",self.name)
        print("age",self.age)

obj=person()
obj.setperson(25,"amal")
obj.printperson()