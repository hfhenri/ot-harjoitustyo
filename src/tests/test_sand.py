import unittest
from pixels.sand import Sand
from simulation import Simulation


class TestSand(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation(100, 80)

    def test_sand_falls_down(self):
        sand = Sand(0, 0)
        self.simulation.add_pixel(sand)
        self.simulation.simulate()

        self.assertEqual((sand.x, sand.y), (0, 1))

    def test_sand_stacks(self):
        sand1 = Sand(5, 78)
        sand2 = Sand(5, 79)
        self.simulation.add_pixel(sand1)
        self.simulation.add_pixel(sand2)
        self.simulation.simulate()

        self.assertTrue((sand1.x, sand1.y) == (4, 79)
                        or (sand1.x, sand1.y) == (6, 79))
