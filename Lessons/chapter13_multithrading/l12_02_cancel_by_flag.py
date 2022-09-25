
# Демонстрация кооперативной отмены потока по флагу

from threading import Thread
from time import sleep

from l01_problem_demo import read_ints

should_stop = False  # Флаг для отмены потока
# Создание модифицированной функции count_three_sum


def count_three_sum(nums_list, threadname=''):
    print(f"Started count_three_sum() in {threadname}")
    n = len(nums_list)
    counter = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if should_stop:
                    print('Task was cancelled')
                    counter = -1
                    return counter
                if nums_list[i] + nums_list[j] + nums_list[k] == 0:
                    counter += 1
                    print(f"Triple found in {threadname}: {nums_list[i], nums_list[j], nums_list[k]}")
    print(f"Ended count_three_sum in {threadname}. Triplets counter = {counter}")
    return counter


if __name__ == "__main__":
    print("Started main")
    nums = read_ints("l01_data_digits.txt")

    thr1 = Thread(target=count_three_sum, args=(nums,), daemon=False)
    thr1.start()

    sleep(5)

    should_stop = True

    sleep(2)

    print("Ended main")
