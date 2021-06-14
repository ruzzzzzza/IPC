import time
from multiprocessing import Process, Queue

start_time = time.time()


def creator(q, n, k):
    for item in range(n):
        q.put(item)
    for item in range(k):
        q.put(-1)


def consumer(q, q1):
    plus = 0
    while True:
        if q.empty() is False:
            a = q.get()
            if a == -1:
                break
            plus += a
    q1.put(plus)


if __name__ == '__main__':
    q = Queue()
    q1 = Queue()
    n = 10000
    k = 10
    l = []
    last = Process(target=creator, args=(q, n, k))
    for i in range(k):
        l.append(Process(target=consumer, args=(q, q1)))
    last.start()
    for p in l:
        p.start()

    q.close()
    q.join_thread()

    last.join()
    for p in l:
        p.join()
    sm = 0
    for i in range(k):
        sm += q1.get()
    print(sm)
    print(time.time() - start_time)
