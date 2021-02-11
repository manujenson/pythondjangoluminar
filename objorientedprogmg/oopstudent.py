class student:

    def __init__(self,rol,course,name):
        self.rol=rol
        self.course=course
        self.name=name

    def get_student(self):
        print(self.rol,",",self.course,",",self.name)


obj=student(100,"django","amal")
obj.get_student()

