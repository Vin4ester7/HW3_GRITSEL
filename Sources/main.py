import sys, time
from calculator import calculator

if len(sys.argv) != 2:
    print('Вы не указали имя файла в командной строке!')
else:
    validator = calculator()
    start = time.perf_counter()
    f = open(sys.argv[1], 'r')

    data = f.readlines()
    data = [int(i) for i in data]
    f.close()

    file = ''
    for number in data:
        file += str(number)
        file += ' '

    if len(data) > 0:
        print(f'В файле: {file}')
        print(f'Минимум: {validator.minimum(data)}')
        print(f'Максимум: {validator.maximum(data)}')
        print(f'Сумма: {validator.sum_numbers(data)}')
        print(f'Произведение: {validator.multiplication_numbers(data)}')
        print("Время работы = {}".format(time.perf_counter() - start))
    else:
        print('Нет данных.')
