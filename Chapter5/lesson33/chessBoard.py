def promising(i, col):
    for k in range(i):
        # Check if queens are in the same column or diagonal
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            return False
    return True

def n_queens(i, col):
    if promising(i, col):
        if i == len(col) - 1:
            print(col)  # Print the solution
        else:
            for j in range(len(col)):
                col[i + 1] = j  # Place queen in the next row
                n_queens(i + 1, col)

# Input for the number of queens
N = int(input("Input the number of queens: "))
n_queens(-1, [-1] * N)
