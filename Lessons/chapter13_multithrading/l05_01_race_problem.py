
# Пример проблемы Race condition (гонка)

import time
from concurrent.futures import ThreadPoolExecutor


class BankAccount:
    """ Класс банковского аккаунта """
    def __init__(self):
        self.balance = 100  # Баланс по умолчанию равен 100

    def update(self, transaction, amount):
        print(f'{transaction} started')
        tmp_amount = self.balance
        tmp_amount += amount
        time.sleep(1)
        self.balance = tmp_amount
        print(f'{transaction}  ended')


if __name__ == '__main__':
    acc = BankAccount()
    print(f'Main started. acc.balance = {acc.balance}')
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(acc.update, ('refill', 'withdraw'), (100, -200))
    print(f'End of main. Balance = {acc.balance}')
    # Баланс должен быть нулевой. Баланс не соответствует требуемому!!!!!!!!