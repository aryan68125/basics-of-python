#this program accepts the total amount of the bill that is to be payed by the customers and tells them how much they would have to pay :- payment = tip + actual payment
import sys
total_bill = input("What is the total bill?\n") #input for python3 and raw_input for python2 input is used to input a value in the variable in run time
noOfPeople = input("Number of people that you want to split the bill for = \n")
bill_split = float(total_bill) / float(noOfPeople)
tip = input("percentage of tip that you want to pay for total bill\n")
calculated_tip = (float(tip)/100)*float(bill_split)
payment = float(bill_split)+float(calculated_tip)
print("each person would have to pay (actual payment  + tip) = "+"%s"%payment) 