
import threading

sum = 0
loopsum = 1000000

#声明锁
lock = threading.Lock()

def myAdd():
    global sum,loopsum
    for i in range(1,loopsum):
        # 上锁，申请锁
        lock.acquire()
        sum += 1
        # 解锁
        lock.release()

def myMinu():
    global sum,loopsum
    for i in range(1,loopsum):
        lock.acquire()
        sum -= 1
        lock.release()

if __name__ == '__main__':
    print("Start:",sum)

    add = threading.Thread(target=myAdd)
    minu = threading.Thread(target=myMinu)
    add.start()
    minu.start()

    add.join()
    minu.join()
    print("Done:", sum)