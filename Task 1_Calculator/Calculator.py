def calculator():

    while True:

        print(f"------------------------- C A L C U L A T O R ----------------------------")

        num1 = int(input(f"Enter the first number\n = "))
        operator = input(f"Enter the operation [ + || - || * || / ]\n = ")
        num2 = int(input(f"Enter the second number\n = "))

        if operator == "+":
            print(f"Addition of {num1} + {num2} is\n = " ,num1 + num2 )

        elif operator =="-":
            print(f"The subtraction of {num1} - {num2} is\n = " , num1 - num2 )

        elif operator =="*":
            print(f"The muliplication of {num1} * {num2} is\n = ", num1 * num2 )

        elif operator == "/":

            if num2==0:
                print(f"The o cannot valid here..Enter the valid number ")
            else:
                print(f"The division of {num1} / {num2} is\n = " , num1 / num2)

        else:
            print(f"Envalid Operator.....Enter the valid operator [ + || - || * || / ]")
        
        choice = input(f"Do you want to continue calculation ( yes / no ) : ")
        if choice == "yes":
            continue
        else:
            break        



calculator()
