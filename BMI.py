#this program accepts height and weight of a person and return the BMI of that person
height = input("what is your height in foot?\n")
heightInMeters = float(height)*0.3048 #converting foot in meters
floatHeight = float(heightInMeters)
weight = input("what is your weight in kg?\n")
floatWeight = int(weight)
BMI = floatWeight/(floatHeight ** 2) #number **2 will return square of the number
BMI_int = int(BMI)                             #number ** 3 will return cube of the number
print("your BMI is = "+"%s"%BMI_int)