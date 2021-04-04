#this program is written to guess wheather the coin has landed in heads or tales surface
# a simple game
import random
for i in range(0,1000):
 num = input(" Press 0 to choose head \n Press 1 to choose Tails\n")
 numInt = int(num)
 random_float = random.random() #this will generate random number b/w 0 to 0.99999
 random_roundUp = round(random_float)
 if random_roundUp == 0 and numInt == 0:
  print(f"your guess is right It's a Head\n")
 elif random_roundUp == 1 and numInt == 1:
  print("your guess is right It's a Tail\n")
 else:
  print("your guess is wrong \n Try again!!!\n")
 
 q= input("press q to terminate the program OR Press enter to continue\n")
 if q=='q' or q=='Q':
  print("Program terminated by the user\n")
  break