# Step 1: Defining basic operations

def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

Step 2: Implementing a User Interface

This function call and the user interaction will be commented out as it cannot be executed in this environment.
However, this is how it would look:

def main():
    while True:
        print("Select operation:")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")

        choice = input("Enter choice(1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                result = divide(num1, num2)
                print(num1, "/", num2, "=", result)

        elif choice == '5':
            break
        else:
            print("Invalid Input")

main() # This call will be commented out as it cannot be executed here.

