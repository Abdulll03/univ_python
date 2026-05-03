
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


# import matplotlib.pyplot as plt
# import numpy as np

# # Параметры из условия
# a = -5 * np.pi
# b = 10 * np.pi
# n = 100

# x = np.linspace(a, b, n)

# y = 2 * np.cos(x - np.pi / 6)

# plt.figure(figsize=(12, 6))
# plt.plot(x, y, label=r'$y = 2 \cos(x - \pi/6)$', color='blue', linewidth=2)

# plt.title(f'График функции $y = 2 \\cos(x - \\pi/6)$ на интервале [$-5\\pi$, $10\\pi$]')
# plt.xlabel('x')
# plt.ylabel('y')

# plt.grid(True, linestyle='--', alpha=0.7)

# plt.axhline(0, color='black', linewidth=1)
# plt.axvline(0, color='black', linewidth=1)

# # # Настроим деления по оси X, чтобы они отображались в долях Пи (опционально для красоты)
# def format_func(value, tick_number):
#     N = int(np.round(value / np.pi))
#     if N == 0: return "0"
#     if N == 1: return r"$\pi$"
#     if N == -1: return r"$-\pi$"
#     return r"${0}\pi$".format(N)

# plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(format_func))
# plt.gca().xaxis.set_major_locator(plt.MultipleLocator(base=np.pi * 2)) # Шаг в 2 Пи

# plt.legend()
# plt.show()




# 25
# class Product:
#     # 1. Конструктор (с параметрами по умолчанию, что заменяет конструктор по умолчанию)
#     def __init__(self, name="Неизвестно", price_rub=0.0, manufacturer="Неизвестно"):
#         self.name = name
#         self.price_rub = float(price_rub)
#         self.manufacturer = manufacturer

#     # 2. Деструктор для сообщения об уничтожении объекта
#     def __del__(self):
#         print(f"[System]: Объект '{self.name}' удален.")

#     # 3. Метод 1: Пересчитать цену товара в евро
#     def calculate_price_euro(self, rate):
#         if rate <= 0:
#             return 0
#         return self.price_rub / rate

#     # 3. Метод 2: Увеличить цену товара, если название содержит «Samsung»
#     def apply_samsung_markup(self, percent=10):
#         if "Samsung" in self.name:
#             self.price_rub += self.price_rub * (percent / 100)
#             print(f"-> Цена товара '{self.name}' увеличена на {percent}% (бренд Samsung).")
#         else:
#             print(f"-> Товар '{self.name}' не является Samsung, цена не изменена.")

#     # 4. Функция формирования строки информации об объекте
#     def get_info(self):
#         return (f"Товар: {self.name:<20} | "
#                 f"Изготовитель: {self.manufacturer:<15} | "
#                 f"Цена: {self.price_rub:>10.2f} руб.")

# # 5. Создание проекта для демонстрации работы
# def main():
#     print("=== Лабораторная работа №25 (Вариант 14) ===\n")
    
#     # Курс евро для расчетов
#     EURO_RATE = 100.0

#     # Создание трех объектов класса:
    
#     # Объект 1: Со значениями-константами
#     obj1 = Product("Samsung Galaxy S24", 95000.0, "Samsung")

#     # Объект 2: Со значениями-константами
#     obj2 = Product("iPhone 15", 110000.0, "Apple")

#     # Объект 3: С вводом данных с клавиатуры
#     print("Введите данные для третьего товара:")
#     name = input("Наименование: ")
#     try:
#         price = float(input("Цена в рублях: "))
#     except ValueError:
#         price = 0.0
#     manuf = input("Изготовитель: ")
#     obj3 = Product(name, price, manuf)
    
#     products = [obj1, obj2, obj3]

#     print("\n--- Список товаров до обработки ---")
#     for p in products:
#         print(p.get_info())
#         print(f"    Цена в евро: {p.calculate_price_euro(EURO_RATE):.2f} EUR")

#     print("\n--- Обработка данных (Метод 2) ---")
#     for p in products:
#         p.apply_samsung_markup()

#     print("\n--- Список товаров после обработки ---")
#     for p in products:
#         print(p.get_info())

#     print("\nЗавершение работы программы...")
# if __name__ == "__main__":
#     main()




# 27
# import csv
# import os

# # 1. Представление таблиц в виде структур Python
# # Используем списки словарей. Связи осуществляются через ID.
# countries = []  # {'id': int, 'name': str}
# cities = []     # {'id': int, 'country_id': int, 'name': str}
# streets = []    # {'id': int, 'city_id': int, 'name': str}

# # --- ФУНКЦИИ ДЛЯ РАБОТЫ С ФАЙЛАМИ (.csv) ---

# def save_to_csv():
#     """Сохранение всех структур в CSV файлы"""
#     with open('countries.csv', 'w', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=['id', 'name'])
#         writer.writeheader()
#         writer.writerows(countries)
    
#     with open('cities.csv', 'w', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=['id', 'country_id', 'name'])
#         writer.writeheader()
#         writer.writerows(cities)
        
#     with open('streets.csv', 'w', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=['id', 'city_id', 'name'])
#         writer.writeheader()
#         writer.writerows(streets)
#     print("\n[Система]: Данные успешно сохранены в CSV.")

# def load_from_csv():
#     """Загрузка данных из CSV файлов"""
#     global countries, cities, streets
#     try:
#         if os.path.exists('countries.csv'):
#             with open('countries.csv', 'r', encoding='utf-8') as f:
#                 countries = list(csv.DictReader(f))
#                 for c in countries: c['id'] = int(c['id'])
        
#         if os.path.exists('cities.csv'):
#             with open('cities.csv', 'r', encoding='utf-8') as f:
#                 cities = list(csv.DictReader(f))
#                 for c in cities: 
#                     c['id'] = int(c['id'])
#                     c['country_id'] = int(c['country_id'])
        
#         if os.path.exists('streets.csv'):
#             with open('streets.csv', 'r', encoding='utf-8') as f:
#                 streets = list(csv.DictReader(f))
#                 for s in streets:
#                     s['id'] = int(s['id'])
#                     s['city_id'] = int(s['city_id'])
#         print("\n[Система]: Данные загружены из файлов.")
#     except Exception as e:
#         print(f"Ошибка при загрузке: {e}")

# # --- ФУНКЦИИ ОБРАБОТКИ ДАННЫХ (CRUD и Связи) ---

# def add_country(name):
#     new_id = max([c['id'] for c in countries], default=0) + 1
#     countries.append({'id': new_id, 'name': name})

# def delete_country(country_id):
#     # Каскадное удаление: сначала города этой страны и их улицы
#     global countries, cities, streets
#     # 1. Находим города этой страны
#     cities_to_del = [c['id'] for c in cities if c['country_id'] == country_id]
#     # 2. Удаляем улицы этих городов
#     streets = [s for s in streets if s['city_id'] not in cities_to_del]
#     # 3. Удаляем города
#     cities = [c for c in cities if c['country_id'] != country_id]
#     # 4. Удаляем саму страну
#     countries = [c for c in countries if c['id'] != country_id]

# def show_variant_info():
#     """Вывод информации согласно Варианту 10"""
#     print("\n=== ИНФОРМАЦИЯ ПО СТРАНАМ И ГОРОДАМ ===")
#     for country in countries:
#         # Список городов для каждой страны
#         country_cities = [c['name'] for c in cities if c['country_id'] == country['id']]
#         print(f"Страна: «{country['name']}», города: {', '.join(country_cities) if country_cities else 'нет городов'}")

#     print("\n=== СТАТИСТИКА ПО ГОРОДАМ (УЛИЦЫ) ===")
#     for city in cities:
#         # Количество улиц в каждом городе
#         street_count = sum(1 for s in streets if s['city_id'] == city['id'])
#         print(f"Город: {city['name']} | Количество улиц: {street_count}")

# # --- ИНТЕРФЕЙС КОНСОЛИ ---

# def main_menu():
#     load_from_csv()
#     while True:
#         print("\n--- МЕНЮ УПРАВЛЕНИЯ БАЗОЙ ДАННЫХ ---")
#         print("1. Показать отчет (Вариант 10)")
#         print("2. Добавить страну")
#         print("3. Добавить город (в страну)")
#         print("4. Добавить улицу (в город)")
#         print("5. Удалить страну (каскадно)")
#         print("6. Сохранить изменения")
#         print("0. Выход")
        
#         choice = input("Выберите действие: ")
        
#         if choice == '1':
#             show_variant_info()
#         elif choice == '2':
#             name = input("Введите название страны: ")
#             add_country(name)
#         elif choice == '3':
#             if not countries: print("Сначала создайте страну!"); continue
#             for c in countries: print(f"{c['id']}: {c['name']}")
#             c_id = int(input("ID страны: "))
#             name = input("Название города: ")
#             new_id = max([c['id'] for c in cities], default=0) + 1
#             cities.append({'id': new_id, 'country_id': c_id, 'name': name})
#         elif choice == '4':
#             if not cities: print("Сначала создайте город!"); continue
#             for c in cities: print(f"{c['id']}: {c['name']}")
#             c_id = int(input("ID города: "))
#             name = input("Название улицы: ")
#             new_id = max([s['id'] for s in streets], default=0) + 1
#             streets.append({'id': new_id, 'city_id': c_id, 'name': name})
#         elif choice == '5':
#             for c in countries: print(f"{c['id']}: {c['name']}")
#             c_id = int(input("ID страны для удаления: "))
#             delete_country(c_id)
#             print("Удалено.")
#         elif choice == '6':
#             save_to_csv()
#         elif choice == '0':
#             break
#         else:
#             print("Неверный ввод.")

# if __name__ == "__main__":
#     main_menu()



