import multiprocessing
from time import ctime

# 设置哨兵问题
def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q")
    print ("Out of consumer:", ctime()) ## 此句执行完成，再转入主进程


def producer(sequence, output_q):
    print ("Into procuder:", ctime())
    for item in sequence:
        output_q.put(item)
        print ("put", item, "into q")
    print ("Out of procuder:", ctime())

if __name__ == '__main__':
    q = multiprocessing.Queue()
    cons_p = multiprocessing.Process(target = consumer, args = (q,))
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    q.put(None)
    cons_p.join()

'''
Into procuder: Sun Dec  2 11:53:50 2018
put 1 into q
put 2 into q
put 3 into q
put 4 into q
Out of procuder: Sun Dec  2 11:53:50 2018
Into consumer: Sun Dec  2 11:53:53 2018
pull 1 out of q
pull 2 out of q
pull 3 out of q
pull 4 out of q
Out of consumer: Sun Dec  2 11:53:53 2018
'''