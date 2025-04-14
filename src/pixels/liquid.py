import random

def liquid_flow_logic(simulation, pixel, up=False):
    direction = 1

    if up:
        direction = -1

    if simulation.can_move(pixel.x, pixel.y + direction):
        pixel.move_self(pixel.x, pixel.y + direction)
        simulation.changed = True
        return True

    if random.choice([True, False]):
        if simulation.can_move(pixel.x - 1, pixel.y):
            pixel.move_self(pixel.x - 1, pixel.y)
            simulation.changed = True
            return True

    if simulation.can_move(pixel.x + 1, pixel.y):
        pixel.move_self(pixel.x + 1, pixel.y)
        simulation.changed = True
        return True

    return False
