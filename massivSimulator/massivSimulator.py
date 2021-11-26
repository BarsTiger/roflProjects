import os
import sys
import json
import pprint
import random
try:
    import ezztui
except:
    os.system(sys.executable + " -m pip install " + "ezztui")
    import ezztui
try:
    import progressbar
except:
    os.system(sys.executable + " -m pip install " + "progressbar")
    import progressbar

massivmenu = {
    'Управление массивами': {
        'Создать массив': 'ezztui_return_value',
        'Выбрать текущий массив': 'ezztui_return_value',
        'Очистить массив': {
            'Очистить': 'ezztui_return_value',
            'Назад': 'ezztui_back_value'
        },
        'Удалить массив': {
            'Удалить': 'ezztui_return_value',
            'Назад': 'ezztui_back_value'
        },
        'Управление основательными массивами': {
            'Сохранить массивы глубоко на диск': {
                'Сохранить с заменой': 'ezztui_return_value',
                'Сохранить с объединением': 'ezztui_return_value',
                'Назад': 'ezztui_back_value'
            },
            'Срезик массивов с диска': {
                'Срезик с заменой': 'ezztui_return_value',
                'Срезик с объединением': 'ezztui_return_value',
                'Назад': 'ezztui_back_value'
            },
            'Назад': 'ezztui_back_value'
        },
        'Назад': 'ezztui_back_value'
    },
    'Заполнение массивов': {
        'Режим заполнения': {
            'Замена': 'ezztui_return_value',
            'Добавление': 'ezztui_return_value',
            'Назад': 'ezztui_back_value'
        },
        'Заполнить массив случайными числами': 'ezztui_return_value',
        'Заполнить массив по заданному интервалу': 'ezztui_return_value',
        'Заполнить массив вручную по крупицам': 'ezztui_return_value',
        'Назад': 'ezztui_back_value'
    },
    'Вывод массивов': {
        'Вывести массив по одному элементу': 'ezztui_return_value',
        'Вывести массив одной строчкой': 'ezztui_return_value',
        'Вывести массив как список': 'ezztui_return_value',
        'Назад': 'ezztui_back_value'
    },
    'Действия с массивами': {
        'Сложение массивов': 'ezztui_return_value',
        'Перемешать массив': 'ezztui_return_value',
        'Отсортировать массив': {
            'По возрастанию': 'ezztui_return_value',
            'По убыванию': 'ezztui_return_value',
            'Назад': 'ezztui_back_value'
        },
        'Назад': 'ezztui_back_value'
    },
    'Игры': {
        'Игра "угадай массив"': 'ezztui_return_value',
        'Игра "посчитай сумму" - на развитие толковейшей головы': 'ezztui_return_value',
        'Назад': 'ezztui_back_value'
    },
    'О программе': 'ezztui_return_value',
    'Выход': {
        'Выход': 'ezztui_exit_value',
        'Назад': 'ezztui_back_value',
        'KorvusTeam': 'ezztui_return_value',
    }
}

massives = {}
current = ''
fill_mode = 'add'


def create_massive():
    global massives
    global current
    print('Назовите массив.'
          'Придумывайте основательное и глубокое название.'
          'Не делайте название на 70 слайдов, ведь его сложно прочитать')
    input('Введите название: ')

def choose_current():
    pass

def clear():
    pass

def delete():
    pass

def save_disk(mode):
    pass

def read_disk(mode):
    pass

def fill_random():
    global massives
    global current
    global fill_mode

def fill_interval():
    global massives
    global current
    global fill_mode

def fill_user():
    global massives
    global current
    global fill_mode

def sum_massives():
    global massives
    global current

def guess_game():
    pass

def sum_game():
    pass

def about():
    pass

def corvusTeam():
    pass

while True:
    choice = ezztui.menu(massivmenu)
    if choice[0] == 'Управление массивами':
        if choice[1] == 'Создать массив':
            create_massive()
        elif choice[1] == 'Выбрать текущий массив':
            choose_current()
            input("Теперь вы работаете с массивом " + current)
        elif choice[1] == 'Очистить массив':
            clear()
            input("Массив очищен")
        elif choice[1] == 'Удалить массив':
            delete()
            input("Массив удален")
        elif choice[1] == 'Управление основательными массивами':
            if choice[2] == 'Сохранить массивы глубоко на диск':
                save_disk('replace' if choice[3] == 'Сохранить с заменой' else 'merge')
                input("Закладка массива произошла")
            if choice[2] == 'Срезик массивов с диска':
                read_disk('replace' if choice[3] == 'Срезик с заменой' else 'merge')
                input("Закладку массива нашли и используют в металлургии")

    elif choice[0] == 'Заполнение массивов':
        if choice[1] == 'Режим заполнения':
            fill_mode = 'add' if choice[2] == 'Добавление' else 'replace'
            print('Используется метод "' + choice[2] + '" при заполнении')
            input()
        elif choice[1] == 'Заполнить массив случайными числами':
            fill_random()
        elif choice[1] == 'Заполнить массив по заданному интервалу':
            fill_interval()
        elif choice[1] == 'Заполнить массив вручную по крупицам':
            fill_user()

    elif choice[0] == 'Вывод массивов':
        if choice[1] == 'Вывести массив по одному элементу':
            try:
                for i in massives[current]:
                    print(i)
                input()
            except:
                print("Возможно, у вас нет массивов или еще что-то не так")
                input("Не ломайте прогу, я ее по крупицам писал")
        elif choice[1] == 'Вывести массив одной строчкой':
            try:
                massiveline = ''
                for i in massives[current]:
                    massiveline += str(i)
                print(massiveline)
                input()
            except:
                print("Возможно, у вас нет массивов или еще что-то не так")
                input("Не ломайте прогу, я ее по крупицам писал")
        elif choice[1] == 'Вывести массив как список':
            try:
                print(massives[current])
                input()
            except:
                print("Возможно, у вас нет массивов или еще что-то не так")
                input("Не ломайте прогу, я ее по крупицам писал")

    elif choice[0] == 'Действия с массивами':
        if choice[1] == 'Сложение массивов':
            sum_massives()
        elif choice[1] == 'Перемешать массив':
            try:
                random.shuffle(massives[current])
                input('Кристалічну ґратку массива зруйновано')
            except:
                print("Возможно, у вас нет массивов или еще что-то не так")
                input("Не ломайте прогу, я ее по крупицам писал")
        elif choice[1] == 'Отсортировать массив':
            try:
                massives[current] = sorted(massives[current], reverse=False if choice[1] == 'По возрастанию' else True)
                input('Кристалічну ґратку массива відновлено')
            except:
                print("Возможно, у вас нет массивов или еще что-то не так")
                input("Не ломайте прогу, я ее по крупицам писал")

    elif choice[0] == 'Игры':
        if choice[1] == 'Игра "угадай массив"':
            guess_game()
        elif choice[1] == 'Игра "посчитай сумму" - на развитие толковейшей головы':
            sum_game()

    elif choice[0] == 'О программе':
        about()

    elif choice[0] == 'Выход' and choice[1] == 'KorvusTeam':
        corvusTeam()
