
# Демонстрация отмены процесса

import multiprocessing
import time

from l01_problem_demo import read_ints, count_three_sum

if __name__ == "__main__":
    print("Started main")
    nums = read_ints("l01_data_digits.txt")

    # Создание процесса для выполнения функции
    process = multiprocessing.Process(target=count_three_sum, args=(nums,))
    process.start()

    time.sleep(5)

    # Отменяем процесс
    process.terminate()

    print("Ended main")
