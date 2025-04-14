from pixels.empty import Empty
from pixels.sand import Sand
from pixels.stone import Stone
from pixels.wood import Wood
from pixels.water import Water
from pixels.lava import Lava

def pixel_from_id(type_id):
    if type_id == Sand.type_id:
        return Sand(0, 0)
    if type_id == Water.type_id:
        return Water(0, 0)
    if type_id == Stone.type_id:
        return Stone(0, 0)
    if type_id == Lava.type_id:
        return Lava(0, 0)
    if type_id == Wood.type_id:
        return Wood(0, 0)
    return Empty(0, 0)
