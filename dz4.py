t = 0
k = 0
for i in range(5):
    m = int(input("Введите число:  "))
    t += 1
    if m != 0:
        k = m + k
x = k/t
print(x)
