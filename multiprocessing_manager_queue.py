from multiprocessing import Process, Manager
import time

start_time = time.time()


def creator(q, n):
    for item in range(n):
        q.put(item)


def consumer(q, n):
    plus = 0
    while True:
        if q.empty() is False:
            a = q.get()
            plus += a
            if a == n - 1:
                break
    print(plus)


if __name__ == '__main__':
    m = Manager()
    q = m.Queue()
    n = 10000
    process_one = Process(target=creator, args=(q, n))
    process_two = Process(target=consumer, args=(q, n))

    process_one.start()
    process_two.start()

    process_one.join()
    process_two.join()

    print(time.time() - start_time)
