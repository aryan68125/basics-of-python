#find the student with the heigest score from a list of students
import itertools #this import itertools is used to print more than one list using one for loop
for i in range(0,1000):
 heigh=0
 index=0
 studentName = []
 studentScore = []
 Size=int(input("Enter the number of students in the list\n"))
 print("\n")
 for j in range(0,Size):
  print(f"student name and score at index {j}\n")
  student = input() #entering items
  studentName.append(student) #entering items in the list
  score = int(input()) #entering student score
  studentScore.append(score) #entering student score in the list
  if heigh < score:
   heigh = score
   index = j
 print("\n")
 print("printing the list of students entered by the user\n")
 for (a, b) in zip(studentName, studentScore): #for this to work you need to import itertools
  print (a, b)                                 #this is the for loopwhich will print more than one lists
 print(f"{studentName[index]} is the student who obtained heighest marks {heigh} in the class\n")
 print(" do you want to continue?\n press enter to continue \n press q to terminate program\n")
 q = input()
 if q=="q" or q=="Q":
 	print("Program terminated by the user\n")
 	break