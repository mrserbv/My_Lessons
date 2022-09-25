
# Пример использования семафора в моделировании работы ночного клуба

import time
from threading import Semaphore, Thread


class NightClub:
    def __init__(self, num_places=3):
        self.bouncer = Semaphore(num_places)  # Вышибала - это семафор с ограничением 3 мест в клубе

    def open_club(self):
        num_guests = 10  # Количество желающих посетить ночной клуб
        for x in range(1, num_guests):  # Для каждого гостя
            t = Thread(target=self.guest, args=[x])  # создаем отдельный поток
            t.start()  # И запускаем его

    def guest(self, guest_id):
        print(f'\n Guest {guest_id} is waiting to entering the night club')
        self.bouncer.acquire()
        print(f'\n Guest {guest_id} is doing some dancing')
        time.sleep(0.2)
        print(f'\n Guest {guest_id} is leaving the night club')
        self.bouncer.release()


if __name__ == "__main__":
    print("Начало программы <main>")
    club = NightClub()
    club.open_club()
