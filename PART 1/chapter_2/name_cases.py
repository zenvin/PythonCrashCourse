#Goal: Use a variable to represent a person's name, and print a message to that person. Your message should be simple, such as, "Hello Eric, would you like to learn some Python today?"

name = input("Greetings! What is your name\n")
print("Hi " + name + ", are you ready to learn some Python today?")
name_lower = name.lower()
print("Hi " + name_lower + ", are you ready to learn some Python today?")
name_upper = name.upper()
print("Hi " + name_upper + ", are you ready to learn some Python today?")
name_title = name.title()
print("Hi " + name_title + ", are you ready to learn some Python today?")