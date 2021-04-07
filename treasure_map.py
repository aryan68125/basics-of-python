#treasure map
row1=["☠️","☠️","☠️","☠️"]
row2=["☠️","☠️","☠️","☠️"]
row3=["☠️","☠️","☠️","☠️"]
column = [row1,row2,row3]
print(f" {row1} \n {row2} \n {row3}") #before treasure insertion
for i in range(0,1000):
 print("Enter the location where you want to insert the treasure\n")
 k = int(input("Enter the row number\n"))
 j = int(input("Enter the column\n"))
 column[k][j] = input("Enter the treasure\n")

 print(f" {row1} \n {row2} \n {row3}") #after  treasure insertion

 q = input("press q to exit and press enter to continue\n")
 if q=='q' or q=='Q':
  print("terminating program\n")
  break