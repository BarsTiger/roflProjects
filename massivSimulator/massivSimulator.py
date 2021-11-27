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
    from progress.bar import ChargingBar
except:
    os.system(sys.executable + " -m pip install " + "progress")
    from progress.bar import ChargingBar

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
    print('Назовите массив.\n'
          'Придумывайте основательное и глубокое название.\n'
          'Не делайте название на 70 слайдов, ведь его сложно прочитать\n')
    name = input('Введите название: ')
    massives[name] = []
    current = name
    input("Массив " + name + " создан! Сейчас он пустой. Вы можете заполнить его")

def choose_current():
    global massives
    global current
    massives_menu = {}
    for massive in list(massives):
        massives_menu[massive] = 'ezztui_return_value'
    try:
        current = ezztui.menu(massives_menu)[0]
    except:
        print("Что-то не так. Возможно, у вас нет массивов")

def clear():
    global massives
    massives_menu = {}
    for massive in list(massives):
        massives_menu[massive] = 'ezztui_return_value'
    toclear = ezztui.menu(massives_menu)[0]
    massives[toclear] = []

def delete():
    global massives
    massives_menu = {}
    for massive in list(massives):
        massives_menu[massive] = 'ezztui_return_value'
    toclear = ezztui.menu(massives_menu)[0]
    massives.pop(toclear)

def save_disk(mode):
    global massives
    if mode == 'merge':
        try:
            massivesread = open('смачний.шматочок', 'r')
            massives_disk = json.load(massivesread)
            to_dump = massives | massives_disk
            massivesread.close()
            massiveswrite = open('смачний.шматочок', 'w+')
            json.dump(to_dump, massiveswrite, indent=3)
            massiveswrite.close()
        except:
            massiveswrite = open('смачний.шматочок', 'w+')
            json.dump(massives, massiveswrite, indent=3)
            massiveswrite.close()
    else:
        massiveswrite = open('смачний.шматочок', 'w+')
        json.dump(massives, massiveswrite, indent=3)
        massiveswrite.close()

def read_disk(mode):
    global massives
    massivesfile = open('смачний.шматочок', 'r')
    try:
        if mode == 'merge':
            massives |= json.load(massivesfile)
        else:
            massives = json.load(massivesfile)
    except:
        massives = massives
    massivesfile.close()

def fill_random():
    global massives
    global current
    global fill_mode
    needlen = None
    while needlen == None:
        try:
            needlen = int(input('Введите, сколько элементов массива нужно создать и засунуть ♂deep♂ в массив: '))
        except:
            print("Введите число и не ломайте программу, я ее мозгами писал")
    minint = None
    while minint == None:
        try:
            minint = int(input('Введите, каким минимально должно быть случайное число: '))
        except:
            print("Введите число и не ломайте программу, я ее мозгами писал")
    maxint = None
    while maxint == None:
        try:
            maxint = int(input('Введите, каким максимально должно быть случайное число: '))
        except:
            print("Введите число и не ломайте программу, я ее мозгами писал")
    try:
        if fill_mode == 'replace':
            massives[current] = []
        zapoln_bar = ChargingBar('Заполнение массива', max=needlen)
        for i in range(needlen):
            massives[current].append(random.randint(minint, maxint))
            zapoln_bar.next()
        input("\nМассив заполнен")
    except:
        input("Что-то сломалось. Скорее всего, у вас нет массивов")

def fill_interval():
    global massives
    global current
    global fill_mode
    needlen = None
    while needlen == None:
        try:
            needlen = int(input('Введите, сколько элементов массива нужно создать и засунуть ♂deep♂ в массив: '))
        except:
            print("Введите число и не ломайте программу, я ее мозгами писал")
    maxint = None
    while maxint == None:
        try:
            maxint = int(input('Введите, от какого числа будет заполняться массив: '))
        except:
            print("Введите число и не ломайте программу, я ее мозгами писал")
    minint = None
    while minint == None:
        try:
            minint = int(input('Введите, до какого числа будет заполняться массив: '))
        except:
            print("Введите число и не ломайте программу, я ее мозгами писал")
    interval = None
    while interval == None:
        try:
            interval = int(input('Введите интервал между числами: '))
        except:
            print("Введите число и не ломайте программу, я ее мозгами писал")

    try:
        if fill_mode == 'replace':
            massives[current] = []
        zapoln_bar = ChargingBar('Заполнение массива', max=needlen)
        prev = minint - interval
        for i in range(needlen):
            massives[current].append(prev + interval)
            prev += interval
            zapoln_bar.next()
        input("\nМассив заполнен")
    except:
        input("Что-то сломалось. Скорее всего, у вас нет массивов")


def fill_user():
    global massives
    global current
    global fill_mode
    needlen = None
    while needlen == None:
        try:
            needlen = int(input('Введите, сколько элементов массива вы будете вводить и программа засунет их ♂deep♂ в массив: '))
        except:
            print("Введите число и не ломайте программу, я ее мозгами писал")
    try:
        if fill_mode == 'replace':
            massives[current] = []
        for i in range(needlen):
            add_this = None
            while add_this == None:
                try:
                    add_this = int(input())
                except:
                    print("Введите число и не ломайте программу, я ее мозгами писал")
            massives[current].append(add_this)
        input("Массив заполнен")
    except:
        input("Что-то сломалось. Скорее всего, у вас нет массивов")

def sum_massives():
    global massives
    global current
    input('Нажмите Enter, чтобы выбрать первый массив')
    massives_menu = {}
    for massive in list(massives):
        massives_menu[massive] = 'ezztui_return_value'
    first = ezztui.menu(massives_menu)[0]
    input('Нажмите Enter, чтобы выбрать второй массив')
    second = ezztui.menu(massives_menu)[0]
    print('Назовите новый массив.\n'
          'Напомним, придумывайте основательное и глубокое название.\n'
          'Не делайте название на 70 слайдов, ведь его сложно прочитать\n')
    name = input('Введите название: ')
    massives[name] = massives[first] + massives[second]


def guess_game():
    input('Это игра "угадай массив"\n'
          'Тут вы должны угадать массив, зная его длину\n'
          'Потом вы увидите совпадение с оригинальным массивом в процентах\n'
          'Порядок в массиве не считается')
    length = random.randint(5, 10)
    input("Ваша задача ввести массив из " + str(length) + " чисел от 0 до 100")
    generated = list()
    for i in range(length):
        generated.append(random.randint(0, 100))
    users = list()
    for i in range(length):
        add_this = None
        while add_this == None:
            try:
                add_this = int(input("Введите число: "))
            except:
                print("Введите число и не ломайте программу, я ее мозгами писал")
        users.append(add_this)
    input("Ваш массив заполнен! Пришло время узнать, насколько вы ванга")
    print("Наш массив - " + str(generated))
    sovpalo = len(list(set(users) & set(generated)))
    percent = (sovpalo/length) * 100
    print("В двух массивах совпало " + str(sovpalo) + "! Это около " + str(percent) + "%")
    input("Чё, ванга?" if percent >= 70 else "Немного не угадал" if percent >= 50 else "Меньше половины" if percent >= 30 else "Не ванга")


def sum_game():
    input('Это игра "посчитай сумму"\n'
          'Тут вы должны сложить все элементы массива и ввести сумму\n'
          'Потом вы увидите правильный ответ')
    length = random.randint(5, 10)
    input("Ваша задача сложить массив из " + str(length) + " чисел от 0 до 10")
    generated = list()
    for i in range(length):
        generated.append(random.randint(0, 10))
    real_sum = sum(generated)
    usr_sum = None
    print(generated)
    while usr_sum == None:
        try:
            usr_sum = int(input("Сложите все числа и введите число: "))
        except:
            print("Введите число и не ломайте программу, я ее мозгами писал")
    print("Правильный ответ - " + str(real_sum))
    input("Ты победил! Ответ правильный!" if usr_sum == real_sum else "Ответ неправильный(")

def about():
    ezztui.center_message("©KOTIKOT, script by BarsTiger")
    ezztui.center_multiline(["Симулятор заполнения массива",
                             "Собрано по крупицам на Python 3.9, меню основано на ezztui (by BarsTiger)",
                             "За перевод и локализацию спасибо KorvusTeam",
                             "По вопросам насчет заполнения массивов пишите на почту entin@dlit.dp.ua",
                             "Остальные вопросы задавайте по адресу kozlova_t@dlit.dp.ua",
                             "Пожалуйста, не задавайте потусторонних вопросов о сухариках"])

def korvusTeam():
    ezztui.center_multiline(["Спасибо KorvusTeam за русскую локализацию!",
                             "Она была собрана по крупицам командой Korvus",
                             "Перевод максимально основательный, глубокий и многосторонний",
                             "Вы можете заказать переводы для своих приложений у Korvus"])

ezztui.center_multiline(['  .......... .....  .....   ......  ...........  .....   ..........  .......................  ..........  ............',
                         ' .@BBBBBBBBS.SBBBB* BBBBB.  SBBBB&!!@BBBBB&BBB# .@BBB&. !#BBBBBBBB# *#BBBBBBBBBB#SBBBBBBBBB% *#BBBBBBBBS$ %BBBBBBBBBB@.',
                         ' %BBBBBBBBB@ &BBBB* BBBBB  .#BBBB@**@BBBBS%SBB#.*@BBB$  %BBBBBBBBB@ &BBBBBSBBBBB$@BBBBBBBS@! #BBBBBSBBBBB !BBBBBSBBBBB%',
                         ' *BBBB&      &BBS$%@BBBBB  !#BBBB&$$&BBBB&.&BB#!$#BBS!  $BBB%@BBBB& @BBBB. SBBBB.  &BBBB*    &BBBB! BBBBB !BBBB@ @BBBB*',
                         ' *BBBB&      &BB#%#BBBBBB  *#BBBBB##SBBBB#*$SBS@SBBS%. !@BBB!%BBBB& &BBBB* BBBBB   &BBBB*    &BBBB! BBBBB !BBBB@ @BBBB*',
                         ' *BBBB&      &BBBSBBSSBBB  %#BBBSBBBBSBBB#*!*BBBBBB#.  *&BBB.%BBBB& @BBBBBBBBBBB.  &BBBB%    &BBBB! BBBBB !BBBBS@SBBBB%',
                         ' *BBBB&      &BBBBBS$&BBB  @SBB#%#BB#%#BBS$. SBBBBB@   SBBBB *BBBB& .$BBBBBBBBBB.  &BBBB%    &BBBB! BBBBB !BBBBBBBBBBS*',
                         ' *BBBB&      &BBBB&%%&BBB  @SBB#!#BB#!#BBB&. *&BBB@!  !BBBB# !BBBB&  %BBB$*BBBBB.  &BBBB*    &BBBB! BBBBB !BBBB#!!!*!.',
                         ' %BBBBBBBBB& &BBBB* SBBBB !BBBB&.&BB&.&BBBB* *&BBB*  .%BBBS@ *BBBB& @BBBB* BBBBB.  &BBBB%    #BBBBBSBBBBB !BBBB&      ',
                         ' !&BBBBBBBBS.SBBBB* BBBBB %BBBBS.SBBS.SBBBB% @BBBB.  !@BBB#% %BBBB# #BBBB! BBBBB.  SBBBB$    %#BBBBBBBBB$ %BBBBS      ',
                         '',
                         '              .BBBBB%.!SBBBB$  .%BBBBBBB@!   $SBBBBBBBB*!@BBBBBBBBS.SBBBB* BBBBB *BBBBBBBBBB@. *#BBBBBB#*             ',
                         '              *BBBBB%**#BBBB$  .$SBBBBBB#%  .BBBBBBBBBS.%BBBBBBBBB@ &BBBB* BBBBB !BBBBBSBBBBB% %&BBBBBBS@             ',
                         '             .*BBBBB@$$SBBBB$. !#BB###BBB@  .BBBBB      *BBBB&      &BBS$%@BBBBB !BBBB$ $BBBB* &SBS##SBB#             ',
                         '             .%BBBBBS##BBBBB@! %BBB@$$SBB#  .BBBBB      %BBBB&      &BB#%#BBBBBB !BBBB#!#BBBB! BBB&$$&BBB.            ',
                         '             !$BBBSSBBBBSBBB@! %BBB@%*#BB#.  BBBBB.     %BBBB&      &BBBSBBSSBBB !BBBBBBBBB&! .BBB&%*@BBB*            ',
                         '             *&BBB@$BBB@$BBB#%!$BBBS##BBB#!  BBBBB      %BBBB&      &BBBBBS$&BBB !BBBB#%#BBS#*!BBBBS#SBBB%.           ',
                         '             *&BBB$*BBB$*BBB#$!$BBBBBBBBBS%  BBBBB      *BBBB&      &BBBB&%%&BBB !BBBB@ @BBBB$!BBBBBBBBBB@!           ',
                         '             &BBBB%!BBB%!BBBBB$&BBB%!!#BBS@. BBBBBBBBBS.%BBBBBBBBB& &BBBB* SBBBB !BBBBBSBBBBB&$BBB@!!$BBB&%           ',
                         '             SBBBB$!BBB$!BBBBB#SBBB* .SBBB#! @BBBBBBBBB*!&BBBBBBBBS.SBBBB* BBBBB *BBBBBBBBBB&@#BBB@  @BBBS$           ',
                         '             ...... .... ..........   .....  ..........  .......... .....  .....  .................  ......           ',
                         '                                      Спасибо KorvusTeam за перевод на русский                                        '])
ezztui.cls()

while True:
    choice = ezztui.menu(massivmenu)
    if choice[0] == 'Управление массивами':
        if choice[1] == 'Создать массив':
            ezztui.cls()
            create_massive()
        elif choice[1] == 'Выбрать текущий массив':
            ezztui.cls()
            choose_current()
            input("Теперь вы работаете с массивом " + current)
        elif choice[1] == 'Очистить массив':
            ezztui.cls()
            clear()
            input("Массив очищен")
        elif choice[1] == 'Удалить массив':
            ezztui.cls()
            delete()
            input("Массив удален")
        elif choice[1] == 'Управление основательными массивами':
            if choice[2] == 'Сохранить массивы глубоко на диск':
                ezztui.cls()
                save_disk('replace' if choice[3] == 'Сохранить с заменой' else 'merge')
                input("Закладка массива произошла")
            if choice[2] == 'Срезик массивов с диска':
                ezztui.cls()
                read_disk('replace' if choice[3] == 'Срезик с заменой' else 'merge')
                input("Закладку массива нашли и используют в металлургии")

    elif choice[0] == 'Заполнение массивов':
        if choice[1] == 'Режим заполнения':
            ezztui.cls()
            fill_mode = 'add' if choice[2] == 'Добавление' else 'replace'
            print('Используется метод "' + choice[2] + '" при заполнении')
            input()
        elif choice[1] == 'Заполнить массив случайными числами':
            ezztui.cls()
            fill_random()
        elif choice[1] == 'Заполнить массив по заданному интервалу':
            ezztui.cls()
            fill_interval()
        elif choice[1] == 'Заполнить массив вручную по крупицам':
            ezztui.cls()
            fill_user()

    elif choice[0] == 'Вывод массивов':
        if choice[1] == 'Вывести массив по одному элементу':
            ezztui.cls()
            try:
                for i in massives[current]:
                    print(i)
                input()
            except:
                print("Возможно, у вас нет массивов или еще что-то не так")
                input("Не ломайте прогу, я ее по крупицам писал")
        elif choice[1] == 'Вывести массив одной строчкой':
            ezztui.cls()
            try:
                massiveline = ''
                for i in massives[current]:
                    massiveline += str(i) + " "
                print(massiveline)
                input()
            except:
                print("Возможно, у вас нет массивов или еще что-то не так")
                input("Не ломайте прогу, я ее по крупицам писал")
        elif choice[1] == 'Вывести массив как список':
            ezztui.cls()
            try:
                print(massives[current])
                input()
            except:
                print("Возможно, у вас нет массивов или еще что-то не так")
                input("Не ломайте прогу, я ее по крупицам писал")

    elif choice[0] == 'Действия с массивами':
        if choice[1] == 'Сложение массивов':
            ezztui.cls()
            sum_massives()
        elif choice[1] == 'Перемешать массив':
            ezztui.cls()
            try:
                random.shuffle(massives[current])
                input('Кристалічну ґратку массива зруйновано')
            except:
                print("Возможно, у вас нет массивов или еще что-то не так")
                input("Не ломайте прогу, я ее по крупицам писал")
        elif choice[1] == 'Отсортировать массив':
            ezztui.cls()
            try:
                if choice[2] == 'По возрастанию':
                    massives[current] = sorted(massives[current])
                elif choice[2] == 'По убыванию':
                    massives[current] = sorted(massives[current], reverse=True)
                input('Кристалічну ґратку массива відновлено')
            except:
                print("Возможно, у вас нет массивов или еще что-то не так")
                input("Не ломайте прогу, я ее по крупицам писал")

    elif choice[0] == 'Игры':
        if choice[1] == 'Игра "угадай массив"':
            ezztui.cls()
            guess_game()
        elif choice[1] == 'Игра "посчитай сумму" - на развитие толковейшей головы':
            ezztui.cls()
            sum_game()

    elif choice[0] == 'О программе':
        ezztui.cls()
        about()

    elif choice[0] == 'Выход' and choice[1] == 'KorvusTeam':
        ezztui.cls()
        korvusTeam()
