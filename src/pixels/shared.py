from pixels.empty import Empty
from pixels.sand import Sand
from pixels.stone import Stone
from pixels.wood import Wood
from pixels.water import Water
from pixels.lava import Lava
from pixels.oil import Oil
from pixels.fire import Fire
from pixels.steam import Steam

"""Gets the pixel class object from the type id of the pixel.

Args:
    type_id: The type id of the pixel.

Returns:
    The pixels class object.
"""
def pixel_from_id(type_id):
    mapping = {
        Sand.type_id: Sand,
        Stone.type_id: Stone,
        Wood.type_id: Wood,
        Water.type_id: Water,
        Lava.type_id: Lava,
        Oil.type_id: Oil,
        Steam.type_id: Steam,
        Empty.type_id: Empty
    }
    cls = mapping.get(type_id, Empty)
    return cls(0, 0)

"""
Gets the pixel class object from the class name of the pixel.

Args:
    name: The name of the pixel class as a string.

Returns:
    The pixels class object.
"""
def pixel_from_name(name):

    pixel = Empty(0, 0)
    match name:
        case "Sand":
            pixel = Sand(0, 0)
        case "Wood":
            pixel = Wood(0, 0)
        case "Lava":
            pixel = Lava(0, 0)
        case "Oil":
            pixel = Oil(0, 0)
        case "Steam":
            pixel = Steam(0, 0)
        case "Water":
            pixel = Water(0, 0)
        case "Stone":
            pixel = Stone(0, 0)
        case "Fire":
            pixel = Fire(0, 0)

    return pixel
