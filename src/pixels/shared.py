from pixels.empty import Empty
from pixels.sand import Sand
from pixels.water import Water
from pixels.stone import Stone

def pixel_from_id(type_id):
    if type_id == Sand.type_id:
        return Sand(0, 0)
    if type_id == Water.type_id:
        return Water(0, 0)
    if type_id == Stone.type_id:
        return Stone(0, 0)
    return Empty(0, 0)
