import unittest
from pixels.shared import pixel_from_name, pixel_from_id
from pixels.empty import Empty
from pixels.sand import Sand
from pixels.stone import Stone
from pixels.wood import Wood
from pixels.water import Water
from pixels.lava import Lava
from pixels.oil import Oil
from pixels.fire import Fire
from pixels.steam import Steam


class TestShared(unittest.TestCase):
    
    def test_pixel_from_name(self):
        for cls in (Sand, Water, Stone, Lava, Wood, Oil, Empty, Fire, Steam):
            self.assertTrue(isinstance(pixel_from_name(cls.__name__), cls))
