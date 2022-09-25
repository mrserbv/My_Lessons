import os


class TrueOrFalseGame:
    """Класс, реализующий основное поведение игры 'Верю/Неверю'
    """

    def __init__(self, max_mistake: int = 2, filepath: str = '2022_09_25_TrueOrFalseGame_Questions.csv'):
        self.__filepath = filepath
        self.__max_mistake = max_mistake
        self.__count_mistake = 0
        self.__questions = []
        self.__count_question = -1
        self.__is_run_game = False
        self.__is_win = False

    def run_game(self):
        self.__is_run_game = True
        self.__load_questions()

    # noinspection PyTypeChecker
    def __load_questions(self):
        """ Приватный метод загрузки вопросов
        из файла, адрес которого находится в атрибуте self.__filepath,
        и записи в атрибут self.__questions в виде листа.
        Метод выдает исключение, если файл не найден."""
        if not os.path.exists(self.__filepath):
            raise FileNotFoundError('Файл с игрой не найден.')
        with open(self.__filepath, 'r') as file:
            text = file.readlines()
        for line in text:
            quest = line.strip('\n"').split(';')
            if quest[1].lower() == 'yes':
                quest[1] = True
            elif quest[1].lower() == 'no':
                quest[1] = False
            else:
                raise Exception('Файл не соответствует формату.')
            self.__questions.append(quest)

    def set_filepath(self, filepath: str):
        """Метод передачи адреса файла с игрой и записи
        в атрибут self.__filepath
        Метод выдает исключение, если введены 'плохие' данные."""
        if type(filepath) != str:
            raise TypeError('Введенный путь не является строкой!')
        if not os.path.exists(filepath):
            raise FileNotFoundError('Указанный файл не найден.')
        self.__filepath = filepath

    def set_max_mistake(self, max_mistake: int):
        """Метод передачи числа максимально допустимых ошибок и записи
        в атрибут self.__max_mistake.
        Метод выдает исключение, если введены 'плохие' данные."""
        if type(max_mistake) != int:
            raise TypeError('Введенные данные не относятся к int!')
        if max_mistake < 0:
            raise ValueError('Количество ошибок не может быть меньше нуля!')
        self.__max_mistake = max_mistake

    def next_question(self):
        """Метод, увеличивающий счетчик вопросов
        и возвращающий текст вопроса.
        Метод выдает исключение, если игра не запущена."""
        if self.__is_run_game:
            self.__count_question += 1
            return self.__questions[self.__count_question][0]
        else:
            raise Exception('Игра не запущена.')

    def set_answer(self, ans):
        """Метод, принимающий ответ от клиентского кода
        и возвращающий корте:
        Первый элемент - True или False - сообщает правильный ли ответ.
        Второй элемент - Объяснение в копросу из файла.
        Если вопросы закончились, метод изменяет статус игры на False.
        Если количество ошибок превышено, метод изменяет статус игры на False.
        Метод устанавливает победу, если вопросы закончились, а количество ошибок не превышено.
        Метод выдает исключение, если игра не запущена
        """
        if self.__is_run_game:
            if type(ans) != bool:
                raise ValueError('Ответ должен быть типа bool!')
            if self.__questions[self.__count_question][1] == ans:
                final = True
            else:
                final = False
                self.__count_mistake += 1
                if self.__count_mistake > self.__max_mistake:
                    self.__is_run_game = False
                    self.__is_win = False
            if (self.__count_question >= len(self.__questions) - 1 and
                    self.__count_mistake <= self.__max_mistake):
                self.__is_run_game = False
                self.__is_win = True
            return final, self.__questions[self.__count_question][2]
        else:
            raise Exception('Игра не запущена.')

    def get_status(self):
        """Метод возвращает атрибут статуса игры"""
        return self.__is_run_game

    def is_win(self):
        """Метод возвращает атрибут победы в игре"""
        return self.__is_win


if __name__ == "__main__":
    print('Welcome to game "True or False".\nPlease, ask some questions.\n')

    game = TrueOrFalseGame()
    game.set_filepath('2022_09_25_TrueOrFalseGame_Questions.csv')
    game.set_max_mistake(2)

    game.run_game()
    while game.get_status():
        question = game.next_question()
        answer = input(f'Question: {question} (Y/N): ')
        f1 = lambda x: True if x in 'yYдД' else False
        result = game.set_answer(f1(answer))
        f2 = lambda x: 'Correct' if x else 'Wrong'
        print(f'{f2(result[0])}. {result[1]}')
    if game.is_win():
        print('Congratulations! You are WIN!!!')
    else:
        print('Sorry! You are loose.')
