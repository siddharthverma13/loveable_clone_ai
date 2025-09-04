def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def main():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Enter operation (+, -, *, /): ")

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation")
                continue

            print("Result:", result)
            break  # Exit loop if calculation is successful

        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    main()
