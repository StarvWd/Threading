
'''
使用time.seleep,生成两个函数
顺序调用
计算总时间
'''

import threading
import time

def loop1():
    print("Start loop 1 at:", time.ctime())

    time.sleep(4)

    print("End loop 1 at:", time.ctime())


def loop2():
    print("Start loop 2 at:", time.ctime())

    time.sleep(2)

    print("End loop 2 at:", time.ctime())



def main():
    print("Starting at:", time.ctime())
    loop1()
    loop2()
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()