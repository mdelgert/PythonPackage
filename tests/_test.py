#https://realpython.com/pytest-python-testing/
#https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
#https://docs.python.org/3/library/unittest.html
#https://docs.pytest.org/en/stable/

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from src.example_package_mdelgert.example import egg

def test_egg():
        print('Test the egg...')
        eggValue = egg()
        print(eggValue)
        assert eggValue == 'Hello egg!'