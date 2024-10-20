import copy
import random
from othello import Othello
from tokenizer import tokenize_board


class MCTS:
    def __init__(self, game, simulations=100, max_depth=5):
        self.game = game
        self.simulations = simulations
        self.max_depth = max_depth

    def best_move(self, color):
        legal_moves = self.game.get_legal_moves(color)
        # print(f"legal_moves: {legal_moves}")
        if not legal_moves:
            return None

        move_scores = {move: 0 for move in legal_moves}
        all_mcts_cot = []

        for move in legal_moves:
            total_score = 0
            mcts_cot_list = [] # mcts_cot, score
            for _ in range(self.simulations):
                simulation_score, mcts_cot = self.simulate(move, color)
                total_score += simulation_score
                mcts_cot_list.append(mcts_cot)

            avg_score = total_score / self.simulations
            move_scores[move] = avg_score
            # mcts_cot_list.append(avg_score)
            all_mcts_cot.append(mcts_cot_list)
        
        best_move = max(move_scores, key=move_scores.get)
        return best_move, all_mcts_cot
    
    def simulate(self, move, color):
        simulated_game = copy.deepcopy(self.game)
        simulated_game.make_move(color, move)

        current_color = -color
        depth=0
        mcts_cot = []

        tokenized_board = tokenize_board(copy.deepcopy(simulated_game.board))

        mcts_cot.append([tokenized_board, simulated_game.get_score(color)])

        while depth < self.max_depth and simulated_game.get_legal_moves(current_color):
            random_move = random.choice(simulated_game.get_legal_moves(current_color))
            simulated_game.make_move(current_color, random_move)
            current_color = -current_color
            depth += 1
            tokenized_board = tokenize_board(copy.deepcopy(simulated_game.board))

            mcts_cot.append([tokenized_board, simulated_game.get_score(color)])
        
        final_score = simulated_game.get_score(color)
        return final_score, mcts_cot

