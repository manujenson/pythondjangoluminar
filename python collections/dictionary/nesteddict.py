employee={
    1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
    1001:{"id":1001,"name":"jhon","salary":30000,"exp":2},
    1002:{"id":1002,"name":"dany","salary":35000,"exp":2},
    1003:{"id":1003,"name":"jack","salary":30000,"exp":2},
}

#nested dict
print(employee[1000])
#PRINT NAME OF 1001
if 1001 in employee:
    print(employee[1001]["name"])
else:
    print("employe with id is not exist")

#salary of 1003
if 1003 in employee:
    print(employee[1003]["salary"])


#using kwargs
def print_employee(**kwargs):
    print(kwargs)
    id=kwargs["id"]
    if id in employee:
        print(employee[id]["name"])
    else:
        print("employe with id is not exist")

print_employee(id=1000,prop="salary")

#
def print_employee(**kwargs):

    id=kwargs["id"]
    if id in employee:
        print(employee[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(employee[id][prop])
        else:
            pass
    else:
        print("employe with id is not exist")

print_employee(id=1000,prop="salary")

