st = int(input("Укажите количество студентов:  "))
date = {}
n = 0  # сумма всех оценок

for i in range(st):
    nam = input("Введите имя студента:  ")
    bl = int(input("Укажите его балл:  "))
    date[nam] = bl
    n += bl

m = n / st  # ср ариф

for i in date:
    t = 1
    print(t, "-й студент: ", i)
    print("Балл:", date[i])
    t += 1

print("Средний балл:", m, "  Студенты с баллом выше среднего:")
for i in date:
    if date[i] > m:
        print(i)
