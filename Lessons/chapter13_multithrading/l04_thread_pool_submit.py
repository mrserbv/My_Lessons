
# Вызов concurent.futures.ThreadPoolExecutor()
# с возвратом объектов класса futures и возвратом результатов функций

from concurrent.futures import ThreadPoolExecutor
import time


def div(divisor, limit):
    print(f'start div={divisor}')
    for x in range(1, limit):
        if x % divisor == 0:
            print(f'divisor = {divisor}, x = {x}')
        time.sleep(0.2)
    print(f'ended div')


def div2(divisor, limit):
    print(f'start div={divisor}')
    result = 0
    for x in range(1, limit):
        if x % divisor == 0:
            result += x
        time.sleep(0.2)
    print(f'ended div')
    return result


if __name__ == "__main__":
    print("Started main")

    # ---------- Вариант 1. Вызов через менеджер контекстов: --------------
    # with ThreadPoolExecutor(max_workers=2) as executor:
    #     executor.submit(div, 3, 25)
    #     executor.submit(div, 5, 25)
    #
    #     print("Immediatelly printed out after submit")
    #
    # print("After with block")

    # ---------- Вариант 2. Простой вызов ------------------------
    # executor = ThreadPoolExecutor(max_workers=2)
    # executor.submit(div, 3, 25)
    # executor.submit(div, 5, 25)
    # executor.shutdown(wait=True)
    # # wait=True - Продолжение основного потока только после выполнения потоков
    # # wait=False - Продолжаем программу не дожидаясь окончания потоков
    # print("\nEnded main")

    futures = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures.append(executor.submit(div2, 3, 25))
        futures.append(executor.submit(div2, 5, 25))

        while futures[0].running() and futures[1].running():  # Цикл вывода
            print('.', end='')  # точек при условии работоспособности
            time.sleep(0.2)  # каждого из двух потоков

        for f in futures:
            print(f'{f.result()}')  # Получение результата функций
            #                         Он же блокирует продолжение

        print("Immediatelly printed out after submit")

    print("After with block")
