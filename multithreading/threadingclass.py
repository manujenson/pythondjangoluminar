from threading import *


class mythread(Thread):
    def run(self):
        for i in range(10):

            print("inside thread class")

obj=mythread()
obj.start()

for i in range(10):

    print("main thread class")