import time
import threading

def fun():
    print("Start Fun")
    time.sleep(1)
    print("End Fun")

def bar():
    print("Start Bar")
    time.sleep(3)
    print("End Bar")

print("Main thread")

t1 = threading.Thread(target=fun, args=())
t2 = threading.Thread(target=bar, args=())
#守护线程，在start之前设置
t2.setDaemon(True)
t1.start()
t2.start()

#time.sleep(1)

print("Main thread end")
print(t1.is_alive())
print(t2.is_alive())