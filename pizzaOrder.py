#this program is made to take the order of the customer in a pizza shop and calculate the bill
cost = 0
for i in range(0,1000):
 print(" 1. Large pizaa \n 2. Medium Pizza \n 3. Small Pizza\n")
 size = input("Choose the size of the pizza\n")
 if size == "1":
  print("you chose Large sized pizza\n")
  cost = 25
  pepperoni = input("do you want to add pepperoni?\n")
  if pepperoni == "y":
   cost += 3
  cheese = input("do you want to add cheese?\n")
  if cheese == "y":
   cost += 1
  print(f"you have to pay ${cost}\n") 
 if size == "2":
  print("you chose Medium sized pizza\n")
  cost = 20
  pepperoni = input("do you want to add pepperoni?\n")
  if pepperoni == "y":
   cost += 3
  cheese = input("do you want to add cheese?\n")
  if cheese == "y":
   cost += 1
  print(f"you have to pay ${cost}\n") 
 if size == "3":
  print("you chose Small sized pizza\n")
  cost = 15
  pepperoni = input("do you want to add pepperoni?\n")
  if pepperoni == "y":
   cost += 2
  cheese = input("do you want to add cheese?\n")
  if cheese == "y":
   cost += 1
  print(f"you have to pay ${cost}\n")
 q = input("do you want to quit , press q to exit , press any key to continue\n")
 if q == "q":
 	print("terminating program\n")
 	break #break statement is used to break out of program loop