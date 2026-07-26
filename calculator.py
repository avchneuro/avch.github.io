def calculator() -> None:
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")

    while True:
        try:
            first_number = float(input("\nВведите первое число: "))
            operation = input("Введите операцию: ").strip()
            second_number = float(input("Введите второе число: "))

            if operation == "+":
                result = first_number + second_number
            elif operation == "-":
                result = first_number - second_number
            elif operation == "*":
                result = first_number * second_number
            elif operation == "/":
                if second_number == 0:
                    print("Ошибка: на ноль делить нельзя.")
                    continue
                result = first_number / second_number
            else:
                print("Ошибка: неизвестная операция.")
                continue

            print(f"Результат: {result}")

        except ValueError:
            print("Ошибка: нужно ввести число.")
            continue

        repeat = input("Продолжить? да/нет: ").strip().lower()

        if repeat not in {"да", "д", "yes", "y"}:
            print("Калькулятор завершён.")
            break


if __name__ == "__main__":
    calculator()
