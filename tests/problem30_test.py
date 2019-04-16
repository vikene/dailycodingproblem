import sys
sys.path.insert(0,"../src/")
from problem30 import waterremaining


def test_problem30_1():
    assert waterremaining([2,1,2]) == 1
def test_problem30_2():
    assert waterremaining([3, 0, 1, 3, 0, 5]) == 8



