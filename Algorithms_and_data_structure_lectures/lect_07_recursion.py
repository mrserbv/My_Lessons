# Пример рекурсии в виде матрешки
def matryoshka(n):
    if n == 1:
        print('Матрешечка')
    else:
        print(f'Верх матрешки № {n}')
        matryoshka(n-1)
        print(f'Низ матрешки № {n}')

# Вычисление факториала методом рекурсии
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

# Поиск НОД алгоритмом Евклида
def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    elif a < b:
        return gcd(a, b-a)


# Поиск НОД алгоритмом Евклида модернизированный
def gcd2(a, b):
    return a if b == 0 else gcd2(b, a % b)


# Быстрое возведение в степень
def pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(a*a, n // 2)
    else:
        return pow(a, n-1) * a


if __name__ == '__main__':
    # matryoshka(996)
    # print(factorial(900))
    # print(gcd2(5565324, 12115632651))
    print(pow(2, 100))
