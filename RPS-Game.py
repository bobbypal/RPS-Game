print(" Welcome to the Rock, Paper and Scissor game.")
print('''           RPF
-----RULES ARE SIMPLE-----''')
print('''Rock beats Scissors (Rock crushes Scissors).
Scissors beats Paper (Scissors cuts Paper).
Paper beats Rock (Paper covers Rock).

''')

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

#Human choice

choose_you = input("---> Input R for rock, P for paper and S for scissor👉 : ").lower()
if choose_you == "r":
    print("Your choice : Rock")
    print(rock)
elif choose_you == "p":
    print("Your choice : Paper")
    print(paper)
elif choose_you == "s":
    print("Your choice : Scissors")
    print(scissors)
else:
    print("Invalid inputs")

#Computer choice
import random
list_rps = ["r", "p", "s"]
choose_bot = random.choice(list_rps)
if choose_bot == "r":
    print(rock)
    print("Bot choice : Rock")
elif choose_bot == "p":
    print(paper)
    print("Bot choice : Paper")
else:
    print(scissors)
    print("Bot choice : Scisssors")

#Compare to win or loose
if choose_you == "r" and choose_bot == "s":
    print("YOU WIN🏆")
elif choose_you == "r" and choose_bot == "p":
    print("YOU LOOSE😒")
elif choose_you == "p" and choose_bot == "r":
    print("YOU WIN🏆")
elif choose_you == "p" and choose_bot == "s":
    print("YOU LOOSE😒")
elif choose_you == "s" and choose_bot == "p":
    print("YOU WIN🏆")
elif choose_you == "s" and choose_bot == "r":
    print("YOU LOOSE😒")
else:
    print("GAME TIE🫡")