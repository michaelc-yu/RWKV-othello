

# 1 is black, -1 is white, and 0 is empty
# scores will be calculated from the perspective of black
# (higher score means black is doing well)
class Othello:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.board[3][3] = -1
        self.board[4][4] = -1
        self.board[4][3] = 1
        self.board[3][4] = 1

    def get_board(self):
        return self.board

    def draw_board(self):
        for row in self.board:
            print("   ".join(str(item) for item in row))

    def get_score(self, color):
        # (# black pieces - # white pieces)
        score = sum(sum(row) for row in self.board)
        # print(score)
        return score if color==1 else -score
    
    def get_legal_moves(self, color):
        legal_moves = []
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 0:
                    if self.is_valid_move(color, (x,y)):
                        legal_moves.append((x,y))
        return legal_moves
    
    def is_valid_move(self, color, position):
        x,y = position
        if x<0 or y<0 or x>=8 or y>=8 or self.board[x][y]!=0:
            return False
        dirs = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        for (i,j) in dirs:
            if self.search(color, position, i, j, flip=False):
                return True
        return False

    # returns True if valid move and makes move
    # returns False if invalid move
    def make_move(self, color, position):
        x,y = position[0], position[1]
        if x<0 or y<0 or x>=8 or y>=8 or self.board[x][y] != 0:
            return False
        self.board[x][y] = color
        flipped = False
        # now explore in all 8 directions
        # if there is any number of opponent stones followed by our stone, then flip all opponent stones
        dirs = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        for (i,j) in dirs:
            if self.search(color, position, i, j, flip=True):
                flipped = True

        if flipped:
            return True
        else:
            self.board[x][y] = 0
            return False

    def search(self, color, position, i, j, flip=False):
        can_capture = False
        x,y = position[0], position[1]
        dx,dy = x+i, y+j
        opponent_stones = 0

        while dx>=0 and dy>=0 and dx<8 and dy<8 and self.board[dx][dy]==-color:
            opponent_stones+=1
            dx,dy = dx+i, dy+j
        if dx>=0 and dy>=0 and dx<8 and dy<8 and self.board[dx][dy]==color and opponent_stones:
            can_capture = True
            if flip:
                dx,dy = x+i, y+j
                while dx>=0 and dy>=0 and dx<8 and dy<8 and self.board[dx][dy]==-color:
                    self.board[dx][dy]=color
                    dx,dy = dx+i, dy+j
        return can_capture

# o = Othello()
# o.draw_board()
# o.get_score()
# color = 1 # black goes first
# for _ in range(20):
#     while True:
#         bw = "Black" if color==1 else "White"
#         print(f"{bw}'s turn")
#         move = input("Make a legal move: (row, col): ")
#         x,y = map(int, move.split(","))
#         if o.make_move(color, [x,y]):
#             color*=-1
#             o.draw_board()
#             break


