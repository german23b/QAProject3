from test1 import *
from test2 import *
from test3 import *


class TestUI:
    def test_1(self):
        acutal = test1()
        assert acutal == False

    def test_2(self):
        acutal = test2()
        assert acutal == False

    def test_3(self):
        test3()
