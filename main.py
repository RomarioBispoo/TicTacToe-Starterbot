#!/usr/bin/env python3


import sys
import random
from util import *


def go():
    bot = BotStarter()
    parser = BotParser(bot)
    parser.run()


class BotStarter:
    def __init__(self):
        random.seed()
    
    def doMove(self, state):
        moves = state.getField().getAvailableMoves()
        if (len(moves) > 0):
            return moves[random.randrange(len(moves))]
        else:
           return None
class Game:
    """A game has a utility for each
    state and a terminal test. To create a game, subclass this class and implement actions,
    result, utility, and terminal_test. You may override display and
    successors or you can inherit their default methods. You will also
    need to set the .initial attribute to the initial state; this can
    be done in the constructor."""

    def actions(self, state):
        """Return a list of the allowable moves at this point."""
        raise NotImplementedError

    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        raise NotImplementedError

    def utility(self, state, player):
        """Return the value of this final state to player."""
        raise NotImplementedError

    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        return not self.actions(state)

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move

    def display(self, state):
        """Print or otherwise display the state."""
        print(state)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self, *players):
        """Play an n-person, move-alternating game."""
        state = self.initial
        while True:
            for player in players:
                move = player(self, state)
                state = self.result(state, move)
                #self.display(state)
                if self.terminal_test(state):
                    #self.display(state)
                    return self.utility(state, self.to_move(self.initial))

class UltimateTicTacToe (Game):
    __bot = None
    __currentState = None
    __field = None

    def __init__(self):
        self.__bot = BotParser()
        self.__currentState = BotState()
        self.__field = Field()

    def actions(self,state):
        moves = state.getField().getAvailableMoves()
        return moves

    def result(self, state, move):
        fieldcpy = self.__currentState.getField()
        return fieldcpy

    def to_move(self, state):
        player = self.__currentState.getRoundNumber() #return move number ?
        if (player % 2 == 0):
            return self.__field.getMyId()
        else:
            return self.__field.getOpponentId()

    def eval_function(self):
        raise NotImplementedError #dá pra contar a quantidade de quase vitórias para cada player
    def compute_utility(self):
        raise NotImplementedError # checagem pra ver se o jogo terminou: # vitória, derrota ou empate. (1, -1, 0) de recompensa, respectivamente

    def terminal_test(self): # teste para checar se o jogo terminou
        raise NotImplementedError

if __name__ == '__main__':
    go()
