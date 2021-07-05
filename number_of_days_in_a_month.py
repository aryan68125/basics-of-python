#number of days in a month


year = input("Enter the year\n")
month = input("Enter the month in numbers\n")
#create a function to check for the leap year
def leap_year(y):
    year = int(y)
    if year%4 == 0:
 	    if year%100 == 0:
 		    if year%400 ==0:
 			    print(f"{year} is a leap year\n")
 			    return True
 		    else:
 			    print(f"{year} is not a leap year\n")
 			    return False
 	    else:
 		    print(f"{year} is a leap year\n")
 		    return True
    else:
 	    print(f"{year} is not a leap year\n")
 	    return False

def days_in_month(month_number):
    month_name = ["january","febuary","march","april","may","june","july","august","september","october","november","december"]
    month_days_non_leap_year = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_in_days_leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
    year_check = leap_year(year)
    if year_check==True:
        month_id = int(month_number)
        list_index = month_id-1
        days_in_month_selected = month_in_days_leap_year[list_index]
        month_name_selected = month_name[list_index]
        output = f"{month_name_selected} = {days_in_month_selected}"
        return output
    if year_check == False:
        month_id = int(month_number)
        list_index = month_id-1
        days_in_month_selected = month_days_non_leap_year[list_index]
        month_name_selected = month_name[list_index]
        output = f"{month_name_selected} = {days_in_month_selected}"
        return output

number_of_days_in_the_selected_month = days_in_month(month)

print(f"number of days in month {number_of_days_in_the_selected_month}")