# Mô tả:
# Cho mảng số nguyên, hãy tìm max của mảng.

# Input: [1, 2, 3, 4, 5]
# Output: 5

# Input: [11,45,123,124,65]
# Output: 124


# Yêu cầu:

# Tự viết vòng lặp, không dùng sum() (nếu Python).
import numpy as np
import random
arr_ex2 = [random.randint(0, 100) for _ in range(10)]
print(type(len(arr_ex2)))
print(arr_ex2)
max_temp = arr_ex2[0]
for i in (arr_ex2):
    if i > max_temp:
        max_temp = i
print(max_temp)
print(max(arr_ex2))
        