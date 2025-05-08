import unittest
from simulation import Simulation
from pixels.acid import Acid
from pixels.stone import Stone
from pixels.wood import Wood
from pixels.sand import Sand
from pixels.oil import Oil
from pixels.empty import Empty


class TestAcid(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation(5, 5)

    def test_acid_corrosion(self):
        acid = Acid(2, 2)
        stone = Stone(2, 1)
        wood = Wood(1, 2)
        sand = Sand(3, 2)
        oil = Oil(2, 3)
        self.simulation.add_pixel(acid)
        self.simulation.add_pixel(stone)
        self.simulation.add_pixel(wood)
        self.simulation.add_pixel(sand)
        self.simulation.add_pixel(oil)
        self.simulation.simulate()
        self.assertIsInstance(self.simulation.get_pixel(2, 1), (Acid, Empty))
        self.assertIsInstance(self.simulation.get_pixel(1, 2), (Acid, Empty))
        self.assertIsInstance(self.simulation.get_pixel(3, 2), (Acid, Empty))
        self.assertIsInstance(self.simulation.get_pixel(2, 3), (Acid, Empty))

        count = 0
        for (x, y) in [(2, 1), (1, 2), (3, 2), (2, 3)]:
            if isinstance(self.simulation.get_pixel(x, y), (Acid, Empty)):
                count += 1
        self.assertEqual(count, 4)

    def test_acid_flows(self):
        acid = Acid(2, 0)
        self.simulation.add_pixel(acid)
        self.simulation.simulate()
        self.assertEqual((acid.x, acid.y), (2, 1))
