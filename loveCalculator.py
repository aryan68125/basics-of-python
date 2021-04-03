for i in range(0,1000):
 name1 = input("Enter the name of person 1\n")
 name2 = input("enter the name of person 2\n")
 name1LowerCase = name1.lower() # String_variable_name.lower() will convert any upper case character in the string into lower case
 name2LowerCase = name2.lower()
 T1 = name1LowerCase.count("t") #counts the number of occurances of a character in the string
 R1 = name1LowerCase.count("r") #String_variable_name.count("a")
 U1 = name1LowerCase.count("u")
 E1 = name1LowerCase.count("e")
 L1 = name1LowerCase.count("l")
 O1 = name1LowerCase.count("o")
 V1 = name1LowerCase.count("v")
 E1 = name1LowerCase.count("e")
 
 T2 = name2LowerCase.count("t")
 R2 = name2LowerCase.count("r")
 U2 = name2LowerCase.count("u")
 E2 = name2LowerCase.count("e")
 L2 = name2LowerCase.count("l")
 O2 = name2LowerCase.count("o")
 V2 = name2LowerCase.count("v")
 E2 = name2LowerCase.count("e")
 sum1 = T1 + T2 + R1 + R2 + U1 + U2 + E1 + E2
 sum2 = L1 + L2 + O1 + O2 + V1 + V2 + E1 + E2
 sum1String = str(sum1) #converting int to string
 sum2String = str(sum2) #converting int to string
 result = sum1String + sum2String
 print(f"The compatibility percentage of {name1} and {name2} is {result}\n")
 q = input("press enter to continue or press q to terminate the program\n")
 if q == 'q':
  print("Program terminated\n")
  break