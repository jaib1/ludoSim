# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:40:50 2019

@author: Jai
"""

from ludoSim import *

import cProfile

import pstats

import timeit

b = Board()

profiled = cProfile.run('b.playGame()')
wins = 0
tic = timeit.default_timer()
for game in range(0,100):
    b = Board()
    b.playGame()
    if b._Board__winner == 1:
        wins+=1
    print('Game', game)

toc = timeit.default_timer()
print(toc-tic)