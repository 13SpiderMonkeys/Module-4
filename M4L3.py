import random

#Create a list of 10 numbers and 5 letters

elements = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']

#randomly select four elements from the list
winning_ticket = random.sample(elements,4)

#print the winning ticket message
print("Any ticket matching these four numbers or letters wins a prize!", winning_ticket)
