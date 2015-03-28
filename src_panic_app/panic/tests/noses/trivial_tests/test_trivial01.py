import unittest

class TC(unittest.TestCase):
    pass


class TrivialTestCase(TC):
    def test_01_diquesi(self):
        assert "diquesi" == "diquesi"

    def test_02_diqueno(self):
        assert "diqueno" == "diqueno"

    def test_03_faildiquesi(self):
        assert "diqueSI" == "diquesi"

    def test_04_diqueNO(self):
        assert "diqueNO" == "diquesi"    
