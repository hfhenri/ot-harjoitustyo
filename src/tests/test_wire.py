import unittest
from simulation import Simulation
from pixels.wire import Wire
from pixels.fire import Fire


class TestWire(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation(5, 5)

    def test_powered_by_fire(self):
        wire = Wire(2, 2)
        fire = Fire(2, 3)
        self.simulation.add_pixel(wire)
        self.simulation.add_pixel(fire)
        self.simulation.simulate()
        self.assertEqual(wire.power, Wire.FIRE_POWER)

    def test_power_decay(self):
        wire = Wire(2, 2)
        self.simulation.add_pixel(wire)
        wire.power = Wire.FIRE_POWER
        for _ in range(Wire.FIRE_POWER + 1):
            self.simulation.simulate()
        self.assertEqual(wire.power, 0)

    def test_no_self_sustain(self):
        w1 = Wire(1, 2)
        w2 = Wire(2, 2)
        self.simulation.add_pixel(w1)
        self.simulation.add_pixel(w2)
        w1.power = Wire.FIRE_POWER
        for _ in range(Wire.FIRE_POWER * 2):
            self.simulation.simulate()
        self.assertEqual(w1.power, 0)
        self.assertEqual(w2.power, 0)
