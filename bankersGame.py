#a program that decices who will pay the bill in a group of friends randomly
import random
for j in range(0,1000):
 names_list=[]
 n=int(input("Enter the size\n")) #convert String into int
 print("\n")
 for i in range(0,n):
  print("Enter number at index\n",i)
  item = input()
  names_list.append(item) #use append list to enter the elements in the null value
 print("names list \n",names_list)
 x = len(names_list)-1 #x is the length of an array
 y = random.randint(1, x)
 print(names_list[y]+" should pay the bill")
 q = input("do you want to continue\n")
 if q=="q" or q=="Q":
 	print("Terminating program\n")
 	break