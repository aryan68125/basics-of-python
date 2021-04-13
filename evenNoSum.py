# this program will give us the sum of all the even numbers in a series
for i in range(0,1000):
 limit = int(input("Enter the limit of the series\n"))
 suma = 0
 for j in range(2,limit,2): #by using the step size as 2 and starting the series from 2 we can get even numbers
  suma = suma+j
 print(f"sum of all the even numbers from 2 to {limit} = {suma}\n")
 print("press q to quit or press enter to continue\n")
 q=input()
 if q == 'q' or q=='Q':
 	print("Program terminated\n")
 	break