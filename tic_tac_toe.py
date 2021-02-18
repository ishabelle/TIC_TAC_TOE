import os
from colorama import Fore, Style, Back

# Initialize the board:
def init_board():
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return board

# Get the player's move:
def get_move(board, player):
    row = 3
    column = 3
    valid_moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    move = input("Please, input position of your move: ")
    if move.upper() == 'quit':
        quit()
    elif move.upper() not in valid_moves:
        print("Position of your move is wrong!")
        return get_move(board, player)
    if "A" in move.upper():
        row = 0
    elif "B" in move.upper():
        row = 1
    elif "C" in move.upper():
        row = 2
    if "1" in move:
        column = 0
    elif "2" in move:
        column = 1
    elif "3" in move:
        column = 2
    if board[row][column] != 0:
        print("Place is already taken. Please, choose another one.")
        return get_move(board, player)
    return (row, column)

# AI can play:
# def get_ai_move(board, player):
#     pass
    
# Implement making a move:
def mark(board, player, row, column):
    try:
        if board[row][column] == 0:
            board[row][column] = player
    except IndexError:
        return
    

# Check for winner:
def has_won(board, player):
    if (board[0][0] == board[0][1] == board[0][2] == player or 
        board[1][0] == board[1][1] == board[1][2] == player or
        board[2][0] == board[2][1] == board[2][2] == player or 
        board[0][0] == board[1][0] == board[2][0] == player or
        board[0][1] == board[1][1] == board[2][1] == player or 
        board[0][2] == board[1][2] == board[2][2] == player or
        board[0][0] == board[1][1] == board[2][2] == player or 
        board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False

# Check for a full board:
def is_full(board):
    if "." in board[0]:
        return False
    elif "." in board[1]:
        return False
    elif "." in board[2]:
        return False
    else:
        return True

# Print board:
board = init_board()
def print_board(board):
    
    # filled_board = init_board()
    # for x in range(len(board)):
    #     for i in range(len(board[0])):
    #         if board[x][i] == 0:
    #             filled_board[x][i] = Fore.WHITE + "."
    #         if board[x][i] == 1:
    #             filled_board[x][i] = Fore.RED + "X"
    #         if board[x][i] == 2:
    #             filled_board[x][i] = Fore.GREEN + "O"
    print(Fore.WHITE + "1   2   3")
    print(Fore.WHITE + "A"  + board[0][0] + Fore.WHITE + "|" + board[0][1] + Fore.WHITE + "|" + board[0][2])
    print(Fore.WHITE + "---+---+---")
    print(Fore.WHITE + "B"  + board[1][0] + Fore.WHITE + "|" + board[1][1] + Fore.WHITE + "|" + board[1][2])
    print(Fore.WHITE + "---+---+---")
    print(Fore.WHITE + "C"  + board[2][0] + Fore.WHITE + "|" + board[2][1] + Fore.WHITE + "|" + board[2][2])
    

# Print result:
def print_result(winner):
    if winner == 0:
        print("It's a tie! \n")
    if winner == 1:
        print("X won! \n")
    if winner == 2:
        print("O won! \n")

# Game logic:
def tictactoe_game(mode):
    if mode == "HUMAN_1 - HUMAN_2":
        board = init_board()
        while not has_won(board, 1) and not has_won(board, 2) and not is_full(board):
            os.system("cls")
            print_board(board)
            row, column = get_move(board, 1)
            mark(board, 1, row, column)
            os.system("cls")
            print_board(board)
            if not has_won(board, 1) and not is_full(board):
                row, column = get_move(board, 2)
                mark(board, 2, row, column)
                print_board(board)

        if has_won(board, 1):
            winner = 1
        elif has_won(board, 2):
            winner = 2
        else:
            winner = 0
        print_result(winner)
        sub_menu()

# Quit game or play again:
def sub_menu():  
    action = input("Do you want play again? Y / N \n")
    while action != "Y" or action != "N":
        if action == "Y" or action == "y":
            main_menu()
        elif action == "N" or action == "n":
            print("\nThank you for your game! Bye!")
            quit()
            break
        else:
            print("Wrong input!")
            action = input("Do you want play again? Y / N \n")

# Main menu:
def main_menu():
    os.system("cls")
    print(Fore.BLACK + Back.WHITE + """
 _ _ _   _   _ _ _       _ _ _   _ _ _   _ _ _       _ _ _   _ _ _   _ _ _  
|_   _| | | |  _ _|     |_   _| |     | |  _ _|     |_   _| |     | |  _ _| 
  | |   | | | |           | |   |  |  | | |           | |   |  |  | | |_    
  | |   | | | |           | |   |  |  | | |           | |   |  |  | |  _|   
  | |   | | | |_ _        | |   |  _  | | |_ _        | |   |  |  | | |_ _  
  |_|   |_| |_ _ _|       |_|   |_| |_| |_ _ _|       |_|   |_ _ _| |_ _ _| 

""")
    print(Style.RESET_ALL) 
    print("Available game modes: \n")
    print("1. HUMAN_1 - HUMAN_2")
    # print('2.HUMAN-AI')
    
    select = input("\nWhich one do you choose? ")
    if select == "quit":
        quit()
    elif select == str(1):
        tictactoe_game("HUMAN_1 - HUMAN_2")
        os.system("cls")
    # elif select == str(2):
   
    else:
        main_menu()


if __name__ == "__main__":
    main_menu()