from baby import *

def test_Baby1():
    baby1 = Baby(20, 15, "Quiet", False)
    assert baby1.hungry == False
    assert baby1.weight == 15
    assert baby1.loudness == "Quiet"
    assert baby1.height == 20

def test_Baby2():
    baby2 = Baby(40, 36, "Quiet", True)
    baby2.eat()
    assert baby2.hungry == False
    assert baby2.weight == 36
    assert baby2.loudness == "Quiet"
    assert baby2.height == 40
    assert baby2.cry() == "waaaaa"