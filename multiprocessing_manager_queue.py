from multiprocessing import Process, Queue, Manager
import time

start_time = time.time()


def creator(q, n, start, step):
    for item in range(start, n, step):
        q.put(item)


def consumer(q, n):
    plus = 0
    k = 0
    while True:
        if q.empty() is False:
            a = q.get()
            plus += a
            k += 1
            if k == n:
                break
    print(plus)


if __name__ == '__main__':
    q = Manager().Queue()
    n = 10000
    k = 10  # number of processes
    l = []
    for i in range(k):
        l.append(Process(target=creator, args=(q, n, i, k)))
    last = Process(target=consumer, args=(q, n))
    for p in l:
        p.start()
    last.start()

    for p in l:
        p.join()
    last.join()

    print(time.time() - start_time)
