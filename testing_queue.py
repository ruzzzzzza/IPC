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


def consumer(q, n):
    sum = 0
    while True:
        if q.empty() is False:
            a = q.get()
            if a == -1:
                break
            sum += time.time() - a.timestamp
    print(sum / n)


if __name__ == '__main__':
    q = Queue()
    l = 100 * 1024  # the size of the string in bytes
    n = 1000000  # number of lines
    process_one = Process(target=creator, args=(q, n, l))
    process_two = Process(target=consumer, args=(q, n))

    process_one.start()
    process_two.start()

    q.close()
    q.join_thread()

    process_one.join()
    process_two.join()
