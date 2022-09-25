import random


class Gallows:  # Игра Виселица
    def __init__(self):
        self.__max_attempt = 10  # Максимальное число попыток
        self.__attempts_made = 0  # Сделано попыток
        self.word = ''  # Загаданное слово
        self.answer = []  # Лист с отгаданными буквами

    def set_max_attempt(self, n):
        self.__max_attempt = n

    def set_word(self):  # Метод получения случайного слова из файла
        filename = "2022_09_21-ДЗ Виселица-WordsStockRus.txt"  # Название файла
        with open(filename, 'r', encoding='utf-8') as file:
            nunber_of_strings = 0  # количество строк (или слов)
            for line in file:
                nunber_of_strings += 1  # подсчет количества строк
            file.seek(0, 0)  # перевод каретки в начальное положение
            num_str = random.randint(0, nunber_of_strings)   # выбор случайного слова
            for _ in range(num_str):
                word = file.readline().strip()

        self.word = word  # запись слова в атрибут
        self.answer = ['-'] * len(word)  # создание отгадываемого листа
        self.__attempts_made = 0  # обнуление попыток

    def run_game(self):
        self.set_word()
        print('Добро пожаловать в игру Виселица.')
        print('Отгадайте слово по буквам.')
        print('Загадано слово:', ''.join(self.answer))
        print(f'У вас есть {self.__max_attempt} попыток.')
        while self.__attempts_made < self.__max_attempt:
            letter = input('Введите одну букву: ')  # пока нет защиты от неправильных символов
            self.__attempts_made += 1
            counter = self.word.count(letter)
            if counter > 0:
                print('Такая буква есть.')
                i = 0
                while counter > 0:
                    i = self.word.find(letter, i)
                    self.answer[i] = letter
                    counter -= 1
                    i +=1
            else:
                print('К сожалению такой буквы нет.')
            print(f"Отгадываемое слово выглядит так: {''.join(self.answer)}")
            print(f"Осталось {self.__max_attempt - self.__attempts_made} попыток.")

            if '-' not in self.answer:
                print('!!! Поздравляем с победой !!!')
                break
        else:
            print('Увы... Попытки кончились. Вы повешены...')
            print('    ______')
            print('   |      |')
            print('   |    O_|')
            print('   |   -|-')
            print('   |   / \\')
            print('  _|_')
            print(f'Было загадано слово {self.word}')


st = Gallows()
st.run_game()
