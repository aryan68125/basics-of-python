for i in range(0,1000):
 y = input("enter the year you wanna check\n")
 year = int(y)
 if year%4 == 0:
 	if year%100 == 0:
 		if year%400 ==0:
 			print(f"{year} is a leap year\n")
 		else:
 			print(f"{year} is not a leap year\n")
 	else:
 		print(f"{year} is a leap year\n")
 else:
 	print(f"{year} is not a leap year\n")
 ch = input("press q to quit or press enter to continue\n")
 if ch=='q':
  print("program terminated by the user\n")
  break
