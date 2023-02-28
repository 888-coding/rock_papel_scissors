#rock papel scissors 
#application for learn random play with computer.

import random

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

print("Welcome to Rock Papel Scissors\n")
mychoice = int(input("Choose your option : 0 - rock , 1 - papel, 2 - scissors\n"))

print("My choice is:")
if mychoice == 0 :
    print(rock)
elif mychoice == 1 :
    print(paper)
else :
    print(scissors)

print("The computer choise is : \n")
computer_choice = random.randint(0,2)
if computer_choice == 0 :
    print(rock)
elif computer_choice == 1 :
    print(paper)
else :
    print(scissors)

if mychoice == computer_choice :
    print("You and the computer is draw")
