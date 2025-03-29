from pixels.empty import Empty
from pixels.sand import Sand

def pixel_from_id(id):
    if id == Sand.id:
        return Sand(0, 0)
    return Empty(0, 0)
    