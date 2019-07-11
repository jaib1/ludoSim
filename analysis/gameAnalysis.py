# This script contains code to run analysis on a series of ludo games.
# Initially written to run analysis to determine the outcome of the bet between
# Pip and Anna.

from ludoSim import *
import cProfile
import pstats
import timeit
import shelve
import numpy as np
import matplotlib.pyplot as plt

## profiled = cProfile.run('b.playGame()')

boards = [] # empty list which will contain a Board object for each game run
wins = 0 # represents player1's wins
scores = np.zeros((2,10000)) # represents scores for both players for all games
hits = np.zeros((2,10000)) # represents hits for both players for all games
sixes = np.zeros((2,10000)) # represents number of rolled sixes for both players for all games

# run 10000 games:
tic = timeit.default_timer()
for game in range(0,10000):
    boards[game] = Board()
    boards[game].playGame()

    # see who won
    if boards[game]._Board__winner == 1:
        wins+=1

    # get scores
    scores[0][game] = boards[game]._Board__scores[0]
    hits[0][game] = boards[game]._Board__hits[0]

    # get number of rolled sixes
	p0Turns = [i for i,x in enumerate(b._Board__playerTurns) if x==1]
	numP0Sizes = len([i for i in b._Board__rolls[i] if i in p0Turns and b._Board__rolls[i]==6])




toc = timeit.default_timer()
print(toc-tic)

# save data
filename = 'ludoSim/analysis/gamesResults.out'
shelf = shelve.open(filename, 'n')
shelf[''] = globals()['']
shelf.close()

# to load data, run:
# `shelf = shelve.open(filename)`
# `globals()[''] = shelf['']`
# `shelf.close()`