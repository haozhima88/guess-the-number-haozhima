#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import art
import random


print(art.logo)
# random.seed = 10
# random_num = random.randint(1, 100)

def check_answer(num):
  # print(random_num)
  if num < random_num:
    return "Too low."
  elif num > random_num:
    return "Too High"
  elif num == random_num:
    return num

def game_start():
  esay = 10
  difficult = 5
  # global times

  choice = input("Choice the difficulty level, Type 'E' means easy or Type 'D' means difficult.")
  if choice == 'E':
    times = esay
  elif choice == 'D':
    times = difficult

  while times:
    num = int(input("Guess the number:"))
    print(check_answer(num))
    if type(check_answer(num)) == type(''):
      times -= 1
      if times == 0:
        print(f"The correct number is {random_num}")
      else:
        print(f"Times remains {times}")
    else:
      times = 0
      print("You guess it!")
    

is_continue = True
while is_continue:
  random_num = random.randint(1, 100)
  game_start()
  restart = input("Do you want to rerun the game? 'yes' or 'no'.\n")
  if restart == 'no':
    is_continue = False
