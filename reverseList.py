#how to reverse a list
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
system_reverse = [] #empty list
print('system List:', systems)

# print the elements inside the systems list in reverse order without modifying the actual list
k=-1
l=0
for i in range(0,len(systems)):
    print('printing List in reverse order:', systems[k])
    k-=1
    l+=1
# Get a list with reversed contents
#reversing the list and copying it to another list
system_reverse = list(reversed(systems))
print("printing the entire system_reverse List")
print(system_reverse)

#reversing list using reverse function
# List Reverse
systems.reverse()
print(f"printing the actual system list after modifying it and reversing it\n{systems}")

#reversing a list without using a reverse function
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"numbers list before modification reverse {numbers}")
# Get list length
L = len(numbers)
 
# i goes from 0 to the middle
for i in range(int(L/2)):
    # Swap each number with the number in 
    # the mirror position for example first 
    # and last
    n = numbers[i]
    numbers[i] = numbers[L-i-1]
    numbers[L-i-1] = n
 
# At this point the list should be reversed
print(f"numbers list after modification reverse {numbers}")