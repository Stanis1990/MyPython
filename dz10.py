# Локальная реализация
def p1(a, b, c):
    def vv(a, b, c):
        x1 = a * b
        x2 = a * c
        x3 = b * c
        s = (x1 + x2 + x3) * 2
        return s

    z = vv(a, b, c)
    return (z)


print(p1(2, 4, 6))


# Глобальная реализация

def p2(a, b, c):
    def vv2(a, b, c):
        x1 = a * b
        x2 = a * c
        x3 = b * c
        s = (x1 + x2 + x3) * 2
        return s

    z1 = vv2(a, b, c)
    return z1


s_glob = p2(5, 8, 2)
print(s_glob)


# Что-то среднее

def p3(a, b, c):
    s = 0

    def vv3(a, b, c):
        nonlocal s
        x1 = a * b
        x2 = a * c
        x3 = b * c
        s = (x1 + x2 + x3) * 2

    vv3(a, b, c)

    return s


print(p3(1, 6, 8))
