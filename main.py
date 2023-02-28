#rock papel scissors 
#application for learn random play with computer.

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

if mychoice == 0 :
    print(rock)
elif mychoice == 1 :
    print(paper)
else :
    print(scissors)
