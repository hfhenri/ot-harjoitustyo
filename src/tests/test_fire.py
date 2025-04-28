import unittest
from simulation import Simulation
from pixels.fire import Fire
from pixels.wood import Wood
from pixels.oil import Oil

class TestFire(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation(2, 2)