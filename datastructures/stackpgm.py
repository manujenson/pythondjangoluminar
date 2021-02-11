total=150
def change():
    global total
    total=140
    total+=25
    print(total)

change()
print(total)

#
size=int(input("enter size of stack"))
top=-1
stk=[]
n=1
def push():
    item=int(input("enter item"))
    global top


    if (top<size):

        stk.insert(top,item)
        top += 1
    else:
        print(top)
        print("stk overflow")

def pop():
    global top
    top-=1
    if top<0:
        print("stack is empty")
    else:

        print(stk[top],"item poped out")


def display():
    for i in range(0,top):
        print(stk[i])
while(n!=0):
    option=int(input("enter operation press 1:push 2:pop 3:display"))
    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        display()

    n=int(input("press 0for exit"))




