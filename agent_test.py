"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import isolation
import game_agent

from sample_players import open_move_score, GreedyPlayer
from game_agent import MinimaxPlayer, AlphaBetaPlayer, custom_score
from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        #self.player1 = "Player1"
        self.player1 = game_agent.MinimaxPlayer
   
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)


    def test_MinMax(self):
        self.game.apply_move((2, 3))
        self.game.apply_move((0, 5))
        print(self.game.to_string())

        assert(self.player1 == self.game.active_player)

        legal_moves = self.game.get_legal_moves()
        print(legal_moves)


    def test_minimax_func6(self):
        minimax_player = MinimaxPlayer(search_depth=1, score_fn=custom_score)
        alphabet_player = AlphaBetaPlayer(search_depth=3, score_fn=custom_score)
        other_player = GreedyPlayer()
        state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 43, 57]
        game = isolation.Board(alphabet_player, other_player, width=9, height=9)
        game._board_state = state

        move = alphabet_player.get_move(game, lambda:10)
        print()
        print(game.to_string())
        print(game.get_legal_moves())
        print(move)
        assert(move in [(5, 5)])



if __name__ == '__main__':
    unittest.main()

