import unittest
from manager import *
from models import *


class TestManager(unittest.TestCase):
    def setUp(self):
        self.rink = Rink(purpose=Purpose.ICESCATING, name="Ice arena", price=200000, country=Country.BRAZIL, year=1999,
                         size_in_sq_m=3000, capasity=200, material="plastic", open_air=True)

        self.stadium = Stadium(purpose=Purpose.FOOTBALL, name="Ali arena", price=350000, country=Country.CHINA,
                               year=2020,
                               size_in_sq_m=7000, capasity=999, real_grass=True, open_air=True)

        self.spring_road = Spring_road(purpose=Purpose.SKIING, name="Springer", price=1200000, country=Country.ENGLAND,
                                       year=2007, size_in_sq_m=23000, capasity=500, height_in_m=25.5,
                                       steepness_in_degrees=60)
        item = [self.rink, self.stadium, self.spring_road]
        self.object_manager = Olympics_manager(item)

    def test_sort_by_name(self):
        self.assertEqual(self.object_manager.sort_by_name(), [self.stadium, self.rink, self.spring_road])

    def test_search_by_capasity(self):
        self.assertEqual(self.object_manager.search_by_capasity(), [self.rink, self.stadium, self.spring_road])

    if __name__ == '__main__':
        unittest.main()
