from threading import *
import time

class myclass:
    def job(self):
        for i in range(10):
            time.sleep(2)
            print("child thread")

obj=myclass()
t=Thread(target=obj.job)
t.start()

for i in range(10):
    time.sleep(2)
    print("main thread")
