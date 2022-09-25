

# Демонстрация разницы между последовательными и потоковыми вычислениями

import time
from functools import wraps
from threading import Thread
from l01_problem_demo import read_ints


# Создание декоратора, осуществляющего измерение времени выполнения функции
def measure_time(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'Executed {func} in {elapsed:0.2f} seconds')
        return result
    return wrap


# Создание модифицированной функции count_three_sum
def count_three_sum(nums_list, threadname=''):
    print(f"Started count_three_sum() in {threadname}")
    n = len(nums_list)
    counter = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums_list[i] + nums_list[j] + nums_list[k] == 0:
                    counter += 1
                    print(f"Triple found in {threadname}: {nums_list[i], nums_list[j], nums_list[k]}")
    print(f"Ended count_three_sum in {threadname}. Triplets counter = {counter}")
    return counter


@measure_time
def run_in_parallel(nums_list):
    thrd1 = Thread(target=count_three_sum, args=(nums_list, 'Thread - 1',), daemon=True)
    thrd2 = Thread(target=count_three_sum, args=(nums_list, 'Thread - 2',), daemon=True)
    thrd1.start()
    thrd2.start()
    print('\nGoing to wait for threads.')
    thrd1.join()
    thrd2.join()


@measure_time
def run_sequentially(nums_list):
    count_three_sum(nums_list, '№ 1')
    count_three_sum(nums_list, '№ 2')


if __name__ == "__main__":
    print("Started main")
    nums = read_ints("l01_data_digits.txt")
    run_in_parallel(nums)
    run_sequentially(nums)
    print("Ended main")
