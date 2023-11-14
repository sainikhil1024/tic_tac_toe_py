def print_instructions():
    print("Welcome to Tic-Tac-Toe!")
    print("To play, enter a number from 1 to 9 to place your symbol on the board as shown below:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("Let's start!\n")


def print_board(squares):
    print(f" {squares[0]} | {squares[1]} | {squares[2]} ")
    print(" -----------")
    print(f" {squares[3]} | {squares[4]} | {squares[5]} ")
    print(" -----------")
    print(f" {squares[6]} | {squares[7]} | {squares[8]} ")


def check_win(player, squares, win_conditions):
    for a, b, c in win_conditions:
        if squares[a] == squares[b] == squares[c] == player:
            return True
    return False


def replay():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            return True
        elif play_again == 'no':
            return False
        else:
            print("Please enter 'yes' or 'no'.")
            continue


def play_game(win_conditions):
    print_instructions()
    while True:
        squares = [' '] * 9
        players = 'XO'
        current_player = players[0]

        while True:
            print_board([str(i) if val == ' ' else val for i, val in enumerate(squares, start=1)])
            move = input(f"{current_player}'s turn. Enter your move (1-9): ")

            if not move.isdigit() or not 1 <= int(move) <= 9 or squares[int(move) - 1] != ' ':
                print("Invalid move! Try again.")
                continue

            squares[int(move) - 1] = current_player
            if check_win(current_player, squares, win_conditions):
                print_board(squares)
                print(f"Congratulations! {current_player} wins!")
                break

            if ' ' not in squares:
                print_board(squares)
                print("It's a tie!")
                break

            current_player = players[1] if current_player == players[0] else players[0]

        if not replay():
            print("Thanks for playing!")
            break


win_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontals
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # verticals
    (0, 4, 8), (2, 4, 6)  # diagonals
]

play_game(win_conditions)
