
# Пример обработки исключений в Thread()
# Обработка может производиться только внутри потока!!!

import threading
import time

throw = False  # Флаг вызова исключения


def count():
    i = 0
    # ----- Без обработки исключений --
    # while True:
    #     if throw:
    #         raise ZeroDivisionError()
    #     i += 1
    #     print(f'{i=}')
    #     time.sleep(1)
    # ---------------------------------

    # ----- Оработка исключений --------
    try:
        while True:
            if throw:
                raise ZeroDivisionError()
            i += 1
            print(f'{i=}')
            time.sleep(1)
    except ZeroDivisionError:
        print('Exception occured')


if __name__ == "__main__":
    print("Started main")

    thr1 = threading.Thread(target=count)
    thr1.start()

    # ---- Отловить исключение нижеприведенным образом
    #                       НЕЛЬЗЯ !!!!!!
    # try:
    #     thr1.start()
    # except:
    #     print('Excepted')
    # Thread() не передает исключение в основной поток !!!
    # -------------------------------------------------

    time.sleep(3)
    throw = True  # Вызов исключения
    for x in range(1, 5):
        print(f'{x=}')
        time.sleep(1)
    print("Ended main")
