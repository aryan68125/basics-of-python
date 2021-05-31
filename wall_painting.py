#calculate the number of cans required to paint the area of wall
#user should enter the height and width of the wall in meters
#calculate the area and then calculate the number of cans required
#formula for calculating the number of cans = 1 can = 5 meters square area of wall
# height = 2 width = 4 -> no of cans = (2X4)/5 = 1.6

#download and install art pip3 install art in your linux machine or mac osX then import art
from art import *

Art1=text2art("paint",font='block',chr_ignore=True) # Return ASCII text with block font
print(Art1)
print("\n")
Art2=text2art("can",font='block',chr_ignore=True) # Return ASCII text with block font
print(Art2)
print("\n")
calculator=text2art("Calculator") # Return ASCII text (default font) and default chr_ignore=True 
print(calculator)
print("\n")

height = int(input("enter the height of the wall\n"))
width = int(input("Enter the width of the wall\n"))
#function to calculate the area of a wall in meter square
def area_of_wall(height,width):
    area_of_wall.area = height * width
area_of_wall(height=height,width=width)
areaOfWall = area_of_wall.area
#function to calculate the number of cans required to paint the given area of wall
def can(area):
    can.numberOfCans=round(area/5)
ar =area_of_wall.area
can(ar)
cansOFPaint = can.numberOfCans

print(f"height of wall = {height}")
print(f"width of wall = {width}")
print(f"area of wall = {areaOfWall}")
print(f"number of cans required = {cansOFPaint}")