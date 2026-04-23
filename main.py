
# # 12
# import math

# f = lambda x: math.sqrt(x**2 - 0.16) / x
# # точная первообразная F(x) относительно нижней границы a=1
# F_exact = lambda x: math.sqrt(x**2-0.16) - 0.4*math.acos(0.4/x) - math.sqrt(0.84) + 0.4*math.acos(0.4)

# a, b, n = 1.0, 2.0, 160
# h = (b - a) / n
# integral, x = 0.0, a

# print(f"{'x':<6} | {'Числ. F(x)':<12} | {'Точн. F(x)':<12} | {'Погр.':<9}")
# for i in range(n + 1):
#     if i > 0: 
#         integral += (f(x - h) + f(x)) / 2 * h
#     if i % 20 == 0: # вывод каждые 1/8 (20 шагов из 160)
#         t = F_exact(x)
#         print(f"{x:<6.3f} | {integral:<12.6f} | {t:<12.6f} | {abs(integral-t):.2e}")
#     x += h


# # 13
# print('\n\n\nЗадание 13 \n\n')
# import math

# print(f"{'x':>4} | {'Стирлинг':>14} | {'Точное':>14} | {'Погрешн.':>9}")
# x = 1.0
# while x <= 10.1:
#     # формула Стирлинга из условия
#     s = math.sqrt(2*math.pi/x) * (x/math.e)**x * (1 + 1/(12*x) + 1/(288*x**2) - 139/(51840*x**3))
#     g = math.gamma(x) # точное табличное значение
    
#     print(f"{x:4.1f} | {s:14.6f} | {g:14.6f} | {abs(s-g):.2e}")
#     x += 0.9



# # 17
# print('\n\n\nTask 17\n')
# import numpy as np

# n = 23
# i = np.arange(1, n + 1)

# # Вычисляем массив a: если i > 17 -> sin(i), иначе ctg(i)^2
# a = np.where(i > 17, np.sin(i), (1 / np.tan(i))**2)

# m = a.mean()
# d = (a**2).mean() - m**2

# print(f"Математическое ожидание M = {m:.6f}")
# print(f"Дисперсия D = {d:.6f}")



# 19
# print('\n\n\nTask 19\n')
# import numpy as np

# # 1. Исходные данные
# n = 20
# i = np.arange(1, n + 1)  # Создаем индексы от 1 до 20

# # 2. Вычисляем компоненты вектора x
# # Формула: arcctg(sqrt(i) + 1/20) + e^(-0.5 * i)
# # Используем np.pi / 2 - np.arctan() для реализации арккотангенса
# arg = np.sqrt(i) + (1 / 20)
# x = (np.pi / 2 - np.arctan(arg)) + np.exp(-0.5 * i)

# # 3. Вывод вектора на печать
# print("Вектор x:")
# print(x)

# # 4. Проверка на монотонное возрастание
# # np.diff(x) вычисляет разницу между соседними элементами (x[i+1] - x[i])
# # Если все разницы > 0, то последовательность строго возрастает
# is_mono_increasing = np.all(np.diff(x) > 0)

# print("-" * 30)
# print(f"Логическая переменная: {is_mono_increasing}")



# 20
# 1. Сначала создадим тестовый файл f.txt (для примера)
# with open('f.txt', 'w', encoding='utf-8') as f:
#     f.write("Это   пример текста   в котором есть а одиночные буквы и   лишние пробелы.")

# # 2. Основная логика обработки
# try:
#     with open('f.txt', 'r', encoding='utf-8') as file_in:
#         content = file_in.read()
        
#     # .split() разбивает строку по любым пробелам и удаляет пустые элементы
#     words = content.split()
    
#     # Фильтруем слова: оставляем только те, длина которых больше 1
#     filtered_words = [word for word in words if len(word) > 1]
    
#     # Соединяем слова обратно через один пробел
#     result = " ".join(filtered_words)
    
#     # 3. Записываем результат в файл g.txt
#     with open('g.txt', 'w', encoding='utf-8') as file_out:
#         file_out.write(result)
        
#     print("Обработка завершена. Результат записан в g.txt")
#     print(f"Результат: {result}")

# except FileNotFoundError:
#     print("Ошибка: входной файл f.txt не найден.")


# 21
# import turtle
# import math

# def draw_circle(x, y, radius):
#     turtle.penup()
#     turtle.goto(x, y - radius)
#     turtle.setheading(0)
#     turtle.pendown()
#     turtle.circle(radius)
#     turtle.penup()

# def draw_dial():
#     # Настройки окна
#     screen = turtle.Screen()
#     screen.title("Телефонный диск")
#     turtle.speed(0)
#     turtle.hideturtle()

#     # 1. Большой внешний круг
#     draw_circle(0, 0, 180)

#     # 2. Маленький центральный круг
#     draw_circle(0, 0, 25)

#     # 3. Рисуем отверстия и цифры
#     # Радиус, на котором расположены центры отверстий
#     orbit_radius = 140
#     # Радиус самого отверстия
#     hole_radius = 25
    
#     # Цифры на диске идут от 1 до 9, затем 0
#     digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#     # Начальный угол для '1' примерно 0 градусов (справа), 
#     # идем против часовой стрелки с шагом 30 градусов
#     start_angle = 0
    
#     for i, digit in enumerate(digits):
#         angle_deg = start_angle + i * 30
#         angle_rad = math.radians(angle_deg)
        
#         # Вычисляем координаты центра отверстия
#         x = orbit_radius * math.cos(angle_rad)
#         y = orbit_radius * math.sin(angle_rad)
        
#         # Рисуем отверстие
#         draw_circle(x, y, hole_radius)
        
#         # Пишем цифру внутри (немного смещаем по y, чтобы была в центре)
#         turtle.goto(x, y - 12)
#         turtle.write(digit, align="center", font=("Arial", 16, "normal"))

#     # 4. Рисуем упор для пальца (треугольник)
#     # Расположим его чуть ниже цифры '1'
#     stop_angle = math.radians(-35)
#     stop_x = 180 * math.cos(stop_angle)
#     stop_y = 180 * math.sin(stop_angle)
    
#     turtle.goto(stop_x, stop_y)
#     turtle.setheading(20) # Поворот треугольника
#     turtle.pendown()
#     # Рисуем треугольник
#     for _ in range(3):
#         turtle.forward(50)
#         turtle.left(120)
#     turtle.penup()

#     # Завершение
#     screen.mainloop()

# if __name__ == "__main__":
#     draw_dial()


import matplotlib.pyplot as plt
import numpy as np

# Параметры из условия
a = -5 * np.pi
b = 10 * np.pi
n = 100

x = np.linspace(a, b, n)

y = 2 * np.cos(x - np.pi / 6)

plt.figure(figsize=(12, 6))
plt.plot(x, y, label=r'$y = 2 \cos(x - \pi/6)$', color='blue', linewidth=2)

plt.title(f'График функции $y = 2 \\cos(x - \\pi/6)$ на интервале [$-5\\pi$, $10\\pi$]')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True, linestyle='--', alpha=0.7)

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# # Настроим деления по оси X, чтобы они отображались в долях Пи (опционально для красоты)
def format_func(value, tick_number):
    N = int(np.round(value / np.pi))
    if N == 0: return "0"
    if N == 1: return r"$\pi$"
    if N == -1: return r"$-\pi$"
    return r"${0}\pi$".format(N)

plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(format_func))
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(base=np.pi * 2)) # Шаг в 2 Пи

plt.legend()
plt.show()