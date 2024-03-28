def run_ttt_game():
    # here is where the actual game plays out
    turn = 'X'
    grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] # 3 empty spaces per line
    while True:
        print(f'It is the turn of "{turn}"') # this is how to put a value into a text string from inside any variable! 
        # you just use the f-string syntax and put curly braces {}
        print_grid(grid) # of course i had to print the grid..... i forgot lmao
        row = input('what row? ')
        row = int(row)
        col = input('what column? ')
        col = int(col)
        if not ((0 <= row < 3) and (0 <= col < 3)):
            print('Bad values!!! try again')
            continue # this skips back to the start of the WHILE loop

        if grid[row][col] != ' ': 
            print('This cell is not free. try again')
            continue

        print()
        # now we can place the symbol
        grid[row][col] = turn

        # now check if anybody wins
        winner = who_wins(grid)
        if winner is not None:
            print_grid(grid) # don't forget to show the final grid!!!
            print(f'"{winner}" wins!!!! Congratulations')
            break   # this means exit the `while` loop

        # if no one wins, go to the next player
        # here we invert X and O -->  becomes O if it was X before,   becomes X if it was O before
        turn = 'O' if turn == 'X' else 'X'
    print('Game over')

def print_grid(grid):
    # we call this whenever we want to show the grid
    # grid is a list of 3 lines, and each line is a list with 3 symbols
    for line in grid:
        print(' '.join(line))   # this is how to print a list by separating it with spaces

def who_wins(grid):
    def three_in_a_row():
        # we call this every time to know if anybody wins
        # 3 in a row, horizontal
        for line in grid:
            if line[0] == line[1] == line[2]: # 'X X X' or 'O O O'
                return line[0]

        # 3 in a row, vertical
        for i in range(3):
            if grid[0][i] == grid[1][i] == grid[2][i]:
                return grid[0][i]

        # diagonals
        if grid[0][0] == grid[1][1] == grid[2][2]:
            return grid[0][0]

        if grid[0][2] == grid[1][1] == grid[2][0]:
            return grid[0][2]

        return None

    winner = three_in_a_row()

    # return winner, but don't try telling that 'space' is the winner
    return winner if winner != ' ' else None
        


def main():
    print("Welcome to Tic Tac Toe")
    print("developed by alessandro with help from rylmovuk")
    print()
    print()
    run_ttt_game()
    print("Press SPACE to go back")
    import runpy
    answer = input()
    if answer == "pl":
        project = runpy.run_path(f"./explorer.py")
        back_to_explorer = project["main"]
        back_to_explorer()
        
