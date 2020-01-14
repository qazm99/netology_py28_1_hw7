class Negative_float(ArithmeticError):
    def print_error(self):
        print("Операнды только положительные числа")

def polsky_calculate(operator, operand1, operand2):
    assert operator in ["+", "-", "*", "/"]
    operand1 = float(operand1)
    operand2 = float(operand2)
    if (operand1 < 0) or (operand2 < 0):
        raise Negative_float
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = operand1 / operand2
    else:
        print("Некорректный оператор")
        return False
    return result

def main():
    print("Польская нотация. Для выполнения")
    while True:

        polsky_in = input("Введите арифметическую операцию и 2 операнда через пробел: ")
        polsky_in_list = polsky_in.strip().split()
        try:
            result_calculate = polsky_calculate(polsky_in_list[0], polsky_in_list[1], polsky_in_list[2])
            if result_calculate != False:
                print(f"Результат арифметической операции: {result_calculate}")
            else:
                print("Не удалось вычислить!")
        except AssertionError:
            print(f"Ошибка выполнения операции, нет такого операнда, попробуйте еще раз")
        except IndexError:
            print(f"Ошибка выполнения операции, не хватает операндов, попробуйте еще раз")
        except ZeroDivisionError:
            print(f"Ошибка выполнения операции, на ноль делить нельзя, попробуйте еще раз")
        except (TypeError, ValueError, Negative_float):
            print(f"Ошибка выполнения операции, операнды должны быть только положительные числа, попробуйте еще раз")
        except Exception as e:
            print(f"Ошибка выполнения операции {e}, попробуйте еще раз")

main()
