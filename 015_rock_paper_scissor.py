import os
import random

banner = '''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣉⠹⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⠰⠿⠿⠂⠻⠿⢶⠀⣀⡀⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⣤⣶⣿⣿⣿⣿⡷⢠⡀⣿⣿⡇⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⠀⠀⢿⣿⡟⢛⣛⡋⣰⣿⡇⣿⣿⡇⣿⣷⣦⡀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠟⠻⣿⡿⠁⠀⠀⠀⠀⠀⢸⣿⣿⠈⢛⣁⠛⠿⠃⠻⢿⡇⣿⣿⢹⣧⠀⠀⠀⠀⠙⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿
⣿⠟⣉⠁⣾⣷⣬⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⣴⣦⣬⡙⠻⣷⣶⣶⣬⣁⣾⡏⠀⠀⠀⠀⠀⠘⣿⡿⢃⣾⣶⢙⣿⣿⣿⣿
⣏⠸⣿⣿⣦⡙⢿⣿⣦⡀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣷⣬⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠈⣴⣿⡿⣡⣾⣿⣿⣿⣿
⡿⢣⣌⠻⣿⣿⣦⡙⢿⣿⣦⡀⠀⠀⣀⣀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⢋⣴⣿⣿⣿⣿⣿⣿
⣇⠻⣿⣷⣌⠻⣿⣿⣦⣙⣿⣿⣷⣄⠻⣿⣿⣷⣆⠻⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⢡⣿⣿⠿⠿⢛⣛⣫⢻
⣿⠇⣈⠻⣿⣷⣌⣻⣿⣿⣿⣿⣿⣿⣷⣬⣿⣿⣿⣧⠙⣿⣿⣿⠟⣰⣾⣶⣤⣀⠠⣶⣿⣿⣿⣇⣀⣬⣵⣶⣾⣿⣿⣿⡿⢈
⣿⣄⠹⢷⣦⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⡿⢃⣾⣿⣿⣿⡇⠻⢿⣦⡍⣿⣿⣿⠿⠿⢟⣛⣛⣭⣭⣴⣾⣿
⣿⣿⣷⣦⡙⢿⣦⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣿⡇⣿⣿⣿⣿⣿⢇⣷⢸⣿⠇⣴⣶⣶⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢸⣿⣷⠸⣿⣿⣿⣏⣾⢇⣤⣍⣈⣩⣭⡉⣁⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠙⠿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣿⣦⡙⢋⣴⣿⣿⣿⣿⣿⣶⣭⣭⣙⣛⡿⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠙⠻⠿⠟⢛⣩⣴⣿⣿⣿⣿⣦⣙⣿⣿⣿⡿⠿⠿⠿⠿⠛⢉⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠘⠿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣤⣤⣤⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
'''

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


def main():
    os.system('clear')
    print(banner)
    print(
        '''
    Welcome Rock, Paper, Scissor Game:

    Game Rules:
    1. Between Rock & Scissor, Rock wins!
    2. Between Paper & Scissor, Scissor wins!
    3. Between Rock & Paper, Paper wins!

    That's all... Let's play the game!!!
    '''
    )
    tmp = input("Press any to continue...")
    winner = 0
    while (winner == 0):
        os.system('clear')
        print(banner)
        userturn = 0
        while True:
            userturn = int(input(
                "Enter 1 for 'Rock', 2 for 'Paper', 3 for 'Scissor': "))
            if userturn >= 1 and userturn <= 3:
                break
            tmp = input("Invalid input, enter anykey to try again... ")
        computerturn = random.randint(1, 3)
        print("Your choice: ")
        if userturn == 1:
            print(rock)
        elif userturn == 2:
            print(paper)
        else:
            print((scissors))
        print("\nComputer's choice: ")
        if computerturn == 1:
            print(rock)
        elif computerturn == 2:
            print(paper)
        else:
            print(scissors)

        if userturn != computerturn:
            if userturn == 1:
                if computerturn == 2:
                    winner = 2
                else:
                    winner = 1
            elif userturn == 2:
                if computerturn == 1:
                    winner = 1
                else:
                    winner = 2
            else:
                if computerturn == 1:
                    winner = 2
                else:
                    winner = 1
            if winner == 1:
                print("Congratulation! You win!!!")
            else:
                print("You loose... Better Luck Next Time!!!")
        else:
            print("It's a draw!!!")
            tmp = input("Enter anykey...")


if __name__ == "__main__":
    main()
