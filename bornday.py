#МОДУЛЬ 3

year_pyshkin = 1799  #др Пушкина
day_pushkin = 6

year_users = int(input('Введите год рождения А.С. Пушкина: '))

if year_pyshkin == year_users:
    day_user=int(input('Введите день рождения А.С. Пушкина:  '))
    if day_user==day_pushkin:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')

