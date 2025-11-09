##  Mini Project TicTacToe

#   Representing the Game Board
borad = [' ' for _ in range(9)]  # A list to hold the board state
print("Welcome to TIC TAC TOE!")

#   Displaying the Game Board
def display_board():
    print("TIC TAC TOE")
    print("****************")
    print(f"*  {borad[0]} | {borad[1]} | {borad[2]}   *")
    print("* ---|---|---  *")
    print(f"*  {borad[3]} | {borad[4]} | {borad[5]}   *")
    print("* ---|---|---  *")
    print(f"*  {borad[6]} | {borad[7]} | {borad[8]}   *")
    print("****************")
display_board()

#   Getting Player Input
def player_input(player):
    while True:
        position = input(f"Player {player}, enter your position (1-9): ")
        if position.isdigit() and 1 <= int(position) <= 9:
            position = int(position) - 1
            if borad[position] == ' ':
                borad[position] = player
                break
            else:
                print("Position already taken. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

#   Checking for a Winner
def check_win(board, player):
    win_conditions =[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

#   Checking for a Tie
def check_tie(board):
    if ' ' not in board:
        return True
    return False

#   The Main Game Loop
def play():
    player1 = 'X'
    player2 = 'O'
    while True:
        player_input(player1)
        display_board()
        if check_win(borad, player1):
            print("Player X wins!")
            break
        if check_tie(borad):
            print("It's a tie!")
            break
        player_input(player2)
        display_board()
        if check_win(borad, player2):
            print("Player O wins!")
            break
        if check_tie(borad):
            print("It's a tie!")
            break

play()

