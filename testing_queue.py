from multiprocessing import Process, Queue
import time

start_time = time.time()


class pack:

    def __init__(self, payload, timestamp):
        self.payload = payload
        self.timestamp = timestamp


def creator(q, n, l, k):
    str = ''
    for i in range(l):
        str = str + 'a'
    for i in range(n):
        q.put(pack(str, time.time()))
    for i in range(k):
        q.put(-1)


def consumer(q, q1):
    sum = 0
    while True:
        if q.empty() is False:
            a = q.get()
            if a == -1:
                break
            sum += time.time() - a.timestamp
    q1.put(sum)


if __name__ == '__main__':
    q = Queue()
    q1 = Queue()
    l = 5 * 1024  # the size of the string in bytes
    n = 1000000  # number of lines
    k = 10  # number of processes
    kk = []
    main_process = Process(target=creator, args=(q, n, l, k))
    for i in range(k):
        kk.append(Process(target=consumer, args=(q, q1)))

    main_process.start()
    for p in kk:
        p.start()

    sum = 0
    for i in range(k):
        sum += q1.get()

    q.close()
    q.join_thread()
    q1.close()
    q1.join_thread()

    main_process.join()
    for p in kk:
        p.join()

    print(sum / n)
