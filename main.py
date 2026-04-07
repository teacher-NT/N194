import os
os.system('cls')
import math

# print(math.pow(2,3), 2**3)

# print(math.sqrt(25))

# print(math.log2(64))
# print(math.log(625, 5))

# print(math.floor(4.99))
# print(math.ceil(4.12))
# print(round(4.99), round(4.12))


import random as rd

# a = rd.uniform(1,10)
# print(a)

names = ['Ali', 'Vali', 'Xasan',  'Xusan']
# n = rd.choice(names)
# print(n)

# n = rd.choices(names,k=2)
# print(n)

# n = rd.sample(names, k=2)
# print(n)

rd.shuffle(names)
print(names)
