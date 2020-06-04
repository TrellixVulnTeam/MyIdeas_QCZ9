while True:
    print("\nOptions: ")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input=input(":")

    if user_input=="quit":
        break
    elif user_input=="add":
        num_1=float(input("Input the first number:"))
        num_2=float(input("Input the second number:"))
        result=str(num_1+num_2)
        print('The result is '+ result)
    elif user_input=="subtract":
        num_1 = float(input("Input the first number:"))
        num_2 = float(input("Input the second number:"))
        result=str(num_1-num_2)
        print('The result is ' + result)

    elif user_input=="multiply":
        num_1 = float(input("Input the first number:"))
        num_2 = float(input("Input the second number:"))
        result=str(num_1*num_2)
        print('The result is ' + result)
    elif user_input=="divide":
        num_1 = float(input("Input the first number:"))
        num_2 = float(input("Input the second number:"))
        result=str(num_1/num_2)
        print('The result is ' + result)

    else:
        print('Unknown input. Try again')