import subprocess, sys
try:
    import ezztui
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'ezztui'])
    import ezztui

massivmenu = {
    'Управление массивами': {
        'Создать массив': 'ezztui_return_value',
        'Выбрать текущий массив': 'ezztui_return_value',
        'Удалить массив': 'ezztui_return_value',
        'Управление постоянными массивами': {
            'Сохранить массивы на диск': 'ezztui_return_value',
            'Загрузить массивы с диска': 'ezztui_return_value',
            'Назад': 'ezztui_back_value'
        },
        'Назад': 'ezztui_back_value'
    },
    'Заполнение массивов': {
        'Заполнить массив случайными числами': 'ezztui_return_value',
        'Заполнить массив по заданному интервалу': 'ezztui_return_value',
        'Заполнить массив вручную': 'ezztui_return_value',
        'Назад': 'ezztui_back_value'
    },
    'Вывод массивов': {
        'Вывести массив по одному элементу': 'ezztui_return_value',
        'Вывести массив одной строчкой': 'ezztui_return_value',
        'Вывести массив как список': 'ezztui_return_value',
        'Назад': 'ezztui_back_value'
    }
}

choice = ezztui.menu(massivmenu)
