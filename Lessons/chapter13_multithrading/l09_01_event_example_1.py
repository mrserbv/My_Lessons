import random
import threading
from enum import Enum
from time import sleep


class Event:
    def __init__(self):
        self.__handlers = []

    def __call__(self, *args, **kwargs):
        for f in self.__handlers:
            f(*args, **kwargs)

    def __iadd__(self, other):
        self.__handlers.append(other)
        return self

    def __isub__(self, other):
        self.__handlers.remove(other)
        return self


class OperationStatus(Enum):
    FINISHED = 0
    FAULTED = 1


class Protocol:
    def __init__(self, port, ip_address):
        self.port = port
        self.ip_address = ip_address
        self.massage_received = Event()
        self.set_ip_port()

    def set_ip_port(self):
        print("Установка IP")
        sleep(0.2)
        return self

    def send(self, op_code, param):
        def process_sending():
            print(f"Операция отправки с параметрами {param=}")
            result = self.process(op_code, param)
            self.massage_received(result)
        thr = threading.Thread(target=process_sending)
        thr.start()

    def process(self, op_code, param):
        print(f"Процесс операции = {op_code} с {param=}")
        sleep(3)
        # third party respond
        finished = random.randint(0, 1) == 1
        return OperationStatus.FINISHED if finished else OperationStatus.FAULTED


class BankTerminal:
    def __init__(self, port, ip_address):
        self.ip_address = ip_address
        self.port = port
        self.protocol = Protocol(port, ip_address)
        self.protocol.massage_received += self.on_massage_received
        self.operation_signal = threading.Event()

    def on_massage_received(self, status):
        print(f"Сигнализация для Event: {status}")
        self.operation_signal.set()

    def purchase(self, amount):
        def process_purchase():
            purchase_op_code = 1
            self.protocol.send(purchase_op_code, amount)
            self.operation_signal.clear()
            print("\nОжидание сигнала")
            self.operation_signal.wait()
            print("Покупка завершена")
        thr = threading.Thread(target=process_purchase)
        thr.start()
        return t


if __name__ == "__main__":
    print("Начало программы <main>")
    bt = BankTerminal(10, '192.168.1.1.')
    t = bt.purchase(20)
    print('Программа <main> ожидает завершение потока покупки 1')
    t.join()
    t = bt.purchase(30)
    print('Программа <main> ожидает завершение потока покупки 1')
    t.join()
    print('Окончание <main>')
