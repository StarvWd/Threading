import time
import threading

def fun():
    print("Start Fun")
    time.sleep(2)
    print("End Fun")

print("Main thread")

t1 = threading.Thread(target=fun, args=())
t1.start()

time.sleep(1)

print("Main thread end")
print(t1.isAlive())