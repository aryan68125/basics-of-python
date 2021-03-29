result = 0
for i in range(0,1000):
 number1 = input("enter the first number\n")
 number2 = input("enter the second number\n")
 num1 = int(number1)
 num2 = int(number2)
 operator = input("enter the operator +,-,/,*,power\n")
 if operator == "+":
  result = num1 + num2
  print(f"{num1} + {num2} = {result} \n") # here we are using f string to convert the different data types into string in an easy way
 if operator == "-":
  result = num1 - num2
  print(f"{num1} - {num2} = {result} \n")
 if operator == "*":
  result = num1 * num2
  print(f"{num1} * {num2} = {result} \n")
 if operator == "**":
   result = num1**num2 #this operator will give us the power of number 1 for example num1**num2 = num1 Power num2
   print(f"{num1}^{num2} = {result} \n")
 if operator == "/":
  if num2!=0:
   result = num1/num2
   print(f"{num1} / {num2} = {result} \n")
  else:
   print("divide by zero error\n")
 operator = input("do you want to quit , press q to exit , press any key to continue\n")
 if operator == "q":
 	print("terminating program\n")
 	break #break statement is used to break out of program loop
