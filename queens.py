# 8 Queens solver
# Juan Cruz Dal Bello - Portfolio Project


def print_board(board):
    """
    Prints the board on console.
    """
    print()
    for index_row, row in enumerate(board):
        for index_squere, squere in enumerate(row):
            print(squere, end=' ')
            if index_squere != 7:
                print('|', end=' ')
        print()
        if index_row != 7:
            print('--+---+---+---+---+---+---+---')
    print()


def print_queens_coordinates(board):
    """
    Prints the coordniates x and y of every queen on the board.
    """
    print('\n-------- LOCATION OF QUEENS ON THE BOARD (row, column) --------\n')

    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            if board[i][j] == 1:
                print(f'({i+1}, {j+1})')


def all_queens_placed(board):
    """
    If all 8 queens are positioned on the board return True, else return False.
    """
    amount_of_queens = 0

    for row in board:
        for squere in row:
            if squere == 1:
                amount_of_queens += 1
    
    if amount_of_queens >= 8:
        return True
    
    return False


def valid(board, position):     # position -> (x, y)
    """
    Checks if a position is valid to put a queen.
    """    
    # Check for queens on the same line
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            # Same row
            if i == position[0] and board[i][j] == 1:
                return False
            
            # Same column
            if j == position[1] and board[i][j] == 1:
                return False
            
            # Same left-to-right diagonal
            if i-j == position[0]-position[1] and board[i][j] == 1:
                return False

            # Same right-to-left diagonal
            if i+j == position[0]+position[1] and board[i][j] == 1:
                return False
    
    return True


def solve(board):
    """
    Solves the 8 queens board recursively, stops once all the queens are positioned on the board.
    """    
    if all_queens_placed(board):
        return True
    
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            if valid(board, (i, j)):
                board[i][j] = 1

                if solve(board):
                    return True
                
                board[i][j] = 0

    return False


def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print('\n-------- SOLUTION --------')
    solve(board)
    print_board(board)
    print_queens_coordinates(board)
    input()


# ----------------------------------------------------

if __name__ == '__main__':
    main()
