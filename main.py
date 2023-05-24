from datetime import datetime
import random
import locale

locale.setlocale(locale.LC_ALL, "ru")

commands = ('Вот список поддерживаемых команд:\n• Какое сегодня число?\n• Сколько время?\n• Список покупок\n• '
            'Посчитай\n• Случайный фильм\n• Разбор слова\n• Брось кубик\n• Подбрось монетку')

print('Привет, я твой персональный помощник')
print(commands)

list_things = []  # сюда записываются элементы списка покупок

while True:
    question = str(input('\033[34mЧто хочешь? \033[0m'))
    if question.lower() == 'какое сегодня число?':
        month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                 'ноября', 'декабря']  # список для вывода названия месяца на русском языке
        today = datetime.today()
        print(today.strftime("%A,"), today.day, month[today.month - 1], today.year, 'г.')

    elif question.lower() == 'сколько время?':
        today = datetime.today()
        print(today.hour, ':', today.minute, sep='')

    elif question.lower() == 'список команд' or question.lower() == 'команды':
        print(commands)

    elif question.lower() == 'список покупок':
        while True:
            setting = int(input('1 - Посмотреть список\n2 - Добавить элемент\n3 - Удалить элемент\n4 - Удалить все '
                                'элементы\n5 - Выйти из списка\nВыберите команду: '))
            if setting == 1:
                if len(list_things) == 0:
                    print('\033[31mСписок пуст \033[0m')  # пишет "список пуст", если в списке нет элементов
                else:
                    for i in list_things:  # цикл выводит список покупок
                        print('\033[36m- ', i, '\033[0m', sep='')
            if setting == 2:
                element = str(input('Введите название элемента: '))
                list_things.append(element)  # добавляет введенный элемент в список
                print('\033[32mЭлемент\033[1;32m', element, '\033[0;32mдобавлен в список\033[0m')

            if setting == 3:
                flag1 = 1
                element = str(input('Какой элемент хотите удалить?'))
                while flag1 == 1:  # цикл проверяет, есть ли элемент, который пользователь хочет удалить в списке
                    if element.lower() == 'назад':
                        flag1 = 0
                    elif element in list_things:
                        list_things.remove(element)
                        print('\033[31mЭлемент\033[1;31m', element, '\033[0;31mудален\033[0m')
                        flag1 = 0
                    else:
                        print('\033[31mТакого элемента нет. Напишите "Назад" чтобы выйти.\033[0m')
                        element = str(input('Какой элемент хотите удалить? '))
            if setting == 4:
                list_things.clear()  # удаляет все элементы из списка
                print('\033[31mСписок пуст \033[0m')

            if setting == 5:
                break

    elif question.lower() == 'посчитай':
        math = str(input('Введите математический пример: '))
        if math[-1] == '!':  # если необходимо посчитать факториал
            temp = 1
            for i in range(1, int(math[:-1]) + 1):
                temp *= i
            print("Ответ:\033[35m", temp, '\033[0m')
        else:
            print('Ответ:\033[35m', eval(math), '\033[0m')

    elif question.lower() == 'случайный фильм':
        film_thriller = ['В доме', 'Темный рыцарь', 'Окно во двор', 'Леон', 'Крепкий орешек', 'Титаник']
        film_drama = ['Бэтмен', 'В доме', 'Русский ковчег', 'Крестный отец', 'Властелин колец: Возвращение короля',
                      'Гладиатор', 'Темный рыцарь', 'Бемби', 'Аватар', 'Леон', 'Зеленая миля', 'Побег из Шоушенка',
                      'Форрест Гамп', 'Интерстеллар', 'Король Лев', '1+1', 'Москва слезам не верит',
                      'Джентльмены удачи', 'Титаник']
        film_melodrama = ['В доме', 'Амели', 'Энни Холл', 'Форрест Гамп', 'Шрэк', 'Москва слезам не верит', 'Девчата',
                          'Титаник']
        film_comedy = ['Эверест', 'Назад в будущее', 'В поисках Немо', 'Амели', 'Энни Холл', 'Форрест Гамп',
                       'Тайна Коко', '1+1', 'Шрэк', 'Москва слезам не верит', 'Джентльмены удачи', 'Девчата']
        film_fantastic = ['Назад в будущее', 'Темный рыцарь', 'Аватар', 'Интерстеллар', 'ВАЛЛ·И']
        film_detective = ['Бэтмен', 'Русский ковчег', 'Окно во двор', 'Джентльмены удачи']
        film_criminal = ['Бэтмен', 'Крестный отец', 'Леон', 'Брат 2', 'Крепкий орешек', 'Зеленая миля',
                         'Джентльмены удачи']
        film_mult = ['Эверест', 'Бемби', 'В поисках Немо', 'Тайна Коко', 'Король Лев', 'Шрэк', 'ВАЛЛ·И']
        film_fantasy = ['Эверест', 'Русский ковчег', 'Властелин колец: Возвращение короля', 'Зеленая миля',
                        'Тайна Коко', 'Шрэк']
        film_boevik = ['Властелин колец: Возвращение короля', 'Гладиатор', 'Темный рыцарь', 'Аватар', 'Леон', 'Брат 2',
                       'Крепкий орешек']
        genre = str(input('Выберите жанр: триллер, драма, мелодрама, комедия, фантастика, детектив, криминал, '
                          'мультфильм, фэнтези, боевик\n'))
        if genre.lower() == 'триллер':
            while True:
                print('\033[35m', random.choice(film_thriller), '\033[0m', sep='')
                while True:
                    choice = str(input('Еще раз или выйти? '))
                    if choice.lower() == 'выйти':
                        break
                    elif choice.lower() == 'еще раз' or choice.lower() == 'ещё раз':
                        print('\033[35m', random.choice(film_thriller), '\033[0m', sep='')
                        continue
                    else:
                        print('\033[31mЯ не знаю такой команды\033[0m')
                        continue
                break

        elif genre.lower() == 'драма':
            while True:
                print('\033[35m', random.choice(film_drama), '\033[0m', sep='')
                while True:
                    choice = str(input('Еще раз или выйти? '))
                    if choice.lower() == 'выйти':
                        break
                    elif choice.lower() == 'еще раз' or choice.lower() == 'ещё раз':
                        print('\033[35m', random.choice(film_drama), '\033[0m', sep='')
                        continue
                    else:
                        print('\033[31mЯ не знаю такой команды\033[0m')
                        continue
                break
        elif genre.lower() == 'мелодрама':
            while True:
                print('\033[35m', random.choice(film_melodrama), '\033[0m', sep='')
                while True:
                    choice = str(input('Еще раз или выйти? '))
                    if choice.lower() == 'выйти':
                        break
                    elif choice.lower() == 'еще раз' or choice.lower() == 'ещё раз':
                        print('\033[35m', random.choice(film_melodrama), '\033[0m', sep='')
                        continue
                    else:
                        print('\033[31mЯ не знаю такой команды\033[0m')
                        continue
                break
        elif genre.lower() == 'комедия':
            while True:
                print('\033[35m', random.choice(film_comedy), '\033[0m', sep='')
                while True:
                    choice = str(input('Еще раз или выйти? '))
                    if choice.lower() == 'выйти':
                        break
                    elif choice.lower() == 'еще раз' or choice.lower() == 'ещё раз':
                        print('\033[35m', random.choice(film_comedy), '\033[0m', sep='')
                        continue
                    else:
                        print('\033[31mЯ не знаю такой команды\033[0m')
                        continue
                break
        elif genre.lower() == 'фантастика':
            while True:
                print('\033[35m', random.choice(film_fantastic), '\033[0m', sep='')
                while True:
                    choice = str(input('Еще раз или выйти? '))
                    if choice.lower() == 'выйти':
                        break
                    elif choice.lower() == 'еще раз' or choice.lower() == 'ещё раз':
                        print('\033[35m', random.choice(film_fantastic), '\033[0m', sep='')
                        continue
                    else:
                        print('\033[31mЯ не знаю такой команды\033[0m')
                        continue
                break
        elif genre.lower() == 'детектив':
            while True:
                print('\033[35m', random.choice(film_detective), '\033[0m', sep='')
                while True:
                    choice = str(input('Еще раз или выйти? '))
                    if choice.lower() == 'выйти':
                        break
                    elif choice.lower() == 'еще раз' or choice.lower() == 'ещё раз':
                        print('\033[35m', random.choice(film_detective), '\033[0m', sep='')
                        continue
                    else:
                        print('\033[31mЯ не знаю такой команды\033[0m')
                        continue
                break
        elif genre.lower() == 'криминал':
            while True:
                print('\033[35m', random.choice(film_criminal), '\033[0m', sep='')
                while True:
                    choice = str(input('Еще раз или выйти? '))
                    if choice.lower() == 'выйти':
                        break
                    elif choice.lower() == 'еще раз' or choice.lower() == 'ещё раз':
                        print('\033[35m', random.choice(film_criminal), '\033[0m', sep='')
                        continue
                    else:
                        print('\033[31mЯ не знаю такой команды\033[0m')
                        continue
                break
        elif genre.lower() == 'мультфильм':
            while True:
                print('\033[35m', random.choice(film_mult), '\033[0m', sep='')
                while True:
                    choice = str(input('Еще раз или выйти? '))
                    if choice.lower() == 'выйти':
                        break
                    elif choice.lower() == 'еще раз' or choice.lower() == 'ещё раз':
                        print('\033[35m', random.choice(film_mult), '\033[0m', sep='')
                        continue
                    else:
                        print('\033[31mЯ не знаю такой команды\033[0m')
                        continue
                break
        elif genre.lower() == 'фэнтези':
            while True:
                print('\033[35m', random.choice(film_fantasy), '\033[0m', sep='')
                while True:
                    choice = str(input('Еще раз или выйти? '))
                    if choice.lower() == 'выйти':
                        break
                    elif choice.lower() == 'еще раз' or choice.lower() == 'ещё раз':
                        print('\033[35m', random.choice(film_fantasy), '\033[0m', sep='')
                        continue
                    else:
                        print('\033[31mЯ не знаю такой команды\033[0m')
                        continue
                break
        elif genre.lower() == 'боевик':
            while True:
                print('\033[35m', random.choice(film_boevik), '\033[0m', sep='')
                while True:
                    choice = str(input('Еще раз или выйти? '))
                    if choice.lower() == 'выйти':
                        break
                    elif choice.lower() == 'еще раз' or choice.lower() == 'ещё раз':
                        print('\033[35m', random.choice(film_boevik), '\033[0m', sep='')
                        continue
                    else:
                        print('\033[31mЯ не знаю такой команды\033[0m')
                        continue
                break
        else:
            print('\033[31mЯ не знаю такого жанра\033[0m')

    elif question.lower() == 'разбор слова':
        glas = 'аяуюоеёэиы'  # список с гласными буквами
        sogl = 'бвгджзйклмнпрстфхцчшщ'  # список с согласными буквами
        word = str(input('Введите слово: '))
        sogl_count = len([letter for letter in word if letter.lower() in sogl])
        glas_count = len([letter for letter in word if letter.lower() in glas])
        if (glas_count+sogl_count) != len(word):
            print('\033[31mПоддерживаются только русские буквы\033[0m')
        else:
            print('Всего букв:\033[35m', glas_count + sogl_count)
            print('\033[0mГласных букв:\033[35m', glas_count)
            print('\033[0mСогласных букв: \033[35m', sogl_count, '\033[0m', sep='')

    elif question.lower() == 'брось кубик':
        cube = [1, 2, 3, 4, 5, 6]
        print(random.choice(cube))  # выводит случайное число от 1 до 6

    elif question.lower() == 'подбрось монетку':
        coin = ['Орел', 'Решка']
        print(random.choice(coin))

    elif question.lower() == 'хватит' or question.lower() == 'стоп' or question.lower() == 'пока':  # слова для
        # отключения помощника
        print('До встречи!')
        break

    else:
        stop = ['«Хватит»', '«Стоп»', '«Пока»']
        print('\033[31mТакой команды нет.\033[0m Напиши «Команды», чтобы узнать список команд '
              'или ' + random.choice(stop) + ', чтобы '
                                             'закончить.')  # выводит ошибку, если введенная команда не поддерживается
