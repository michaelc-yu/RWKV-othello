

# takes a board and represents it with 8 tokens
def tokenize_board(board):
    res = []
    for row in board:
        total = 0
        exp = 7
        for digit in row:
            if digit == -1:
                digit = 2
            total += digit * (3**exp)
            exp -= 1
        res.append(total)
    return res
