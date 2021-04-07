#this is the example program of nested list
#a program that decices who will pay the bill in a group of friends randomly
import random
for j in range(0,1000):
 boys_list=[]
 n=int(input("Enter the size\n")) #convert String into int
 print("\n")
 for i in range(0,n):
  print("Enter number at index\n",i)
  item = input()
  boys_list.append(item) #use append list to enter the elements in the null value
 print("names list \n",boys_list)

 girls_list=[]
 n2=int(input("Enter the size\n")) #convert String into int
 print("\n")
 for k in range(0,n2):
  print("Enter number at index\n",k)
  item2 = input()
  girls_list.append(item2) #use append list to enter the elements in the null value
 
 print("boys list = ", boys_list)
 print("girls list = ", girls_list)
 
 class_list = [boys_list,girls_list]
 print("children in a class = \n",class_list)
 q = input("do you want to continue\n")
 if q=="q" or q=="Q":
 	print("Terminating program\n")
 	break