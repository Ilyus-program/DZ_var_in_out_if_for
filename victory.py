count_r = 0     # количество правильных ответов
per_count_r = 0 # процент правильных ответов
count_f = 0     # количество неправильных ответов
per_count_f = 0 # процент неправильных ответов
count = 0       # количество вопросов

while True:
    b_Newton = int(input('Знаете ли Вы год рождения И.Ньютона? Введите в формате ХХХХ: ')) # 1643
    if b_Newton == 1643:
        count_r += 1
    else:
        count_f += 1
    count += 1
    b_Einstein = int(input('Знаете ли Вы год рождения А.Эйнштейна? Введите в формате ХХХХ: '))  # 1879
    if b_Einstein == 1879:
        count_r += 1
    else:
        count_f += 1
    count += 1
    b_Galileo = int(input('Знаете ли Вы год рождения Г.Галилео? Введите в формате ХХХХ: '))  # 1564
    if b_Galileo == 1564:
        count_r += 1
    else:
        count_f += 1
    count += 1
    b_Lomonosov = int(input('Знаете ли Вы год рождения М.В.Ломоносова? Введите в формате ХХХХ: '))  # 1749
    if b_Lomonosov == 1749:
        count_r += 1
    else:
        count_f += 1
    count += 1
    b_Mendeleev = int(input('Знаете ли Вы год рождения Д.И.Менделеева? Введите в формате ХХХХ: '))  # 1834
    if b_Mendeleev == 1834:
        count_r += 1
    else:
        count_f += 1
    count += 1
    per_count_r = int(count_r / count * 100)
    per_count_f = int(count_f / count * 100)
    print('Количество правильных ответов: ', count_r)
    print('Количество ошибок: ', count_f)
    print('Процент правильных ответов: ', per_count_r, ' %')
    print('Процент неправильных ответов: ', per_count_f, ' %')
    rep = input('Хотите ли начать игру сначала (y/n): ')
    if rep == 'y' or rep == 'н':
        count_r = 0
        per_count_r = 0
        count_f = 0
        per_count_f = 0
        count = 0
    else:
        break
