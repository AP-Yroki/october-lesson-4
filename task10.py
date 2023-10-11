# решение с презентации
# def shift(lst, steps):
#     if steps < 0:
#         steps = abs(steps)
#         for i in range(steps):
#             lst.append(lst.pop(0))
#     else:
#         for i in range(steps):
#             lst.insert(0, lst.pop())
#
#
# nums = [4, 5, 6, 7, 8, 9, 0]
# print(nums)
#
# shift(nums, -2)
# print(nums)
#
# shift(nums, 3)
# print(nums)

def shift(list, n): # Моё решение
    if n < 0:
        n = abs(n)
        for i in range(n):
            list.append(list.pop(0))
    else:
        for i in range(n):
            list.insert(0, list.pop())

list = [1, 2, 3, 4, 5]
shift(list, 3)
print(list)
shift(list, -2)
print(list)
