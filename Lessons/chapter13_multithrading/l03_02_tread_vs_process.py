
# Демонстрация разницы между потоками и процессами

from threading import Thread
from multiprocessing import Process
from l01_problem_demo import read_ints
from l03_01_seq_vs_paralle import measure_time


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
                    # print(f"Triple found in {threadname}: {nums_list[i], nums_list[j], nums_list[k]}")
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
def run_process(nums_list):
    proc1 = Process(target=count_three_sum, args=(nums_list, 'Process - 1',), daemon=True)
    proc2 = Process(target=count_three_sum, args=(nums_list, 'Process - 2',), daemon=True)
    proc1.start()
    proc2.start()
    print('\nGoing to wait for proccess.')
    proc1.join()
    proc2.join()


if __name__ == "__main__":
    print("Started main")
    nums = read_ints("l01_data_digits.txt")
    run_in_parallel(nums)
    run_process(nums)
    print("Ended main")
