from example import get_egg

def test_egg():
        print('Test the egg...')
        eggValue = get_egg()
        print(eggValue)
        assert eggValue == 'Hello egg!'