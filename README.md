This repository contains code to create a simple ludo simulator in Python to settle a bet between Pip and Anna.

The root folder contains this 'README', a 'TermsOfBet' file, and the source code that executes when running the ludo simulator. 

The 'analysis' folder contains code that is used to run the ludo simulator a set number of times and determine the outcome of the bet, and figures showing results. The `analysis/gameAnalysis.py` script contains information and code for running a set number of 2 player games, with those players taking the positions of 'player 0' and 'player 1' (see https://github.com/jaib1/ludoSim/blob/master/StandardLudoBoard.png). Running the `analysis/gameAnalysis.py` script to run 10000 games and display results should take less than a minute on a computer with a modern cpu and >= 16 gb RAM. Saved data from running 10000 simulations also already exists in the `analysis/gamesResults.out` file. To load that data and see the results, follow the instructions at the bottom of the `analysis/gameAnalysis.py` file.

The 'tests' folder contains unit tests for confirming the source code is functioning as expected. (These tests are to be run in the 'pytest' framework: to run these tests, follow the instructions in the 'runTest.py' file) 

To run a game of ludo, navigate to the local folder where you have cloned or installed this repository, launch python, and run:
```
from ludoSim import *
b = Board() # look at the optional input args to set the board however you'd like
b.playGame()
```

*Note, this package was created using the Anaconda package manager distribution (5.3.0, running Python 3.7.0), and imports some packages native to Anaconda. For best results, download and install (Anaconda)[https://www.anaconda.com/distribution], navigate to the local folder where you have cloned or installed this repository, and in your conda terminal run:
`conda activate ludoSim_env`
to activate the environment with the appropriate package dependencies which were used at the time this package was created*

