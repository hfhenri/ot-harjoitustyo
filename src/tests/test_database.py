import os
import tempfile
import unittest
import database
from simulation import Simulation


class TestDatabaseCRUD(unittest.TestCase):
    def setUp(self):
        fd, self.db_path = tempfile.mkstemp(suffix='.db')
        os.close(fd)
        self.db = database.Database(self.db_path)

    def tearDown(self):
        self.db.close()
        os.remove(self.db_path)

    def test_save_game(self):
        simulation = Simulation(5, 5)
        self.db.save_game("test_game", simulation, 33)

        self.assertTrue(self.db.load_game(1) is not None)

    def test_load_game(self):
        simulation = Simulation(5, 5)
        self.db.save_game("test_game", simulation, 33)

        self.assertEqual(self.db.load_game(1)[0], 5)
        self.assertEqual(self.db.load_game(1)[1], 5)
        self.assertEqual(self.db.load_game(1)[2], 33)
