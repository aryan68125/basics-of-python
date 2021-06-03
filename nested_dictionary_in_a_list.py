#this program demonstrates how to deal with nested dictionaies inside a list
travel_log = [] #empty list

# a function that will accept county, names of cities visited and number of times you have visited the country
def travel(country_name, city_names_list, numberOfTimeVisited):
    #using global keyword will allow us to make changes in the list declared globally outside the function
    global travel_log
    travel_data = {} #empty dictionary
    country = country_name #string
    city_names = city_names_list.copy() #list
    visit = numberOfTimeVisited #integer

    #entering data into the dictionary in the run time
    #travel_data[key] = value
    travel_data["country"] = country
    travel_data["city"] = city_names
    travel_data["visits"] = visit

    #now adding our newly created dictionary into our list
    travel_log.append(travel_data)

for i in range(0,1000):
    cities = [] #cities list
    print("press 1 to enter the travel data inside travel log list")
    print("press 2 to print the travel log list")
    print("press 3 to exit ")
    choice = int(input())
    if choice == 1:
        #input from user
        #enter country name
        countryName = input("enter the name of the country you've visited\n")

        #enter city names in the lsit cities
        print(f"enter the number of cities you have visited in {countryName}\n")
        n = int(input())
        print(f"Enter the cities you have visited in {countryName}\n")
        for i in range(0, n):
            print("Enter city at index", i, )
            item = input()
            cities.append(item)
        print(f"cities = {cities}")
 
        #enter number of times you have visited the country
        print(f"enter number of times you have visited the {countryName}")
        visit = int(input())
        travel(country_name = countryName, city_names_list = cities, numberOfTimeVisited = visit)
    elif choice==2:
        print(travel_log)
    elif choice==3:
        print("program terminated")
        break
