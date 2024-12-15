def add(a, b):
    result = a + b
    print("Output: ", result, '\n')

def subtract(a, b):
    result = a - b
    print("Output: ", result, '\n')

def multiply(a, b):
    result = a * b
    print("Output: ", result, '\n')

def divide(a, b):
    if b == 0:
        print("zero division error\n")
    else:
        result = a / b
        print("Output: ", result, '\n')

while True:
    print("------- Basic Calculator -------")
    try:
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        
        print('''Choose operation:
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Division
          5. Exit Basic Calculator''')
        
        option = int(input("Enter option number: "))
        
        
        if option == 1:
            add(num1, num2)
        elif option == 2:
            subtract(num1, num2)
        elif option == 3:
            multiply(num1, num2)
        elif option == 4:
            divide(num1, num2)
        elif option == 5:
            print("\nThank you for using Basic Calculator!")
            print('''\n
  _______   _     _        ____    ____    _    _    _   ____    
 |__   __| | |   | |      / _  |  |    |  | |  | |  / / |  __|   |
    | |    | |___| |     / /_| |  |  _ |  | |  | | / /  | |__    |  
    | |    |  ___  |    / ___  |  | | ||  | |  | |/ /_  |__  |   | 
    | |    | |   | |   / /   | |  | | ||__| |  |  _   |  __| |   |
    |_|    |_|   |_|  /_/    |_|  |_| |_____|  |_| |__| |____|   *
''')
            break
        else:
            print("Invalid option! Please choose a valid operation.\n")
    except ValueError:
        print("Error: Invalid input! Please enter numeric values for numbers and a valid option number.\n")
    except Exception as e:
        print(f"Unexpected error occurred: {e}\n")
