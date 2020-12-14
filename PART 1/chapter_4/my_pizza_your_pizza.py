my_pizzas = ["pepperoni", "chesse", "Meatza"]
friend_pizzas = my_pizzas[:] #make a copy of the list of pizzas and call it friend_pizza

#add a new pizza to the original list
my_pizzas.append('veggie')
#add a a different pizza to the friend's list
friend_pizzas.append('chicago')

#prove that the lists are not the same
print("My favorite pizzas are:")
print(my_pizzas)
print(f"\nMy friend's favorite pizzas are:")
print(friend_pizzas)

#write a loop to print out the names of my favorite pizza
for pizza in my_pizzas:
	print(f"I like to eat {pizza} pizza!")
print("I'll eat pizza all day!")