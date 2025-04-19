lst = {
    "John": {"N": 3056, "S": 8463, "E": 2694, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
}

for i in lst:
    print(i)
    for j in lst[i]:
        print(j, lst[i][j])

nm = input("Введите имя сотрудника:  ")
reg = input("Укажите регион (N,S,E,W):  ")

if nm in lst and reg in lst[nm]:
    mon = lst[nm][reg]
    print("Текущий уровень продаж сотрудника ", nm, " по региону ", reg, " составляет: ", mon)
    nw = int(input("Для обновления значения продаж введите новое число:  "))
    lst[nm][reg] = nw
    print(lst[nm])
else:
    print("Одно или несколько значений введены неверно")
