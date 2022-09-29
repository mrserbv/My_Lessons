# Генерация всех перестановок через рекурсию

def gen_bin(M, prefix=''):
    if M == 0:
        print(prefix)
        return
    gen_bin(M-1, prefix + '0')
    gen_bin(M-1, prefix + '1')


def generate_numbers(N: int, M: int, prefix=None):
    """Генерирует все числа (с лидирующими незначащими нулями)
    N - основание системы счисления (N <= 10),
    M - длина числа,
    prefix - для использования в незначащих разрядах
    """
    if M == 0:
        print(prefix)
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M - 1, prefix)
        prefix.pop()


def find(x, A):
    """Ищет х в А и возращает Истину, если такой есть
    и Ложь, если такого нет
    """
    for elem in A:
        if elem == x:
            return True
    return False


def generate_permutations(N: int, M: int, prefix=None):
    """Генерация всех перестановок N чисел в M позициях,
    с префиксом prefix"""
    M = N if M == -1 else M  # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, sep='', end=', ')
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()



if __name__ == '__main__':
    #gen_bin(3) # для двоичных чисел
    # generate_numbers(10, 2)
    generate_permutations(6, 6)
