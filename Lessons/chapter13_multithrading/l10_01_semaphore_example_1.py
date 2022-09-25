# Демонстрация работы семафора для ограничения количества потоков к одному ресурсу
from random import randint
from threading import Event, Semaphore
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def work(smphr):
    sleep(randint(5, 10))
    print('Realising one connection')
    smphr.release()


def connect(smphr, max_connections):
    with ThreadPoolExecutor(max_workers=2) as ex:
        while True:
            connections_counter = 0
            while not max_connections.is_set():
                print(f'\nConnection n = {connections_counter}')
                smphr.acquire()
                connections_counter += 1

                ex.submit(work, smphr)

                sleep(0.8)

            sleep(5)


def connections_guarg(smphr, max_connections):
    while True:
        print(f'[guard] semaphore = {smphr._value}')
        sleep(1.5)

        if smphr._value == 0:
            max_connections.set()
            print(f'[guard] Reached max connections!')
            sleep(2)
            max_connections.clear()


if __name__ == "__main__":
    print("Начало программы <main>")
    max_connection = 10
    reached_max_connections = Event()

    semaphore = Semaphore(value=max_connection)

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(connections_guarg, semaphore, reached_max_connections)
        executor.submit(connect, semaphore, reached_max_connections)
