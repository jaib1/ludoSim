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

tic = timeit.default_timer()
for game in range(0,100):
    b = Board()
    b.playGame()
    print('Game', game)

toc = timeit.default_timer()
print(toc-tic)