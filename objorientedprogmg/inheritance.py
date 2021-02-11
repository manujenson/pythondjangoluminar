#single inheritance

class parent:
    def phone(self):
        print("i have iphone 12 pro")


class child(parent):
    pass

c=child()
c.phone()

#multilvl inheritance
class parent:
    def m1(self):
        print("inside parent")

    def ne_meth(self):
        print("hello")

class child(parent):
    def m2(self):
        print("inside the child")

class subchild(child):
    def m3(self):
        print("inside sub child")

obj=subchild()
obj.m3()
obj.m2()
obj.m1()
obj.ne_meth()

#multiple inhertnce
class parent:
    def m1(self):
        print("inside parent")


class child:
    def m1(self):
        print("inside the child")

class subchild(child,parent):   #1st one is child with m1 works
    def m3(self):
        print("inside sub child")

obj=subchild()
obj.m3()
obj.m1()

