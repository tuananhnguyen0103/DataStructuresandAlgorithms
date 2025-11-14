# 🧩 Bài 3 – Đếm số lần xuất hiện của 1 phần tử

# Đếm số lần xuất hiện của số x.

# Input 
# arr = [1, 2, 1, 3, 1]
# x = 1

# Output
# 3

# Input 
# arr = [5, 7, 5, 2, 5, 9]
# x = 5

# Output
# 3

import numpy as np
import random
arr_ex3 = [random.randint(0, 100) for _ in range(10)]
arr_ex3 = [123, 123, 344, 51, 51, 1354, 51, 12, 75, 41, 65]
# print(type((arr_ex3)))
print(arr_ex3)

random_value = random.choice(arr_ex3)
print(random_value)
count_x = 0
for i in arr_ex3:
    if i == random_value:
        count_x +=1
print(count_x)
print(arr_ex3.count(random_value))
