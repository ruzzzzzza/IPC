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


def consumer(q):
    while True:
        if q.empty() is False:
            a = q.get()
            if a == -1:
                break


if __name__ == '__main__':
    q = Queue()
    l = 100 * 1024  # the size of the string in bytes
    n = 1000000  # number of lines
    process_one = Process(target=creator, args=(q, n, l))
    process_two = Process(target=consumer, args=(q,))

    process_one.start()
    process_two.start()

    q.close()
    q.join_thread()

    process_one.join()
    process_two.join()

    print(time.time() - start_time)
