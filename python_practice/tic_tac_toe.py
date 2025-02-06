board = ["" for x in range(0,9)]

def print_row():
    print(f"| {board[0] or 1} | {board[1] or 2} | {board[2] or 3} |")
    print(f"| {board[3] or 4} | {board[4] or 5} | {board[5] or 6} |")
    print(f"| {board[6] or 7} | {board[7] or 8} | {board[8] or 9} |")

print_row()

winning_combinations = [[0,1,2],
                        [3,4,5],
                        [6,7,8],
                        [0,3,6],
                        [1,4,7],
                        [2,5,8],
                        [0,4,8],
                        [2,4,6]]

def is_winner():
    for comb in winning_combinations:
        if all(board[i] =='x' for i in comb):
            return True
        if all(board[i] =='o' for i in comb):
            return True

user_choice = input("Enter a choice (x or o): ").lower()

if user_choice != 'x' and user_choice != 'o':
    print("Enter valid choice")

for turn in range(9):
    move = int(input("Enter a cell (1-9): "))
    if board[move-1] == 'x' or board[move-1] == 'o':
        print("You used that cell already")
        continue
    elif move not in range(1,10):
        print("Enter valid cell")
        continue
    else:
        board[move-1] = user_choice
        print_row()
        if turn == 8 and not is_winner():
            print("It's a draw")
        if user_choice == 'x':
            user_choice = 'o'
        elif user_choice == 'o':
            user_choice = 'x'
        if is_winner():
            print("You won")
            break