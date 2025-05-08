import unittest
from simulation import Simulation
from pixels.fire import Fire
from pixels.wood import Wood


class TestFire(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation(2, 2)

    def test_fire_spreads(self):
        self.simulation.add_pixel(Fire(1, 1))
        self.simulation.add_pixel(Wood(0, 1))

        for _ in range(10):
            self.simulation.simulate()

        self.assertIsInstance(self.simulation.get_pixel(0, 1), Fire)
