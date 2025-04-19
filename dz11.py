def srarif(fn):
    def sr(*args):
        s = fn(*args) / len(args)
        return s

    return sr


@srarif
def summa(*args):
    return sum(args)


print(summa(1, 3, 2, 1))
