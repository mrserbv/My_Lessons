
# Пример взаимной блокировки

import time
from threading import Thread


def f1():  # Демонстрационная функция
    print('Running 1st thread\n')
    print('f1 joining f2\n')
    time.sleep(2)
    thr2.join()
    print('f1 sleep\n')
    time.sleep(5)
    print('End of f1\n')


def f2():  # Демонстрационная функция
    print('Running 2nd thread\n')
    print('f2 joining f1\n')
    time.sleep(2)
    thr1.join()
    print('f2 sleep\n')
    time.sleep(5)
    print('End of f2\n')


if __name__ == "__main__":
    print("Started main")
    thr1 = Thread(target=f1)
    thr2 = Thread(target=f2)
    thr1.start()
    thr2.start()

    # Получаем DeadLock
