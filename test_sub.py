from sub import say_hello

def test_sub_no_p():
    assert say_hello() == "Hello, SubUx"

def test_sub_every():
    assert say_hello("babu") == "Hello, babu"