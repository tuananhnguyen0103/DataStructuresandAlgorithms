# Độ khó: ⭐
# Mô tả:
# Cho mảng số nguyên, hãy tính tổng tất cả các phần tử.

# Input: [1, 2, 3, 4, 5]
# Output: 15

# Yêu cầu:

# Tự viết vòng lặp, không dùng sum() (nếu Python).

import numpy as np
import random
arr_ex1 = [random.randint(0, 100) for _ in range(10)]
print(type(len(arr_ex1)))
sum_arr = 0
for i in range (len(arr_ex1)):
    sum_arr += arr_ex1[i]
print(arr_ex1)
print(sum(arr_ex1))
print(sum_arr)