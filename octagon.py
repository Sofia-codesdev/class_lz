import math
import matplotlib.pyplot as plt

class Octagon:
    def __init__(self, side):
        # Задание 1:
        self.side = side  # Задается через конструктор
        self.angle = 135  # Константный угол правильного восьмиугольника (градусы)
        self.k = 1 + math.sqrt(2)  # Константа k
        
        if self.side <= 0:
            raise ValueError("Сторона должна быть больше нуля!")

    # Задание 2:
    def get_perimeter(self):
        """Периметр октагона"""
        return 8 * self.side

    def get_area(self):
        """Площадь октагона"""
        return 2 * (1 + math.sqrt(2)) * (self.side ** 2)

    def get_circumscribed_radius(self):
        """Радиус описанной окружности (R)"""
        # Формула: R = a / (2 * sin(pi/8))
        return self.side / (2 * math.sin(math.pi / 8))

    def get_circumscribed_area(self):
        """Площадь описанной окружности"""
        r = self.get_circumscribed_radius()
        return math.pi * (r ** 2)

    def get_inscribed_radius(self):
        """Радиус вписанной окружности (r)"""
        # Формула: r = a / (2 * tg(pi/8))
        return self.side / (2 * math.tan(math.pi / 8))

    def get_inscribed_area(self):
        """Площадь вписанной окружности"""
        r = self.get_inscribed_radius()
        return math.pi * (r ** 2)

    # Задание 3:
    def draw(self):
        """Отрисовка фигур на координатной плоскости"""
        # Вычисляем координаты вершин восьмиугольника
        r_circum = self.get_circumscribed_radius()
        r_in = self.get_inscribed_radius()
        
        # Углы для вершин (через 45 градусов)
        angles = [math.radians(45 * i) for i in range(8)]
        
        # Координаты вершин октагона
        x_oct = [r_circum * math.cos(a) for a in angles]
        y_oct = [r_circum * math.sin(a) for a in angles]
        
        # Замыкаем фигуру
        x_oct.append(x_oct[0])
        y_oct.append(y_oct[0])

        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Рисуем октагон (Синий)
        ax.plot(x_oct, y_oct, color='blue', linewidth=2, label='Октагон')
        ax.fill(x_oct, y_oct, color='blue', alpha=0.1)
        
        # Рисуем описанную окружность (Красный)
        circle_out = plt.Circle((0, 0), r_circum, color='red', fill=False, linestyle='--', label='Описанная окружность')
        ax.add_patch(circle_out)
        
        # Рисуем вписанную окружность (Зеленый)
        circle_in = plt.Circle((0, 0), r_in, color='green', fill=False, linestyle=':', label='Вписанная окружность')
        ax.add_patch(circle_in)

        # Настройки графика для красоты
        ax.set_aspect('equal') # Чтобы окружности не были овалами
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.set_title(f"Октагон со стороной {self.side}")
        ax.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        
        plt.show()