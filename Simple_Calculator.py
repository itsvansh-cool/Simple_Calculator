def Calculator():
    # Intro
    print("Welcome to Calculator.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Creating Infinite Loop until user choose exit.
    while True:
        
        # Exception handling if user enters anything else 
        try:
            operation = int(input("Choose operation (1-5): "))
        except ValueError:
            print("Please enter a number only!")
            continue

        # Executing Exit if user choose 5.
        if(operation == 5):
            break
        
        # Taking input from the user 
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Applying Conditions
        if(operation == 1):
            print(f"Result: {num1 + num2}")
        elif(operation == 2):
            print(f"Result: {num1 - num2}")
        elif(operation == 3):
            print(f"Result: {num1 * num2}")
        elif(operation == 4): 
            if(num2 == 0): # 0 is not allowed in python for division. So we handle it by giving error and continuing loop
                print("Error: Cannot be divided by 0")
                continue
            else:
                print(f"Result: {(num1 / num2)}")
        else:
            print("Invalid Choice! Please choose (1-5)")
            continue
Calculator()
