b_year = int(input('Знаете ли Вы год рождения А.С.Пушкина? Введите в формате ХХХХ: '))     # 1799
while True:
    if b_year != 1799:
        b_year = int(input('Неверно! Введите год рождения А.С.Пушкина еще раз: '))
    else:
        b_day = input('Знаете ли Вы день рождения А.С.Пушкина? Введите в формате ХХ.ХХ: ') # 06.06
        while True:
            if b_day == '06.06' or b_day == '6 июня' or b_day == '06 июня':
                break
            else:
                b_day = input('Неверно! Введите день рождения А.С.Пушкина еще раз: ')
        break
print('Верно!')