import threading
import time

class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()
        self.arg = arg

    def run(self):
        time.sleep(2)
        print("The args for this class is {0}".format(self.arg))

for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()

print("Main thread is done!!!!!!!!!")