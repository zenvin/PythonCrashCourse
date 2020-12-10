# learning List

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# pulling the first item in the list [0]
print(bicycles[0])

# string methods (and possibly other methods) can be used on the list
print(bicycles[0].title())

# indexing starts at zero. Easy to get the last item on the list is to use [-1]. use -2, -3 etc for the 2nd to the last, 3rd to the last etc.
print(bicycles[-1])

# using individual values from a list: use f-strings (not sure if we went over this already).
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)



