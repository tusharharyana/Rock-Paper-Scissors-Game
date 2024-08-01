#Rock paper scissors small python game.
import random,sys,time 
#Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''


# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

#start again
start = r"""
     __..,,... .,,,,,.
                     ''''        ,'        ` .
                               ,'  ,.  ..      `  .
                               `.,'      ..           `
                     __..,.             .  ..     .
                            ` .       .  `.  .` `
                                ,  `.  `.  `._|,..
                                  .  `.  `..'
                                   ` -'`''
                                   
                                   
"""

#Lose

lose = r'''
                       ((\
            (              _  ,-_  \ \
            )             / \/  \ \ \ \
            (            /)| \/\ \ \| |
            `~()_______)___)\ \ \ \ \ |
                        |)\ )  `' | | |
                       /  /,          |
                       |  |          /
       You Lose        |  |         /
    But you win my     \           /
      Heart baby        \         /
                         )       /
                        /       /
                       /       /
                              /
'''

#Win

win = r'''

                                 /-_-\
                                /  /  \
                               /  /    \
     You win my Heart          \  \    /
         Darling                \__\__/
                                  || ___
                                  ||/__/
                               ___||
                              /__/||
       \                       ___|L._
       //-------------------./   ._. \)
                            |   / (_\_\)
                            |_ '  (___)
\                           |     (__)
 \                          |`----||'
  \_________________________|     ||
                                  ||

'''
while True:
  print("Lets start the game") 
  print("What do you choose ? ")
  print("Type 0 for Rock")
  print("Type 1 for Paper")
  print("Type 2 for Scissiors")

  choice = input()

  random_number = random.random()

  computer_choice = ''
  user_choice = ''
  ch1 = ''
  ch2 = ''
  if random_number < 0.35:
    ch2 = 'Rock'
    computer_choice = rock
  elif random_number >= 0.33 and random_number < 0.66:
    ch2 = 'Paper'
    computer_choice = paper
  else:
    ch2 = 'Scissors'
    computer_choice = scissors

  if choice == '0':
    ch1 = 'Rock'
    user_choice = rock
  elif choice == '1':
    ch1 = 'Paper'
    user_choice = paper
  elif choice == '2':
    ch1 = 'Scissors'
    user_choice = scissors
  else:
    print("Invalid choice Dear")
    sys.exit()

  if user_choice == computer_choice:
    time.sleep(2)
    print(f"Your choice : {ch1}\n{user_choice}"+"\n")
    time.sleep(2)
    print(f"Computer choice : {ch2}\n{computer_choice}"+"\n")
    print("Start again\n")
    time.sleep(1)
    print(start)
  elif user_choice == paper and computer_choice == rock:
    time.sleep(2)
    print(f"Your choice : Paper \n{user_choice}"+"\n")
    time.sleep(2)
    print(f"Computer choice : Rock \n{computer_choice}"+"\n")
    time.sleep(1)
    print("You win\n")
    print(win)
  elif user_choice == rock and computer_choice == scissors:
    time.sleep(2)
    print(f"Your choice : Rock \n{user_choice}"+"\n")
    time.sleep(2)
    print(f"Computer choice : Scissors \n{computer_choice}"+"\n")
    time.sleep(1)
    print("You win\n")
    print(win)   
  elif user_choice == scissors and computer_choice == paper:
    time.sleep(2)
    print(f"Your choice : Scissors \n{user_choice}"+"\n")
    time.sleep(2)
    print(f"Computer choice : Paper \n{computer_choice}"+"\n")
    time.sleep(1)
    print("You win\n")
    print(win)      
  else:
    print(f"Your choice : {ch1}\n{user_choice}"+"\n")
    time.sleep(2)
    print(f"Computer choice : {ch2}\n{computer_choice}"+"\n")
    time.sleep(2)
    print("You lose\n")
    print(lose)

 
  option  = input("Do you wants to play again? Y/N ~ ")

  if option == 'Y' or option == 'y':
    pass
  else:
    print("Thanks for playing")
    sys.exit()
    
