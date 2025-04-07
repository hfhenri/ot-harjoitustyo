import unittest
from pixels.water import Water
from simulation import Simulation


class TestSand(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation(100, 80)

    def test_water_falls_down(self):
        water = Water(0, 0)
        self.simulation.add_pixel(water)
        self.simulation.simulate()

        self.assertEqual((water.x, water.y), (0, 1))

    def test_water_flows(self):
        water1 = Water(5, 77)
        water2 = Water(5, 78)
        water3 = Water(5, 79)

        self.simulation.add_pixel(water1)
        self.simulation.add_pixel(water2)
        self.simulation.add_pixel(water3)

        for _ in range(3):
            self.simulation.simulate()

        self.assertTrue((water1.y, water2.y, water3.y) == (79, 79, 79))
