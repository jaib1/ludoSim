# To run tests for the ludoSim package, follow the below instructions:
# In the directory containing the 'ludoSim' folder, run the following two lines
# to import the ludoSim and pytest packages:
from ludoSim import *
import pytest
# then, within the same python session, navigate to the 'ludoSim/tests' folder
# and run the following line:
pytest.main(['test_ludo.py'])