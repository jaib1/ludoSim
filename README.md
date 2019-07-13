This repository contains code to create a simple ludo simulator in Python to settle a bet between Pip and Anna.

The root folder contains this `README.md`, a file (`TermsOfBet.md`) outlining the terms of the bet, the source code that executes when running the ludo simulator, and an image (`StandardLudoBoard.png`) containing the standard ludo board used and the positions favored by Anna and Pip for the bet.

The `analysis` folder contains code (in `analysis/gameAnalysis.py`) that is used to run 10000 games of ludo in order to determine the outcome of the bet. Running the `analysis/gameAnalysis.py` script to run 10000 games and display results took less than a minute on a Windows10 PC with an Intel core i5-6500 CPU with 16 GB DDR4-2133 RAM. Saved data from running that script exists in the `analysis/gamesResults.out` file. The data from that file can be loaded by following the instructions at the bottom of the `analysis/gameAnalysis.py` file. The `analysis` folder also contains saved figures showing results from that data.

The `tests` folder contains unit and integration tests for confirming the source code is functioning as expected. (These tests are to be run in the pytest package testing framework: to run these tests, follow the instructions in the `runTest.py` file.) 

To run a game of ludo, navigate to the local folder where you have cloned or installed this repository, launch python, and run:
```
from ludoSim import *
b = Board() # look at the optional input args to set the board however you'd like
b.playGame()
```

*Note, this package was created using the Anaconda (5.3) package manager distribution (running Python 3.7), and imports some packages native to Anaconda. For best results, download and install [Anaconda](https://www.anaconda.com/distribution), navigate to the local folder where you have cloned or installed this ludoSim repository, and in your conda terminal run:*

*`conda activate ludoSim_env`*

*to activate the environment with the appropriate package dependencies which were used at the time this package was created*

