import copy
import random
from othello import Othello
from mcts import MCTS

NUM_SIMULATIONS = 3
MAX_DEPTH = 5
NUM_GAMES = 1
NUM_MOVES = 20

data = []

for _ in range(NUM_GAMES):
    game = Othello()
    game.draw_board()
    mcts = MCTS(game, simulations=NUM_SIMULATIONS, max_depth=MAX_DEPTH)
    color = 1

    for _ in range(NUM_MOVES):
        b_w = "Black" if color==1 else "White"
        print(f"{b_w}'s turn")

        datum = {}
        datum["current_board_position"] = copy.deepcopy(game.get_board())

        best_move, mcts_cot = mcts.best_move(color)

        datum["mcts_cot"] = copy.deepcopy(mcts_cot)
        datum["best_move"] = copy.deepcopy(best_move)

        game.make_move(color, best_move)
        game.draw_board()
        print(game.get_score(1)) # get black score

        # only store data for black moves
        if color==1:
            data.append(datum)

        color = -color


print(data)
