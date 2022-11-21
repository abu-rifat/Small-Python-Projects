import os

winner = 2
turn =0
vals = ["❌","⭕️","  "];
board = [
    [2,2,2],
    [2,2,2],
    [2,2,2]
]

def print_board():
    print(
        f"{vals[board[0][0]]}┃{vals[board[0][1]]}┃{vals[board[0][2]]}\n"
        "━━╋━━╋━━\n"
        f"{vals[board[1][0]]}┃{vals[board[1][1]]}┃{vals[board[1][2]]}\n"
        "━━╋━━╋━━\n"
        f"{vals[board[2][0]]}┃{vals[board[2][1]]}┃{vals[board[2][2]]}\n"
    )

def check():
    global winner

    if board[0][0]!=2 and board[0][0]==board[0][1]==board[0][2]:
        winner=board[0][0]
    elif board[1][0]!=2 and board[1][0]==board[1][1]==board[1][2]:
        winner=board[0][0]
    elif board[2][0]!=2 and board[2][0]==board[2][1]==board[2][2]:
        winner=board[0][0]
    elif board[0][0]!=2 and board[0][0]==board[1][0]==board[2][0]:
        winner=board[0][0]
    elif board[0][1]!=2 and board[0][1]==board[1][1]==board[2][1]:
        winner=board[0][0]
    elif board[0][2]!=2 and board[0][2]==board[1][2]==board[2][2]:
        winner=board[0][0]
    elif board[0][0]!=2 and board[0][0]==board[1][1]==board[2][2]:
        winner=board[0][0]
    elif board[0][2]!=2 and board[0][2]==board[1][1]==board[2][0]:
        winner=board[0][2]

    if winner == 2:
        ck=True
        for row in board:
            for col in row:
                if col == 2:
                    ck = False
                    break
            if ck == False:
                break
        
        if ck:
            winner = -1

def play():
    global turn

    while(winner == 2):
        os.system('clear')
        print("::::::::Tic Tac Toe:::::::\n\n")
        print_board()
        print(f"\n\nIt's {vals[turn]}'s turn, enter row and column no to place the symbol...\n")
        row = 0
        while row<1 or row>3:
            row = int(input("Enter row[1,3] number: "))
            if row<1 or row>3:
                tmp = input("Invalid row number, press anykey to continue...")
        col = 0
        while(col<1 or col>3):
            col = int(input("Enter col[1,3] number: "))
            if(col<1 or col>3):
                tmp = input("Invalid column number, press anykey to continue...")

        if(board[row-1][col-1]!=2):
            input("The cell is already occupied! Press anykey to try again..")
        else:
            board[row-1][col-1]=turn
            turn = (turn+1)%2
        check()

def print_welcome():
    print("Welcome to TIC-Tac-Toe Game!")
    input("Press Anykey to Play the game..")

def print_winner():
    os.system('clear')
    print("::::::::Tic Tac Toe:::::::\n\n")
    print_board()
    if winner >=0 and winner <=1:
        print(f"\n\n{vals[winner]} is the winner!!!\n")
    else:
        print("Match Draw!!!")

def main():
    print_welcome()
    play()
    print_winner()

if __name__ == "__main__":
    main()