#COPYING A LIST
#to copy a list, you can make a slice that inclues the entire original list by omitting the first index and the second index ([:]).
#this tells python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #copies my_foods and creates a new list names friend_foods

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#adding to new items to each list to show that they are different:
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#THIS Will not WORK
# friend_foods = my_foods  this will associate friends_food to the list of my_foods. 
# variable will point to the same list.

