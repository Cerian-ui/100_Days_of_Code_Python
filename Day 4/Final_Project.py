rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#Without using lists
import random

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if player == 0:
  print(rock)
elif player == 1:
  print(paper)
elif player == 2:
  print(scissors)
else:
  print("Not an existing choice")

computer = random.randint(0,2)

if computer == 0:
  print("Computer choose:\n" + rock)
elif computer == 1:
  print("Computer choose:\n" + paper)
else:
  print("Computer choose:\n" + scissors)

if player == 0 and computer == 2:
  print("You win!")
elif computer == 0 and player == 2:
  print("You lose")
elif computer > player:
  print("You lose")
elif player > computer:
  print("You win!")
elif computer == player:
  print("It's a draw")


#-----------------------------------------------------------------------------------------------------
#Using lists
import random
choices = [rock, paper, scissors]

player_list = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(choices[player_list])

computer_list = random.randint(0,2)
print("Computer chose:")
print(choices[computer_list])

if player_list == 0 and computer_list == 2:
  print("You win!")
elif computer_list == 0 and player_list == 2:
  print("You lose")
elif computer_list > player_list:
  print("You lose")
elif player_list > computer_list:
  print("You win!")
elif computer_list == player_list:
  print("It's a draw")
