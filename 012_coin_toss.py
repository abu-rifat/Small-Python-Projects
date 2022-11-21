from getkey import getkey, key
import os
import random

while 1:
    os.system('clear')
    print("Welcome to Coin Toss Sumulation.\n")
    print(
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣟⣛⣛⣛⣉⣉⣛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣟⡵⠞⠉⠀⢈⣿⣿⣿⠿⠟⠛⠛⠛⠻⡆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⡀⣀⣠⣴⣿⣿⣿⠁⣶⣿⣿⣿⠿⠛⣡⡋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣭⣥⣤⣶⣾⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠈⠉⠉⢻⣿⡇⠀⠙⢿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠶⣶⣶⣿⣿⣿⣄⠀⠀⠈⢻⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣀⣀⡀⣹⡉⠙⠻⠀⠀⠀⠀⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠉⠉⠙⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠓⠶⠶⠤⣿⡇⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣀⣠⣾⡇⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣉⣁⣀⣀⡀⠀⠀⠀⠀⠀⠀⢸⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣾⣿"
    )
    print("\nPress 'Space' key to flip the coin, Press 'ESC' key to terminate...\n")
    pressed = getkey()
    if pressed == key.SPACE:
        coin = random.randint(0,1)
        if coin == 0:
            print("\n\nHead is the winner!")
        else:
            print("\n\nTail is the winner!")
    elif pressed == key.ESC:
        os.system('clear')
        break
    else:
        print("\n\nInvalid Key Press!")
    print("\n\nPress Anykey To Continue!!!")
    pressed = getkey()