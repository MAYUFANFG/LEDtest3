# main.py

from function import add, subtract, multiply, divide

def main():
    print("Welcome to the Calculator Program!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = int(input("Enter choice (1/2/3/4): "))
    
    if choice == 1:
        result = add(num1, num2)
        operation = "+"
    elif choice == 2:
        result = subtract(num1, num2)
        operation = "-"
    elif choice == 3:
        result = multiply(num1, num2)
        operation = "*"
    elif choice == 4:
        result = divide(num1, num2)
        operation = "/"
    else:
        print("Invalid choice")
        return
    
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
