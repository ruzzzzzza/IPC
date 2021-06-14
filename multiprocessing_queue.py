import time
from multiprocessing import Process, Queue

start_time = time.time()
kolvo = 0
n = 1000
sm = 0


def creator(q):
    global n
    for item in range(n):
        q.put(item)


def consumer(q):
    global kolvo, n, sm
    while True:
        if q.empty() is False:
            a = q.get()
            kolvo += 1
            sm += a
            if kolvo == n:
                break


if __name__ == '__main__':
    q = Queue()
    k = 10
    l = []
    last = Process(target=creator, args=(q,))
    for i in range(k):
        l.append(Process(target=consumer, args=(q,)))
    last.start()
    for p in l:
        p.start()

    q.close()
    q.join_thread()

    last.join()
    for p in l:
        p.join()
    print(sm)
    print(time.time() - start_time)
