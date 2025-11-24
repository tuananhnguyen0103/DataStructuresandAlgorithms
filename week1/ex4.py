# 🧩 Bài 4 – Đảo ngược mảng (2 con trỏ)

# Không dùng reverse().

# # 📥 Input mẫu 1:
# # [1, 2, 3, 4, 5]

# # 📤 Output mẫu 1:
# # [5, 4, 3, 2, 1]

# # 📥 Input mẫu 2:
# # [10, 20, 30]

# # 📤 Output mẫu 2:
# # [30, 20, 10]

# # 📥 Input mẫu 3:
# # [7]

# # 📤 Output mẫu 3:
# # [7]
# import random
# arr_ex4 = [random.randint(0, 100) for _ in range(5)]
# print(type(len(arr_ex4)))
# print(arr_ex4)

# left = 0
# right = 0

# for i in range(len(arr_ex4)):
#     left = i
#     right = len(arr_ex4) - i -1
#     arr_ex4_tmp = arr_ex4[i]
#     arr_ex4[i]=arr_ex4[right]
#     arr_ex4[right] = arr_ex4_tmp
#     if(left>=right):
#         break
#     print(left)
#     print(right)
    
# print(arr_ex4)

arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    # Hoán đổi
    arr[left], arr[right] = arr[right], arr[left]

    # Dịch con trỏ
    left += 1
    right -= 1

print(arr)