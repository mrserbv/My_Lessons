

# Создание и использование потока

from l01_problem_demo import read_ints, count_three_sum
from threading import Thread

if __name__ == "__main__":
    print("Started main")
    nums = read_ints("l01_data_digits.txt")

    # ---- Creates new thead as a class Thread ------
    thr1 = Thread(target=count_three_sum, args=(nums,), daemon=True)
    # daemon=True  - Background поток. Завершается сразу после завершения программы.
    # daemon=False - Foreground поток. Программа заврешается только после потока
    # args=(nums,) - передача позиционных аргументов
    # kwargs=dict(nums_list=nums) - передача именованных аргументов
    thr1.start()  # Starting the thread
    # ------------------------------------------------

    print('Resume program.')
    thr1.join()  # Основной поток продолжится только после завершения <thr1>
    print("Ended main")
