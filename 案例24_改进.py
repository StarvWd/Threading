import multiprocessing
from time import ctime

def consumer(input_q):
    print ("Into consumer:", ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q")
    print ("Out of consumer:", ctime())

def producer(sequence, output_q):
    print("Into procuder:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("Out of procuder:", ctime())

if __name__ == '__main__':
    q = multiprocessing.Queue()
    cons_p1 = multiprocessing.Process (target = consumer, args = (q,))
    cons_p1.start()

    cons_p2 = multiprocessing.Process (target = consumer, args = (q,))
    cons_p2.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    q.put(None)
    q.put(None)

    cons_p1.join()
    cons_p2.join()


'''
put 1 into q
put 2 into q
put 3 into q
put 4 into q
Out of procuder: Sun Dec  2 11:56:12 2018
Into consumer: Sun Dec  2 11:56:12 2018
pull 1 out of q
pull 2 out of q
pull 3 out of q
pull 4 out of q
Out of consumer: Sun Dec  2 11:56:12 2018
Into consumer: Sun Dec  2 11:56:15 2018
Out of consumer: Sun Dec  2 11:56:15 2018
'''