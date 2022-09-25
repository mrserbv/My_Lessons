# Демонстрация проблемы однопоточности программ
from random import randint


def gen_file():
    """ The function create a file with randomly generated
    numbers in range from -999999 to 999999"""
    filename = "l01_data_digits.txt"
    with open(filename, "w") as file:
        [file.write(f"{randint(-999999, 999999)}\n") for _ in range(1_000)]


def read_ints(path):
    """ The function read the file with numbers
    and return result in variable <lst>"""
    lst = []
    with open(path, 'r') as file:
        while line := file.readline():
            lst.append(int(line))
    return lst


def count_three_sum(ints):
    print("Started count_three_sum()...")
    n = len(ints)
    counter = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f"Triple found: {ints[i], ints[j], ints[k]}")
    print(f"Ended count_three_sum. Triplets counter = {counter}")


if __name__ == "__main__":
    print("Started main")
    nums = read_ints("l01_data_digits.txt")
    count_three_sum(nums)
    print("What are we waiting for?...")  # These lines will be output only after
#                                           executing the count_three_sum()
    print("Ended main")
