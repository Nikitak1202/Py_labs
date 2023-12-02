import colorama


colorama.init()
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
REPEATS = 2


for i in range(6):
    print(f'{BLUE}{"  " * 3}{WHITE}{"  " * 3}{RED}{"  " * 3}{END}')
print(2*"\n")


for repeat in range(REPEATS):
    for i in range(9):
        if i > 2 and i < 6:
            print(f'{WHITE}{"  " * 3}{END}{"  " * 3}{WHITE}{"  " * 3}{END}')
        else:
            print(f'{"  " * 3}{WHITE}{"  " * 3}{END}{"  " * 3}')
    print(2*"\n")


plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i ** 2

step = round(abs(result[0] - result[9]) / 9, 2)
print(step)

for i in range(10):
    plot_list[i][0] = step * (8-i) + step

for i in range(9):
    for j in range(1, 10):
        if plot_list[i][0] == result[j]:
            plot_list[i][j] = 1
        elif (result[j] > plot_list[i][0]) and (result[j] < plot_list[i-1][0]):
            plot_list[i][j] = 1
plot_list[8][1] = 1
plot_list[8][2] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '-\t'
        if plot_list[i][j] == 1:
            line += '*\t'
    print(line)
print('\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9')


file = open('sequence.txt', 'r')
counter = 0
plus = 0
minus = 0
for number in file:
    num = float(number[:-1])
    if num < 0:
        minus += 1
    else:
        plus += 1
    counter += 1
file.close()
min_pers = (minus / counter) * 100
plus_pers = (plus / counter) * 100
print("Отрицательных: " + str(min_pers) + "%")
print("Положительных: " + str(plus_pers) + "%")
print("Всего чисел: " + str(counter))