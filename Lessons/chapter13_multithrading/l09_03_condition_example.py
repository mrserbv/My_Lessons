
# Пример использования Condition()

import time
from multiprocessing import Process, Condition

cond = Condition()


def f1():
    while True:
        print(f'f2 running')
        cond.acquire()
        print(f'f1 acquire')
        cond.wait()
        print('Получили событие')
        cond.release()


def f2():
    for i in range(20):
        if i % 4 == 0:
            cond.acquire()
            cond.notify()
            cond.release()
            print('notify')
        else:
            print(f'f2: {i=}')
        time.sleep(0.5)


if __name__ == "__main__":
    print("Начало программы <main>")
    Process(target=f1).start()
    Process(target=f2).start()
