num = input("Enter the number\n")
numTostr = str(num) #converting integer to string
result=0
for digit in numTostr: #traversal sequence
 result += int(digit) #put a space before result whenever writing inside a for loop or in an if statement
print("sum of digits in "+"%s"%num+" is = "+"%s"%result)