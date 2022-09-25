# Пример обработки исключений в ThreadPoolExecutor()
# Обработка может производиться как внутри потока, так и в основном

import time
from concurrent.futures import ThreadPoolExecutor


def div(divisor, limit):
    print(f'start div={divisor}')

    result = 0
    for x in range(1, limit):
        if x % divisor == 0:
            result += x
            print(f'divisor = {divisor}, x = {x}')
        time.sleep(0.2)
    print('Raise exception')
    raise Exception('Bad things happen!')


if __name__ == "__main__":
    print("Started main")
    with ThreadPoolExecutor(max_workers=2) as executor:
        res_list = executor.map(div, (3, 5), (15, 25))
        while res_list:
            # ------ Способ перехвата исключения: ----------
            try:
                cur_res = next(res_list)  # Получает результат вместе с исключением
            except StopIteration:  # Исключение-ошибка итерации
                print('Stop iteration Excepted')
                break
            except Exception as ex:
                print(repr(ex))
    print('Main ended')
