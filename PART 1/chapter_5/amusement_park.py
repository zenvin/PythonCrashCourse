#The if-elif-else Chain

#When you need to test more than two possible situations, use the if-elif-else syntax.
#each condition in if-elif-else will run in order until one passes.

age = 12

if age < 4:
	print("Your admission cost is $0.00.")
elif age < 18:
	print("Your admission cost is $25.00.")
else:
	print("Your admission cost is $40.00.")

#alternate way to code the above. Rather than printing the admission price within
# the if-elif-else block, it would be more concise to set just the price inside 
#the if-elif-else chain and then have a simple print() call that runs after the chain
#has been evaluated:

age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40

print(f"Your admission cost is ${price}.")

#USING MULTIPLE elif BLOCKS

#you can use as many elif as you like. 

age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else: #inferring that everyone else is 65 and over
	price = 20

print(f"Your admission cost is ${price}.")

#OMITTING THE else BLOCK
#Python does not require an else block at the end of the if-elif chain.
#Sometimes an else block is useful; sometimes it is clearer to use an additional elif
#that cathces the specific conditon of interest. if we're confident with the parameters use elif

age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65: #catchall statement. else means we don't know what other situations exist. 
	price = 20


