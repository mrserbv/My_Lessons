
# Пример взаимной блокировки

from time import sleep
from threading import Lock, Thread

a = 5
b = 5

a_lock = Lock()
b_lock = Lock()


def thred1calc():
    global a
    global b

    print('Thread1 aquiring lock a')
    a_lock.acquire(timeout=1)
    sleep(5)

    print('Thread1 aquiring lock b')
    b_lock.acquire(timeout=1)
    sleep(5)

    a += 5
    b += 5

    print('Thread1 releasing both lock')
    a_lock.release()
    b_lock.release()

def thred2calc():
    global a
    global b

    print('Thread2 aquiring lock b')
    b_lock.acquire(timeout=1)
    sleep(5)

    print('Thread2 aquiring lock a')
    a_lock.acquire(timeout=1)
    sleep(5)

    a += 10
    b += 10

    print('Thread2 releasing both lock')
    b_lock.release()
    a_lock.release()


if __name__ == "__main__":
    print("Started main")
    thr1 = Thread(target=thred1calc)
    thr1.start()

    thr2 = Thread(target=thred2calc)
    thr2.start()
