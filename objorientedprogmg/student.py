class students:
    def __init__(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total

obj=students(100,"aksay","django",140)
obj1=students(101,"akil","mean",140)
obj2=students(102,"akil","django",150)

slist=[]
slist.append(obj)
slist.append(obj1)
slist.append(obj2)
total=0
for stud in slist:
    if stud.course=="django":
        total+=stud.total
print(total)