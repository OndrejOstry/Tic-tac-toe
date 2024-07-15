"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Ondřej Ostrý
email: ondrejostry@gmail.com
discord: ondrejostry
"""

#POZDRAV HRÁČE + VYSVĚTLENÍ PRAVIDEL
def greetings():
    print(f"""Welcome to Tic Tac Toe
{"=" * 40}
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
 * horizontal
 * vertical or
 * diagonal row
{"="*40}
Let's start the game
{"-"*40}""")

#VYPÍŠE HRACÍ POLE
def print_board(board):
    for row in board:
        print("+---+---+---+")
        print("| "+" | ".join(row)+" |")   #PŘIDAT MEZERY
    print("+---+---+---+")

#ZJIŠTĚNÍ VÝHERCE
def check_winner(board, player):
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    for column in range(3):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

#SPOŠTĚNÍ HRY
def main():
    board = [[" " for i in range(3)]for i in range(3)]  #VYTVORIT 2D POLE, PŘIDAT FOR LOOP MISTO ROZEPSANE  
    players = ["x", "o"]
    current_player = players[0]
    moves_total = 0
    greetings()
    print_board(board)
    
    while True:                    #CYKLUS DOKUD NEKDO NEVYHRAJE
        move = input(f"Player {current_player} | Please enter your move number: ")
        
        if not move.isdigit():     #CHYBA ZADNÍ ZNAKU
            print("Cannot process your request. Enter a number between 1 and 9.")
            continue
        
        move = int(move)
        
        if 1 < move > 9:     #CHYBA ZADANÍ VĚTŠÍHO ČÍSLA
            print("Invalid move. Please enter a number between 1 and 9.")
            continue
        
        #ČÍSLO 5 --- [[ _ _ _ ][ _ 5 _ ][ _ _ _ ]] TO ZNAMENA BOARD[1][1]
        row = (move - 1) // 3
        column = (move - 1) % 3
        
        if board[row][column] != " ":               #JIŽ OBSAZENÉ POLE
            print("Already Taken! Choose another position!")
            continue

        board[row][column] = current_player
        moves_total += 1
        print_board(board)

        if check_winner(board, current_player):
            print(f"Congratulations, the player {current_player} WON !")
            break

        if moves_total == 9:          #PLNÉ POLE = REMIZA
            print("It is a draw!")
            break
        
        current_player = players[(players.index(current_player) + 1) % 2] #ZMĚNA HRÁČE

main()