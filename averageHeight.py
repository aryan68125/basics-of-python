#this program calculates the average height of students in a list
import itertools #this import itertools is used to print more than one list using one for loop
for i in range(0,1000):
 suma=0
 studentName = []
 studentHeight = []
 Size=int(input("Enter the number of students in the list\n"))
 print("\n")
 for j in range(0,Size):
  print(f"student name and height at index {j}\n")
  student = input() #entering items
  studentName.append(student) #entering items in the list
  height = input() #entering student height
  studentHeight.append(height) #entering student height in the list
 print("\n")
 print("printing the list of students entered by the user\n")
 for (a, b) in zip(studentName, studentHeight): #for this to work you need to import itertools
  print (a, b)                               #this is the for loopwhich will print more than one lists
  suma = suma + int(b)
  average = suma/Size
  averageRound = round(average,2) #rounding up the value of the average up to two decimal places
 print(f"average height of the students in the list  = {averageRound}\n")
 print(" do you want to continue?\n press enter to continue \n press q to terminate program\n")
 q = input()
 if q=="q" or q=="Q":
 	print("Program terminated by the user\n")
 	break