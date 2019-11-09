
import threading

sum = 0
loopsum = 1000000

def myAdd():
    global sum,loopsum
    for i in range(1,loopsum):
        sum += 1

def myMinu():
    global sum,loopsum
    for i in range(1,loopsum):
        sum -= 1

if __name__ == '__main__':
    print("Start:",sum)

    add = threading.Thread(target=myAdd)
    minu = threading.Thread(target=myMinu)
    add.start()
    minu.start()

    add.join()
    minu.join()

    print("Done:", sum)

