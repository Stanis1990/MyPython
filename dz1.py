num = 97531
val1 = num % 10
num = num // 10
val10 = num % 10
num = num // 10
val100 = num % 10
num = num // 10
val1000 = num % 10
num = num // 10
val10000 = num % 10

print("Произведение цифр:", (val1 * val10 * val100 * val1000 * val10000))
print("Среднее арифметическое цифр:", (val1 + val10 + val100 + val1000 + val10000) / 5)
