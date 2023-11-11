# a = 3
# b = 5
# def f(a, b):
#     if b == 1:
#         return a
#     return a * f(a, b-1)
# print(f(a, b))

def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b - 1)

print(sum(a = 6, b = 16))