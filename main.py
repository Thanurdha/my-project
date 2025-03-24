import basic_operations
import advanced_operations

if __name__ == "__main__":
    print("Simple Calculator")
    print("Choose an operation: add, subtract, multiply, divide, power, modulus, square-root")

    operation = input("Enter operation: ").strip().lower()

    try:
        if operation == "square-root":
            num = float(input("Enter the number: "))
            print(f"Result: {advanced_operations.square_root(num)}")
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == "add":
                print(f"Result: {basic_operations.add(num1, num2)}")
            elif operation == "subtract":
                print(f"Result: {basic_operations.subtract(num1, num2)}")
            elif operation == "multiply":
                print(f"Result: {basic_operations.multiply(num1, num2)}")
            elif operation == "divide":
                print(f"Result: {basic_operations.divide(num1, num2)}")
            elif operation == "power":
                print(f"Result: {advanced_operations.power(num1, num2)}")
            elif operation == "modulus":
                print(f"Result: {advanced_operations.modulus(num1, num2)}")
            else:
                print("Invalid operation! Please try again.")
    except ValueError:
        print("Error! Please enter valid numbers.")
