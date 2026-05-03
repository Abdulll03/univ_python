# base_function.py
# import math

# class Function:
#     """Базовый класс для функций от одной переменной."""

#     def __init__(self, name):
#         # 6. Демонстрация конструктора родителя
#         self._name = name  # Поле: Название функции

#     @property
#     def name(self):
#         """Свойство для получения имени функции."""
#         return self._name

#     def get_value(self, x):
#         """Виртуальный метод для вычисления значения функции (будет переопределен)."""
#         raise NotImplementedError("Метод get_value должен быть переопределен в наследниках")

#     def get_derivative(self):
#         """Виртуальный метод для создания экземпляра производной."""
#         raise NotImplementedError("Метод get_derivative должен быть переопределен")

#     def display_info(self):
#         """
#         4. Виртуальный метод, который будет переопределен в одном наследнике 
#         и не переопределен в другом.
#         """
#         return f"Это базовая математическая функция: {self._name}"



# exponent.py
# import math
# from base_function import Function

# class Exponent(Function):
#     """Класс функции Экспонента f(x) = e^x."""

#     def __init__(self):
#         # 6. Вызов конструктора родительского класса
#         super().__init__("Экспонента (e^x)")

#     def get_value(self, x):
#         # 3. Перегрузка (переопределение) метода родителя
#         return math.exp(x)

#     def get_derivative(self):
#         # Производная e^x это e^x
#         return Exponent()

#     def display_info(self):
#         # 4. Переопределяем виртуальный метод
#         return f"Специализированный класс для работы с {self.name}"




# sinh_function.py
# import math
# from base_function import Function
# import cosh_function # Импорт будет внутри метода, чтобы избежать циклической зависимости

# class Sinh(Function):
#     """Класс функции Гиперболический синус f(x) = sinh(x)."""

#     def __init__(self):
#         super().__init__("Гиперболический синус (sinh)")

#     def get_value(self, x):
#         return math.sinh(x)

#     def get_derivative(self):
#         # Производная sinh(x) это cosh(x)
#         from cosh_function import Cosh
#         return Cosh()

#     # 4. Метод display_info НЕ переопределяется здесь (используется базовый)



# cosh_function.py
# import math
# from base_function import Function

# class Cosh(Function):
#     """Класс функции Гиперболический косинус f(x) = cosh(x)."""

#     def __init__(self):
#         super().__init__("Гиперболический косинус (cosh)")

#     def get_value(self, x):
#         return math.cosh(x)

#     def get_derivative(self):
#         # Производная cosh(x) это sinh(x)
#         from sinh_function import Sinh
#         return Sinh()

#     def display_info(self):
#         # 4. Переопределяем виртуальный метод
#         return f"Объект класса Косинус: {self.name}"



# main.py
# from exponent import Exponent
# from sinh_function import Sinh
# from cosh_function import Cosh

# def main():
#     print("=== Демонстрация наследования и полиморфизма (Вариант 14) ===\n")

#     # Создаем список различных функций (Полиморфизм)
#     functions = [Exponent(), Sinh(), Cosh()]
    
#     x_value = 1.0 # Тестовое значение аргумента

#     for func in functions:
#         print(f"--- Работа с объектом: {func.name} ---")
        
#         # 5. Продемонстрировать работу всех методов
#         # Вызов (возможно) переопределенного метода display_info
#         print(f"Инфо: {func.display_info()}")
        
#         # Вычисление значения
#         val = func.get_value(x_value)
#         print(f"Значение функции в точке x={x_value}: {val:.4f}")
        
#         # Получение производной
#         deriv_func = func.get_derivative()
#         print(f"Тип производной: {type(deriv_func).__name__}")
#         print(f"Значение производной в точке x={x_value}: {deriv_func.get_value(x_value):.4f}")
#         print("-" * 40)

# if __name__ == "__main__":
#     main()