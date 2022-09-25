# Для устранения ошибки используем lock
import time
import threading
from concurrent.futures import ThreadPoolExecutor


class BankAccount:
    """ Класс банковского аккаунта """
    def __init__(self):
        self.balance = 100  # Баланс по умолчанию равен 100
        self.lock_obj = threading.Lock()  # Создаем объект Lock

    def update(self, transaction, amount):
        print(f'{transaction} started')
        with self.lock_obj:  # Менеджер контекста: Если один поток захватил
            #                  self.lock_obj, другой поток
            #                  не может его использовать
            #                  Сюда может зайти только один поток
            tmp_amount = self.balance
            tmp_amount += amount
            time.sleep(1)
            self.balance = tmp_amount
        print(f'{transaction}  ended. {self.balance=}')

        #     Это то же самое, что:
        # self.lock_obj.acquire()
        # tmp_amount = self.balance
        # tmp_amount += amount
        # time.sleep(1)
        # self.balance = tmp_amount
        # self.lock_obj.release()


if __name__ == '__main__':
    # lock_obj = threading.Lock()  # Создание объекта Lock
    # print(lock_obj.locked())  # возвращает False
    #
    # lock_obj.acquire()  # Блокирование потока
    # print(lock_obj.locked())  # возвращает True
    #
    # lock_obj.release()  # Снятие блокировки
    # print(lock_obj.locked())  # возвращает False

    acc = BankAccount()
    print(f'Main started. acc.balance = {acc.balance}')
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(acc.update, ('refill', 'withdraw'), (100, -200))
    print(f'End of main. Balance = {acc.balance}')
