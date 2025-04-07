import unittest
from simulation import Simulation
from pixels.sand import Sand
from pixels.water import Water


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation(100, 100)

    def test_pixel_swap_works(self):
        pixel1 = Sand(99, 99)
        pixel2 = Water(0, 99)

        self.simulation.add_pixel(pixel1)
        self.simulation.add_pixel(pixel2)

        self.simulation.swap_places(pixel1, pixel2)

        self.assertTrue(isinstance(self.simulation.get_pixel(99, 99), Water))
        self.assertTrue(isinstance(self.simulation.get_pixel(0, 99), Sand))
