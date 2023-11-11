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

# Write your code below this line 👇
import random

while (True):
    print(f"enter your choice among for rock option 0,  paper option 1 and scissors option 2")
    user_choice = int(input())

    computer_choice = random.randint(0, 2)
    print(f"computer choose {computer_choice}")
    if (user_choice == computer_choice):
        print("draw. please retry")
    elif (user_choice == 0 and computer_choice == 1):
        print("you lose. computer wins")
    elif (user_choice == 0 and computer_choice == 2):
        print("you win. computer loses")
    elif (user_choice == 1 and computer_choice == 0):
        print("you win. computer loses")
    elif (user_choice == 1 and computer_choice == 2):
        print("you lose. computer wins")
    elif (user_choice == 2 and computer_choice == 0):
        print("you lose. computer wins")
    elif (user_choice == 2 and computer_choice == 1):
        print("you win. computer loses")
    else:
        print("invalid choice. please retry")
    retry = input("Enter your choice to retry or exit").lower()
    if (retry == "retry"):
        continue
    elif (retry == "exit"):
        break
    else:
        break

