import sys, time
from calculator import calculator

if len(sys.argv) != 2:
    print('Вы не указали имя файла в командрной строке!')
else:
    validator = calculator()
    start = time.perf_counter()
    f = open(sys.argv[1], 'r')

    data = f.readlines()
    data = [int(i) for i in data]
    f.close()

    print(data)
    print(validator.minimum(data))
    print(validator.maximum(data))
    print(validator.sum_numbers(data))
    print(validator.multiplication_numbers(data))
    print("Время работы = {}".format(time.perf_counter() - start))
