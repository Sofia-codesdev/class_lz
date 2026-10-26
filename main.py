from octagon import Octagon

def main():
    
    try:
        # Ввод стороны пользователем
        side_input = float(input("Введите длину стороны октагона: "))
        
        # Создание объекта класса
        my_octagon = Octagon(side_input)
        
        # Вывод результатов в консоль
        print("\n--- Результаты расчетов ---")
        print(f"Периметр октагона: {my_octagon.get_perimeter():.2f}")
        print(f"Площадь октагона: {my_octagon.get_area():.2f}")
        print(f"Радиус описанной окружности: {my_octagon.get_circumscribed_radius():.2f}")
        print(f"Площадь описанной окружности: {my_octagon.get_circumscribed_area():.2f}")
        print(f"Радиус вписанной окружности: {my_octagon.get_inscribed_radius():.2f}")
        print(f"Площадь вписанной окружности: {my_octagon.get_inscribed_area():.2f}")

        # Вызов метода отрисовки
        print("\nСтроим график... (закройте окно с графиком, чтобы завершить программу)")
        my_octagon.draw()

    except ValueError as e:
        print(f"Ошибка ввода: {e}. Пожалуйста, введите положительное число.")

if __name__ == "__main__":
    main()