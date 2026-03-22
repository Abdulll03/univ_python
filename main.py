'''
# Задача 1. Р-е кодом
import math as m

x, y, z = 8, 9, 10

# расчет a и b
a = (y/m.sin(x) + y/(m.sin(x)**2 - 3*m.cos(z))) * m.exp(5*x**2)
b = (5 - m.exp(z-2)) / (y + x**2 * abs(z**2 - m.tan(z)))

print(f"a = {a}\nb = {b}")


# Задача 2. Р-е кодом
import math as m

# ввод: 3 точки, например: 0 0, 4 0, 2 3
pts = [list(map(float, input(f"Точка {i+1} (x y): ").split())) for i in range(3)]
# расчет длин сторон: AB, BC, CA
d = [m.dist(pts[i], pts[(i+1)%3]) for i in range(3)]

# проверка на треугольник и равнобедренность (с допуском на точность)
if sum(d) > 2*max(d) and any(m.isclose(d[i], d[(i+1)%3]) for i in range(3)):
    p = sum(d) / 2
    S = m.sqrt(p * (p-d[0]) * (p-d[1]) * (p-d[2]))
    print("Высоты:", *[round(2*S/side, 4) for side in d])
else:
    print("Треугольник не равнобедренный или не существует")
'''


# import math

# # Константы из условий
# mu0 = 4 * math.pi * 1e-7
# I = 1.1
# N = 530
# L = 0.17
# R = 0.025
# n = N / L

# # Список значений 'a' от 0.01 до 0.17 с шагом 0.01
# a_values = [round(i * 0.01, 2) for i in range(1, 18)]

# print(f"{'a (м)':<10} | {'B (мТл)':<15}")
# print("-" * 28)

# for a in a_values:
#     # Расчет косинусов по первой картинке
#     cos_beta1 = (L - a) / math.sqrt(R**2 + (L - a)**2)
#     cos_beta3 = a / math.sqrt(R**2 + a**2)
    
#     # Расчет B по второй картинке
#     B = (mu0 * I * n / 2) * (cos_beta1 + cos_beta3)
    
#     # Домножаем на 10^3 (перевод в мТл)
#     B_scaled = B * 10**3
    
#     print(f"{a:<10} | {B_scaled:<15.4f}")




# import math

# a = float(input("Введите a: "))
# b = float(input("Введите b: "))
# c = float(input("Введите c: "))
# x_start = float(input("Введите Xнач: "))
# x_end = float(input("Введите Xкон: "))
# dx = float(input("Введите dX: "))

# print("-" * 25)
# print(f"| {'X':^10} | {'F':^10} |")
# print("-" * 25)

# x = x_start

# # основной цикл расчета (используем небольшую дельту для точности float)
# while x <= x_end + dx / 2:
#     # определение значения функции F в зависимости от условий
#     if x < 1 and c != 0:
#         f = a * x**2 + b / c
#     elif x > 1 and c == 0:
#         # проверка на деление на 0 (x-c)
#         if (x - c) == 0:
#             f = None
#         else:
#             f = (x - a) / (x - c)**2
#     else:
#         # проверка на деление на 0
#         if c == 0:
#             f = None
#         else:
#             f = x**2 / c**2

#     if f is not None:
#         if int(a * b) % 2 == 0:
#             res_display = f"{f:.3f}" # вещественное значение
#         else:
#             res_display = f"{int(f)}" # целое значение
#     else:
#         res_display = "Ошибка"

#     print(f"| {x:^10.2f} | {res_display:^10} |")
    
#     x += dx

# print("-" * 25)


