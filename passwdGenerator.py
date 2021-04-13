#password generator
import random
from random import shuffle
for i in range(0,1000):
 character = 'A'
 letters = []
 numbers = []
 symbols = ['!','@','#','$','%','^','&','*','+','_']
 for j in range(0,26):

  # Using chr()+ord() will increament the character
  # prints P
  x = chr(ord(character) + j)
  letters.append(x)
 for k in range(0,10):
  numbers.append(k)
 print("Enter the number of letters you want in your password. it should be less than 26\n")
 numberOfLetters = int(input())
 numberOfNumbers = int(input("Enter the number of numbers you want in your password it should be less than 9\n"))
 numberOfSymbols = int(input("Enter the number of Symbols in your password it should be less than 9\n"))
 print("creating password from dictionary\n")
 print(letters)
 print(numbers)
 print(symbols)

 if numberOfLetters >26 or numberOfNumbers>9 or numberOfSymbols>9:
  print("try again limit exceeded\n")
  break
 else:
  print("randomizing characters\n")
  #loop for randomizing letters
  L=[]
  for l in range(0,numberOfLetters):
   lengthLetter = len(letters)-1
   y=random.randint(0,lengthLetter)
   L.append(letters[y])
  
  #loop for randomizing numbers
  N=[]
  for n in range(0,numberOfNumbers):
   lengthNumbers = len(numbers)-1
   z=random.randint(0,lengthNumbers)
   N.append(numbers[z])
  
  #loop for randomizing symbols
  Sym=[]
  for s in range(0,numberOfSymbols):
   lengthSymbols=len(symbols)-1
   x=random.randint(0,lengthSymbols)
   Sym.append(symbols[x])
 
  a2 = 0 #index of L list
  b2 = 0 #index of N list
  c2 = 0 #index for Sym list
  acc=[] # final list of randomized letters numbers and symbols
  Passwd = "" # it will hold the final generated password
  accLen = numberOfLetters + numberOfNumbers + numberOfSymbols - 1 # size of acc list
  for w in range(0,accLen):
   if a2> numberOfLetters-1: # set index to zero if it exceeds the max size of the list
   	a2=0
   if b2 > numberOfNumbers-1:
   	b2=0
   if c2 > numberOfSymbols-1:
   	c2=0
   #randomizing the place of appearance of symbols,letters and numbers in the list
   choice = random.randint(1,3)
   if choice==1:
    acc.append(L[a2])
    a2 = a2+1
   elif choice==2:
    acc.append(N[b2])
    b2 = b2+1
   elif choice == 3:
    acc.append(Sym[c2])
    c2 = c2+1
   Passwd =str(Passwd) + str(acc[w]) #conatinating each elemnts present inside acc into Passwd
  print("the generated password is = \n"+Passwd)
 print("press q to quit or press enter to continue\n")
 q=input()
 if q=='q' or q=='Q':
 	print("program terminated\n")
 	break