# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)

random_person = random.randint(0, num_items - 1)
picked_person = names[random_person]

print(picked_person + " is going to buy the meal today!")
