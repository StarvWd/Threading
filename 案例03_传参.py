
'''
使用time.seleep,生成两个函数
顺序调用
计算总时间
'''

import _thread as thread
import time

def loop1(in1):
    print("Start loop 1 at:", time.ctime())
    print("我是参数",in1)
    time.sleep(4)

    print("End loop 1 at:", time.ctime())


def loop2(in1,in2):
    print("Start loop 2 at:", time.ctime())
    print("我是参数", in1,in2)
    time.sleep(2)

    print("End loop 2 at:", time.ctime())



def main():
    print("Starting at:", time.ctime())
    thread.start_new_thread(loop1,(12,))
    thread.start_new_thread(loop2,(12,34))
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)