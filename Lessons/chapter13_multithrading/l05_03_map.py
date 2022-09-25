

# Использование функции map() c ThreadPoolExecutor()
# Запуск одной функции с разными аргументами

from concurrent.futures import ThreadPoolExecutor
from Lessons.chapter13_multithrading.l01_problem_demo import read_ints
from Lessons.chapter13_multithrading.l03_01_seq_vs_paralle import count_three_sum

if __name__ == "__main__":
    print("Started main")

    nums = read_ints("l01_data_digits.txt")

    with ThreadPoolExecutor(max_workers=4) as executor:
        # max_workers=4 - количество максимально выделяемых потоков !!!
        results = executor.map(count_three_sum, (nums, nums), ('t1', 't2'))
        # Создаются два потока по количеству аргументов!!!
        for r in results:
            print(f'{r=}')  # По сути это также блокирующий вызов

    print("Ended main")
