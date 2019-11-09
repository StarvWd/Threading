

'''
rst = lock.acquire(timeout=4)
rst真表示申请成功
'''


import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()


def func_1():
    print("func_1 starting..........")
    lock_1.acquire(timeout=4)
    print("func_1申请了 lock_1....")
    time.sleep(2)

    print("func_1等待 lock_2....")
    rst = lock_2.acquire(timeout=2)
    if rst:
        print("func_1申请了 lock_2....")
        lock_2.release()
        print("func_1释放了 lock_2....")
    else:
        print("func_1没有申请到 lock_2....")
    lock_1.release()
    print("func_1释放了 lock_1....")

    print("func_1 done.....")


def func_2():
    print("func_2 starting..........")
    lock_2.acquire()
    print("func_2申请 lock_2....")
    time.sleep(4)

    print("func_2等待 lock_1....")
    lock_1.acquire()
    print("func_2申请 lock_1....")

    lock_1.release()
    print("func_2释放了 lock_1.....")
    lock_2.release()
    print("func_2释放了 lock_2....")

    print("func_1 done.....")

if __name__ == '__main__':
    print("主程序启动。。。。。")
    t1 = threading.Thread(target=func_1)
    t2 = threading.Thread(target=func_2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主程序结束。。。。。")