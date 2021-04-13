#this program will print
#print Fizz if number%3==0
#print Buzz if number%5==0
#print FizzBuzz if number%3==0 and number%5==0
for j in range(0,1000):
 limit = int(input("enter the upper limit of the number series\n"))
 for i in range(1,limit):
  if i%3==0 and i%5==0:
  	print("FizzBuzz")
  elif i%5 == 0:
  	print("Buzz")
  elif i%3 == 0:
  	print("Fizz")
  else:
  	print(i)

 print("press q to quit or press enter to continue\n")
 q = input()
 if q == 'q' or q=='Q':
 	print("terminating program\n")
 	break