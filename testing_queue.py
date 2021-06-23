from multiprocessing import Process, Queue
import time

start_time = time.time()


def creator(q, n, l, k):
    str = ''
    for i in range(l):
        str = str + 'a'
    for i in range(n):
        q.put(str)
    for i in range(k):
        q.put(-1)


def consumer(q):
    while True:
        if q.empty() is False:
            a = q.get()
            if a == -1:
                break


if __name__ == '__main__':
    q = Queue()
    l = 5 * 1024  # the size of the string in bytes
    n = 1000000  # number of lines
    k = 10  # number of processes
    kk = []
    main_process = Process(target=creator, args=(q, n, l, k))
    for i in range(k):
        kk.append(Process(target=consumer, args=(q,)))

    main_process.start()
    for p in kk:
        p.start()

    q.close()
    q.join_thread()

    main_process.join()
    for p in kk:
        p.join()

    print(time.time() - start_time)
