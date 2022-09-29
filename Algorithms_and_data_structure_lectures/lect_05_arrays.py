
# Основы работы с массивами

def array_search(array: list, size: int, number: int):
    """Осуществляет поиск числа num в массиве array
    от 0 до size включительно.
    Возвращает индекс элемента в массиве.
    Или (-1), если такого нет.
    Если в массиве несколько одинаковых искомых элементов,
    то возвращает индекс первого
    """
    for i in range(size):
        if array[i] == number:
            return i
    return -1


def invert_array(array: list, size: int):
    """ Обращение массива
    в рамках индекса от 0 до size-1
    """
    for i in range(size // 2):
        array[i], array[size - 1 - i] = array[size - 1 - i], array[i]


def left_cyclic_shift(array: list, size: int):
    """ Циклический сдвиг массива влево """
    tmp = array[0]
    for i in range(size-1):
        array[i] = array[i+1]
    array[size-1] = tmp


def right_cyclic_shift(array: list, size: int):
    """ Циклический сдвиг массива вправо """
    tmp = array[size-1]
    for i in range(size-2, -1, -1):
        array[i+1] = array[i]
    array[0] = tmp


def eratosthenes_sieve(n: int):
    """ Функция возвращает лист из значений bool,
    длиной n, и представляющий собой
    РЕШЕТО ЭРАТОСФЕНА
    """
    a = [True] * n
    a[0] = a[1] = False
    for i in range(2, n):
        if a[i]:
            for j in range(2*i, n, i):
                a[j] = False
    return a


def test_array_search():
    array_1 = [1, 2, 3, 4, 5]
    test_1 = array_search(array_1, 5, 8)
    if test_1 == -1:
        print('# Test1 - OK')
    else:
        print('# Test1 - Fail')

    array_2 = [-1, -2, -3, -4, -5]
    test_2 = array_search(array_2, 5, -3)
    if test_2 == 2:
        print('# Test2 - OK')
    else:
        print('# Test2 - Fail')

    array_3 = [10, 20, 30, 10, 10]
    test_3 = array_search(array_3, 5, 10)
    if test_3 == 0:
        print('# Test3 - OK')
    else:
        print('# Test3 - Fail')


def test_invert_array():
    array_1 = [1, 2, 3, 4, 5]
    print(array_1)
    invert_array(array_1, 5)
    print(array_1)
    if array_1 == [5, 4, 3, 2, 1]:
        print('# Test1 - OK')
    else:
        print('# Test1 - Fail')

    array_2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(array_2)
    invert_array(array_2, 8)
    print(array_2)
    if array_2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print('# Test2 - OK')
    else:
        print('# Test2 - Fail')


def test_cyclic_shift():
    array_1 = [1, 2, 3, 4, 5]
    print(array_1)
    right_cyclic_shift(array_1, 5)
    print(array_1)
    if array_1 == [5, 1, 2, 3, 4]:
        print('# Test1 - OK')
    else:
        print('# Test1 - Fail')

    array_2 = [1, 2, 3, 4, 5]
    print(array_2)
    left_cyclic_shift(array_2, 5)
    print(array_2)
    if array_2 == [2, 3, 4, 5, 1]:
        print('# Test2 - OK')
    else:
        print('# Test2 - Fail')


def test_eratosthenes_sieve():
    n = 10000
    a = eratosthenes_sieve(n)
    for i in range(n):
        if a[i]:
            print(i, sep='', end='\n')


if __name__ == "__main__":
    # test_array_search()
    # test_invert_array()
    # test_cyclic_shift()
    test_eratosthenes_sieve()
