import sys
name = raw_input("what is your name")
length = len(name)
print("Number of characters including spaces are = "+"%s"%length)
print("String entered by the user is = "+name)
# this program will return the number of characters in a string entered by the user using raw_input
#print(len(raw_input("what is your name"))) is in the code that you have written in the IDE
#then the raw_input during the run time of the program is replaced by the String entered by the user
# for example:- print(len(Aditya Kumar)) the String enetered by the user at run time is Aditya Kumar
#and it will return the number of characters in a String entered by the user in the terminal output 
#here in this case its 12 (Remember it will also include spaces within the String )