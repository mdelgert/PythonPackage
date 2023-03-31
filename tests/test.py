
#https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
#https://docs.python.org/3/library/unittest.html
#https://docs.pytest.org/en/stable/

import unittest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from src.example_package_mdelgert.example import egg

class TestStringMethods(unittest.TestCase):

    def test_egg(self):
        eggValue = egg()
        print(eggValue)
        self.assertEqual(eggValue, 'Hello egg!')

if __name__ == '__main__':
    unittest.main()