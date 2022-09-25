
# Демонстрация DeadLock - reentrance

import threading

# --------- Вариант 1 - Двойной лок -----------------
# lock_obj = threading.Lock()
# print('Acquire 1st time')
# lock_obj.acquire()  # Захватываем Lock в 1 раз
#
# print('Acquire 2st time')
# lock_obj.acquire()  # При попытке захватить второй раз получаем DeadLock
#
# print('Realising')  # И этой точки уже не достигаем
# lock_obj.release()

# --------- Вариант 2  - Рекурсивный дэдлок  -----------
# lock_obj = threading.Lock()
# def reentrance():
#     print('Srart')
#     lock_obj.acquire()
#     print('Aquired')
#     reentrance()  # рекурсия повторно вызывает Lock => DeadLock
#     lock_obj.release()
#     print('Relesed')
# reentrance()

# --------- Вариант 3  - Избежание DeadLock  -----------
# Используется рекурсивный Lock - RLock()
lock_obj = threading.RLock()
print('Acquire 1st time')
lock_obj.acquire()  # Захватываем Lock в 1 раз

print('Acquire 2st time')
lock_obj.acquire()  # При попытке захватить второй раз получаем DeadLock

print('Realising')  # И этой точки уже не достигаем
lock_obj.release()
