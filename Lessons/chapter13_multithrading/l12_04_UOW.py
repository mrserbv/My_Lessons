
# Демонстрация Pattern_Unit of Work (UOW)

import threading
from time import sleep
from l01_problem_demo import read_ints


class StoppableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def is_stoped(self):
        return self.stop_event.is_set()


class ThreeSumUnitOfWork(StoppableThread):  # Наследуем класс от Thread

    def __init__(self, nums, namethrd='ThreadName'):
        super().__init__(name=namethrd)  # Вызываем конструктор родительского потока, передаем имя потока
        self.nums = nums
        self.threadname = namethrd

    def run(self):
        print(f'{self.threadname} starts')
        self.count_three_sum()
        print(f'{self.threadname} ends')

    def count_three_sum(self):
        print(f"Started count_three_sum() ")
        n = len(self.nums)
        counter = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if super().is_stoped():
                        print('Task was cancelled')
                        counter = -1
                        return counter
                    if self.nums[i] + self.nums[j] + self.nums[k] == 0:
                        counter += 1
                        print(f"Triple found: {self.nums[i], self.nums[j], self.nums[k]}")
        print(f"Ended count_three_sum. Triplets counter = {counter}")
        return counter


if __name__ == "__main__":
    print("Started main")

    task = ThreeSumUnitOfWork(read_ints("l01_data_digits.txt"), 'Tread 1')
    task.start()

    sleep(5)

    task.stop()
    task.join()
    print(task.is_stoped())
    print("Ended main")
