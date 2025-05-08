import unittest
from simulation import Simulation
from pixels.sand import Sand
from pixels.water import Water
from pixels.empty import Empty


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

    def test_add_and_remove_pixel(self):
        sand = Sand(1, 1)
        self.simulation.add_pixel(sand)
        self.assertIs(self.simulation.get_pixel(1, 1), sand)
        self.assertIn(self.simulation.get_pixel(1, 1),
                      self.simulation.movement_queue)

        self.simulation.remove_pixel(1, 1)
        cell = self.simulation.get_pixel(1, 1)
        self.assertIsInstance(cell, Empty)
        self.assertIn(self.simulation.get_pixel(1, 1),
                      self.simulation.movement_queue)

    def test_resize_grid(self):
        self.simulation.resize_grid(3, 4)
        self.assertEqual(self.simulation.width, 3)
        self.assertEqual(self.simulation.height, 4)

        for x in range(3):
            for y in range(4):
                self.assertIsInstance(self.simulation.get_pixel(x, y), Empty)

    def test_move_pixel(self):
        sand = Sand(0, 0)
        self.simulation.remove_pixel(1, 1)
        sand.x, sand.y = 2, 1
        self.simulation.add_pixel(sand)
        self.simulation.clear_queues()
        self.simulation.simulate()
        self.assertEqual((sand.x, sand.y), (2, 2))
