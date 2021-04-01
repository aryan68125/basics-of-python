#this program calculates the number of days , months and years left in your life 
#supposing max lifespan is 90 years
for i in range(0,1000):
 age = input("enter your age\n")
 YearsLeft = 90 - int(age)
 DaysLeft = YearsLeft * 365
 MonthsLeft = YearsLeft * 12
 WeeksLeft = YearsLeft * 52
 print(f"your current age is = {age}\n")
 print(f"no of days left = {DaysLeft} , no of WeeksLeft = {WeeksLeft} , no of months left = {MonthsLeft}")
 q = input("Press q to quit hit enter to continue\n")
 if q == "q":
 	break