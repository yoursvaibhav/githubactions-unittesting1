import pytest 

from calc import add, sub, mul, div

def test_add():
    #compare actual output and expected output
    assert add(2,3) == 5

def test_sub():
    assert sub(10,4) == 6

def test_mul():
    assert mul(5,2) == 10

def test_div():
    assert div(10/2) == 5