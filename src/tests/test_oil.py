import unittest
from pixels.stone import Stone
from pixels.lava import Lava
from pixels.water import Water
from pixels.oil import Oil
from pixels.steam import Steam
from simulation import Simulation


class TestOil(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation(2, 2)

    def test_oil_floats(self):
        water1 = Water(1, 1)
        water2 = Water(0, 1)
        oil = Oil(0, 0)
        self.simulation.add_pixel(water1)
        self.simulation.add_pixel(water2)
        self.simulation.add_pixel(oil)

        self.simulation.simulate()

        self.assertTrue(oil.y == 0)
