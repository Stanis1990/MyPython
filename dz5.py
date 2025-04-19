import math
import random

lst1 = []
lst2 = []
max1 = 0

for i in range(10):
    lst1.append(random.randint(-10, 10))
print(lst1)

for i in lst1:
    if i > 0:
        lst2.append(i)
print(lst2)

for i in lst2:
    if i > max1:
        max1 = i
print(max1)
