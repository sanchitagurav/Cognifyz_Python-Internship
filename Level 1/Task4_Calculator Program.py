def calculator():
    print("🧮 Basic Calculator")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, %): ").strip()
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero!"
        elif operator == '%':
            if num2 != 0:
                result = num1 % num2
            else:
                return "Error: Modulo by zero!"
        else:
            return "Invalid operator!"

        return f"Result: {num1} {operator} {num2} = {result}"

    except ValueError:
        return "Invalid input! Please enter numeric values."

# Run the calculator
print(calculator())
