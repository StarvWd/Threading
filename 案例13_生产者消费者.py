
import time
import threading
import queue

#生产者
class Producer(threading.Thread):
    def run(self):
        global q
        count = 0
        while True:
            if q.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = '生成产品'+str(count)
                    q.put(msg)
                    print(msg)
            time.sleep(0.5)

#消费者
class Consumer(threading.Thread):
    def run(self):
        global q
        while True:
            if q.qsize() > 100:
                for i in range(3):
                    msg = self.name+'消费产品'+q.get()
                    print(msg)
            time.sleep(1)



if __name__ == '__main__':

    q = queue.Queue()

    #初始产品
    for i in range(500):
        q.put('初始产品'+str(i))
    #两个生产者
    for i in range(2):
        p = Producer()
        p.start()
    #五个消费者
    for i in range(5):
        c = Consumer()
        c.start()