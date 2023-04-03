from hello_mdelgert.hello import get_messag

def test_hello():
    helloValue = get_messag()
    assert helloValue == 'hello world!'