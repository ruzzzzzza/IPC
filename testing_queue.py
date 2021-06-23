from multiprocessing import Process, Queue
import time

start_time = time.time()


def creator(q, n, l):
    str = ''
    for i in range(l):
        str = str + 'a'
    for i in range(n):
        q.put(str)
    q.put(-1)


def consumer(q, k):
    s = 0
    while True:
        if q.empty() is False:
            a = q.get()
            if a == -1:
                s += 1
            if s == k:
                break


if __name__ == '__main__':
    q = Queue()
    l = 5 * 1024  # the size of the string in bytes
    n = 1000000  # number of lines
    k = 10  # number of processes
    kk = []
    for i in range(k):
        kk.append(Process(target=creator, args=(q, int(n / k), l)))
    last_process = Process(target=consumer, args=(q, k))

    for p in kk:
        p.start()
    last_process.start()

    q.close()
    q.join_thread()

    for p in kk:
        p.join()
    last_process.join()

    print(time.time() - start_time)
