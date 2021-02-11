#print_data(rol=1000) print name of std(rol=1000)
#print_data(rol=1001,prop="course") name,course

f=open("students","r")

students={}

for lines in f:
    id,name,total,course=lines.rstrip("\n").split(",")


    if id not in students:
        students[id]={"id":id,"name":name,"total":total,"course":course}


def print_student_data(**kwars):
    id=kwars["id"]
    if id in students:
        print(students[id]["name"])
        if "prop" in kwars:
            prop=kwars["prop"]
            print(students[id][prop])
    else:
        print("no std exist with this id")

print_student_data(id="1002",prop="total")

