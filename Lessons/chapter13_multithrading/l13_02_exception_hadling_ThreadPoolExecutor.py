
# Пример обработки исключений в ThreadPoolExecutor()
# Обработка может производиться как внутри потока, так и в основном

import time
from concurrent.futures import ThreadPoolExecutor, CancelledError


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
        future = executor.submit(div, 3, 15)
        time.sleep(5)
        print('Nothing happens untill...')

        # ------ Способ перехвата исключения: ----------
        try:
            res = future.result()  # Получает результат вместе с исключением
        except CancelledError as ex:
            print(repr(ex))
        except TimeoutError as ex:
            print(repr(ex))
        except Exception as ex:
            print(repr(ex))

    print('Main ended')
