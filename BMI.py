
#this program accepts height and weight of a person and return the BMI of that person
for i in range(0,1000):
 height = input("what is your height in foot?\n")
 heightInMeters = float(height)*0.3048 #converting foot in meters
 floatHeight = float(heightInMeters)
 weight = input("what is your weight in kg?\n")
 floatWeight = float(weight)
 BMI = round(floatWeight/(floatHeight ** 2)) #number **2 will return square of the number, round function will round the number upto nearest whole number
 BMIFloat = float(BMI)                             #number ** 3 will return cube of the number
 print(f"your BMI = {BMIFloat}")
 if BMIFloat<18.5:
 	print("you are underweight\n")
 elif BMIFloat<25:
 	print("you have normal weight\n")
 elif 30<BMIFloat:
 	print("you are over weigth\n")
 elif BMIFloat<35:
    print("you are obesse\n")
 else:
 	print("you are clinically obesse\n")
 q=input("press q to quit or press enter to continue\n")
 if q == 'q':
  print("terminating BMI program\n")
  break