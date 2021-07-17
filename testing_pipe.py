from multiprocessing import Process, Pipe
import time

start_time = time.time()


def creator(q, n, l):
    str = ''
    for i in range(l):
        str = str + 'a'
    for i in range(n):
        q.send(str)
    q.send(-1)


def consumer(q):
    while True:
        if q.poll() is True:
            a = q.recv()
            if a == -1:
                break


if __name__ == '__main__':
    q1, q2 = Pipe()
    l = 200  # the size of the string in bytes
    n = 1000000  # number of lines
    process_one = Process(target=creator, args=(q1, n, l))
    process_two = Process(target=consumer, args=(q2,))

    process_one.start()
    process_two.start()

    q1.close()
    q2.close()

    process_one.join()
    process_two.join()

    print(time.time() - start_time)
