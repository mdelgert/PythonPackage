#from src.example_package_mdelgert.example import get_example
from src.example_package_mdelgert import example

def test_egg():
        print('Test the egg...')
        eggValue = example.get_example()
        print(eggValue)
        assert eggValue == 'Hello egg!'