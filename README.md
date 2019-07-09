This repository contains code to create a simple ludo simulator in Python to settle a bet between Pip and Anna.

The root folder contains this 'README', a 'TermsOfBet' file, and the source code that executes when running the ludo simulator. The 'analysis' folder contains code that is used to run the ludo simulator a set number of times, and determine the outcome of the bet. The 'tests' folder contains unit tests (to be run in the 'pytest' framework: follow the instructions in the 'runTest.py' file) for confirming the source code is functioning as expected. To run these tests, navigate to the local folder where you have cloned or installed this repository, launch python, and run:
```
import pytest
pytest.main(['ludoSim/tests/test_ludo.py'])
```
To run a game of ludo, navigate to the local folder where you have cloned or installed this repository, launch python, and run:
```
from ludoSim import *
b = Board() # look at the optional input args to set the Board object however you'd like
b.playGame()
```

*Note, this package was created within the Anaconda 5.3.0 distribution (running Python 3.7.0), and imports some packages native to Anaconda 5.3.0. For best results, run this code within Anaconda 5.3.0*