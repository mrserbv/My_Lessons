
# Пример использования барьеров

from threading import Barrier, Thread
from time import sleep
from datetime import datetime
from random import randrange


class HorseRace:
    def __init__(self):
        self.barrier = Barrier(4)
        self.horses = ["Artax", "Frankel", "Bucephalus", "Barton"]

        self.position = []  # Для ДЗ: создаем список - турнирную таблицу

    def lead(self):
        horse = self.horses.pop()
        sleep(randrange(1, 5))
        print(f"\n{horse} reached the barrier at {datetime.now()}")
        self.barrier.wait()

        sleep(randrange(1, 5))
        print(f"\n{horse} started at {datetime.now()}")

        sleep(randrange(2, 5))

        self.position.append(horse)  # Для ДЗ: Лошадь после финиша записывается в турнирную таблицу
        print(f"\n{horse} finished at {datetime.now()}")

        self.barrier.wait()
        print(f"\n{horse} went sleeping")


if __name__ == '__main__':
    print("Race preparation")

    race = HorseRace()
    # for x in range(4):
    #     Thread(target=race.lead).start()

    # Для ДЗ: создаем потоки со ссылкой на каждый, чтобы дальше
    # можно было заджойнить программу в ожидании каждого потока
    # иначе не вывести турнирную таблицу
    thr = []
    for x in range(4):
        thr.append(Thread(target=race.lead))
        thr[x].start()
    for x in range(4):
        thr[x].join()
    # Для ДЗ: Выводим турнирную таблицу
    print(race.position)  # Для ДЗ: Выводим турнирную таблицу
