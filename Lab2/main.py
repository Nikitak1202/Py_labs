from csv import reader
from random import randint


flag = 0
ind = 0
output = open('result.txt', 'w')
search = input('Search for: ')
counter_longer_30 = 0
authors_books = []
rand_indexes = []
popular = []
publishers = set()


for i in range(20):
    rand_indexes.append(randint(1, 9410))


with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if row[5] == "25":
            popular.append(row[1])
        publishers.add(row[4])
        if len(row[1]) > 30:
            counter_longer_30 += 1
        lower_case = row[2].lower()
        row[6] = row[6].replace(',', '.')
        if search.lower() == lower_case and float(row[6]) < 150:
            authors_books.append(row[1])
            flag = 1
        if ind in rand_indexes:
            output.write(f'{row[2]}. {row[1]} - {row[3]}\n')
        ind += 1
output.close()


print("Задание 1: " + str(counter_longer_30) + "\n")

print("Задание 2:")
if flag == 0:
    print('Nothing found.')
else:
    for book in authors_books:
        print(book)
print("\n")

print("Задание 3: Проверьте файл result.txt))\n")

'''
print("Дополнительное задание 1:")
for publisher in publishers:
    print(publisher)
print("\n")'''

print("Дополнительное задание 2:")
for book in popular[:20]:
    print(book)