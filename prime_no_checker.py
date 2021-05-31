#program to check wheather the entered number is a prime or not
print("prime number checker")
number=int(input("Enter the number\n"))

#function that will check for prime number
def prime(num):
    for i in range(2,num):  
       if (num % i) == 0:  
           print(f"{num} is not a prime number")  
           print(f"{i} times {num//i} is {num}")  
           break  
    else:  
       print(f"{num} is a prime number")  
if number>1:
    prime(number) #function call
else:
    print(f"{number} is not a prime number") 