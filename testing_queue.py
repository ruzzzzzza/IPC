from multiprocessing import Process, Queue
import time

start_time = time.time()


class pack:

    def __init__(self, payload, timestamp):
        self.payload = payload
        self.timestamp = timestamp


def creator(q, n, l):
    str = ''
    for i in range(l):
        str = str + 'a'
    for i in range(n):
        q.put(pack(str, time.time()))
    q.put(-1)


def consumer(q, k, n):
    s = 0
    sum = 0
    while True:
        if q.empty() is False:
            a = q.get()
            if a == -1:
                s += 1
            else:
                sum += time.time() - a.timestamp
            if s == k:
                break
    print(sum / n)


if __name__ == '__main__':
    q = Queue()
    l = 5 * 1024  # the size of the string in bytes
    n = 1000000  # number of lines
    k = 10  # number of processes
    kk = []
    for i in range(k):
        kk.append(Process(target=creator, args=(q, int(n / k), l)))
    last_process = Process(target=consumer, args=(q, k, n))

    for p in kk:
        p.start()
    last_process.start()

    q.close()
    q.join_thread()

    for p in kk:
        p.join()
    last_process.join()
