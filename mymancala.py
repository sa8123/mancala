# This program has two player classes. Each player class is supplied with calculate_utility
# and alphabeta_parameters where utility function returns the likeness of the current state
# based on Piece count and score count and returns their sum which is either positive or
# negative. The alphabeta function gives the game state information on how much the game
# needs to check in terms of depth. Higher, the time higher the depth will be. Among these
# players each player has same utility function but different alphabeta function in order
# to test which strategies might be better.
# @author Sudip Aryal, Ashish Rajthala
# @date March 22, 2020

from mancala import *
import random, re, time

class FirstPlayer(mancala_player):
    # This should return the utility of the given boardstate.
    # It can access (but not modify) the to_move and _board fields.
    def calculate_utility(self, boardstate):
        return simple_utility(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        # This should return a tuple of (cutoffDepth, cutoffTest, evalFn)
        # where any (or all) of the values can be None, in which case the
        # default values are used:
        #        cutoffDepth default is 4
        #        cutoffTest default is None, which just uses cutoffDepth to
        #            determine whether to cutoff search
        #        evalFn default is None, which uses your boardstate_utility_fn
        #            to evaluate the utility of board states.
        if remainingTime >= 600:
            return (6, None, None)
        elif 300 <= remainingTime < 600:
            return (4, None, None)
        else:
            return (2, None, None)

def simple_utility(boardstate):
    first = boardstate.PlayerPieceCount(opponent(boardstate.to_move))
    second = boardstate.PlayerPieceCount(boardstate.to_move)
    final = second - first
    return boardstate.default_utility2() + final

class SecondPlayer(mancala_player2):
    # Second player to play the game
    # This class has methods calculate_utilty and alphabeta_parameters.
    def calculate_utility(self, boardstate):
        return simple_utility(boardstate)

    def alphabeta_parameters(self, boardstate, remainingTime):
        if remainingTime >= 300:
            return (6, None, None)
        elif 150 <= remainingTime < 300:
            return (4, None, None)
        else:
            return (2, None, None)

def simple_utility(boardstate):
    first = boardstate.PlayerPieceCount(opponent(boardstate.to_move))
    second = boardstate.PlayerPieceCount(boardstate.to_move)
    final = second - first
    return boardstate.default_utility2() + final

# After "running" this module, to play a game type:
play_mancala(None, 450, FirstPlayer("Sudip"), SecondPlayer("Ashish"))

# The above plays your player against itself, using the names
# Fred and Bob.  You could try having two different classes that
# use different strategies and play them against each other.



