import unittest
from pixels.stone import Stone
from pixels.lava import Lava
from pixels.water import Water
from pixels.steam import Steam
from simulation import Simulation


class TestSand(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation(100, 80)

    def test_lava_flows(self):
        lava1 = Lava(5, 77)
        lava2 = Lava(5, 78)
        lava3 = Lava(5, 79)

        self.simulation.add_pixel(lava1)
        self.simulation.add_pixel(lava2)
        self.simulation.add_pixel(lava3)

        for _ in range(15):
            self.simulation.simulate()

        self.assertTrue((lava1.y, lava2.y, lava3.y) == (79, 79, 79))

    def test_lava_boils_water(self):

        self.simulation.add_pixel(Stone(49, 79))
        self.simulation.add_pixel(Stone(52, 79))

        lava = Lava(50, 79)
        water = Water(51, 79)

        self.simulation.add_pixel(water)
        self.simulation.add_pixel(lava)

        self.simulation.simulate()

        self.assertTrue(isinstance(self.simulation.get_pixel(51, 78), Steam))