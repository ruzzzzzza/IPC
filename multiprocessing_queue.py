from multiprocessing import Process, Queue
import time

start_time = time.time()


def creator(q, n):
    for item in range(n):
        q.put(item)


def consumer(q):
    plus = 0
    while q.empty() is False:
        a = q.get()
        plus += a
    print(plus)


if __name__ == '__main__':
    q = Queue()
    n = 10
    process_one = Process(target=creator, args=(q, n))
    process_two = Process(target=consumer, args=(q,))

    process_one.start()
    process_two.start()

    q.close()
    q.join_thread()

    process_one.join()
    process_two.join()
