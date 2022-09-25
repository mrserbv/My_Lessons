
# Демонстрация кооперативной отмены потока по флагу с использованием класса

from threading import Lock, Thread
from time import sleep
from l01_problem_demo import read_ints


class ThreeSumTask:

    def __init__(self, nums):
        self.nums = nums
        self.canceled = False
        self.lock_obj = Lock()

    def run(self):
        self.count_three_sum()

    def cancel(self):
        with self.lock_obj:
            self.canceled = True

    def count_three_sum(self):
        print(f"Started count_three_sum() ")
        n = len(self.nums)
        counter = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.canceled:
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

    task = ThreeSumTask(read_ints("l01_data_digits.txt"))
    thr1 = Thread(target=task.run, daemon=False)
    thr1.start()

    sleep(10)

    task.cancel()
    thr1.join()
    print("Ended main")
