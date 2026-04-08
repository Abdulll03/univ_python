
# 12
import math

f = lambda x: math.sqrt(x**2 - 0.16) / x
# точная первообразная F(x) относительно нижней границы a=1
F_exact = lambda x: math.sqrt(x**2-0.16) - 0.4*math.acos(0.4/x) - math.sqrt(0.84) + 0.4*math.acos(0.4)

a, b, n = 1.0, 2.0, 160
h = (b - a) / n
integral, x = 0.0, a

print(f"{'x':<6} | {'Числ. F(x)':<12} | {'Точн. F(x)':<12} | {'Погр.':<9}")
for i in range(n + 1):
    if i > 0: 
        integral += (f(x - h) + f(x)) / 2 * h
    if i % 20 == 0: # вывод каждые 1/8 (20 шагов из 160)
        t = F_exact(x)
        print(f"{x:<6.3f} | {integral:<12.6f} | {t:<12.6f} | {abs(integral-t):.2e}")
    x += h


# 13
print('\n\n\nЗадание 13 \n\n')
import math

print(f"{'x':>4} | {'Стирлинг':>14} | {'Точное':>14} | {'Погрешн.':>9}")
x = 1.0
while x <= 10.1:
    # формула Стирлинга из условия
    s = math.sqrt(2*math.pi/x) * (x/math.e)**x * (1 + 1/(12*x) + 1/(288*x**2) - 139/(51840*x**3))
    g = math.gamma(x) # точное табличное значение
    
    print(f"{x:4.1f} | {s:14.6f} | {g:14.6f} | {abs(s-g):.2e}")
    x += 0.9



# 17
print('\n\n\nTask 17\n')
import numpy as np

n = 23
i = np.arange(1, n + 1)

# Вычисляем массив a: если i > 17 -> sin(i), иначе ctg(i)^2
a = np.where(i > 17, np.sin(i), (1 / np.tan(i))**2)

m = a.mean()
d = (a**2).mean() - m**2

print(f"Математическое ожидание M = {m:.6f}")
print(f"Дисперсия D = {d:.6f}")



# 19
print('\n\n\nTask 19\n')
import numpy as np

# 1. Исходные данные
n = 20
i = np.arange(1, n + 1)  # Создаем индексы от 1 до 20

# 2. Вычисляем компоненты вектора x
# Формула: arcctg(sqrt(i) + 1/20) + e^(-0.5 * i)
# Используем np.pi / 2 - np.arctan() для реализации арккотангенса
arg = np.sqrt(i) + (1 / 20)
x = (np.pi / 2 - np.arctan(arg)) + np.exp(-0.5 * i)

# 3. Вывод вектора на печать
print("Вектор x:")
print(x)

# 4. Проверка на монотонное возрастание
# np.diff(x) вычисляет разницу между соседними элементами (x[i+1] - x[i])
# Если все разницы > 0, то последовательность строго возрастает
is_mono_increasing = np.all(np.diff(x) > 0)

print("-" * 30)
print(f"Логическая переменная: {is_mono_increasing}")



# 20
# 1. Сначала создадим тестовый файл f.txt (для примера)
with open('f.txt', 'w', encoding='utf-8') as f:
    f.write("Это   пример текста   в котором есть а одиночные буквы и   лишние пробелы.")

# 2. Основная логика обработки
try:
    with open('f.txt', 'r', encoding='utf-8') as file_in:
        content = file_in.read()
        
    # .split() разбивает строку по любым пробелам и удаляет пустые элементы
    words = content.split()
    
    # Фильтруем слова: оставляем только те, длина которых больше 1
    filtered_words = [word for word in words if len(word) > 1]
    
    # Соединяем слова обратно через один пробел
    result = " ".join(filtered_words)
    
    # 3. Записываем результат в файл g.txt
    with open('g.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(result)
        
    print("Обработка завершена. Результат записан в g.txt")
    print(f"Результат: {result}")

except FileNotFoundError:
    print("Ошибка: входной файл f.txt не найден.")