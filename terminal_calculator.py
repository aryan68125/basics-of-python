#terminal calculator

for i in range(0,999999999):
    #function for addition
    def addition(a,b):
        return a + b
    #function for subtraction
    def subtraction(a,b):
        return a-b
    #function for multiplication
    def multiplication(a,b):
        return a*b
    #function for division
    def  division(a,b):
        if b == 0:
            print("divide by zero error\n")
            return
        else:
            return a/b

    operation = {
    '+':addition,
    '-':subtraction,
    '*':multiplication,
    '/':division
    }
    def cal():
        #user input
        num1 = float(input("Enter the first number\n"))
        for symbols in operation:
            print (symbols)
        should_continue_with_previous_answer = True
        while should_continue_with_previous_answer:
            operation_symbol = input("Choose the operation\n")
            num2 = float(input("Enter the second number\n"))
        
            calculation_function = operation[operation_symbol]
            answer = calculation_function(num1,num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
            c = input("Press y to continue calculation with the previous answer or Press n to start a new calcuation\n")
            if c.lower() == "y":
                num1 = answer
            else:
                should_continue_with_previous_answer =False
                cal()

    choice2 = input("Press ENTER to continue and N to quit program\n")
    if choice2.lower() == 'n':
        break
    else:
        cal()

