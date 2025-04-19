n = int(input("Введите к-во символов:  "))
m = input("Введите символ:  ")
k = int(input("Введите 0 если горизонтально и 1 если вертикально:  "))

if k == 0:
    while n >= 0:
        print(m, end="")
        n = n - 1
elif k == 1:
    while n >= 0:
        print(m)
        n = n - 1
else:
    print("Что-то пошло не так")
