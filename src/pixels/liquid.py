import random
"""
Contains the logic on how liquid-like pixels should flow.

Args:
    simulation: Simulation handler.
    pixel: The pixel that needs to be computed.
    up: Whether the liquid should flow with gravity reversed or not.

Returns:
    True, if the pixel has moved, False otherwise.
"""


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


"""
Contains the logic on how liquid-like float on water.

Args:
    simulation: Simulation handler.
    pixel: The pixel that needs to be computed.

Returns:
    True, if the pixel has moved, False otherwise.
"""


def liquid_float_on_water_logic(simulation, pixel):

    cell_above = simulation.can_move_return(pixel.x, pixel.y - 1)
    if getattr(cell_above, "liquid", False):
        old_x, old_y = pixel.x, pixel.y
        water = cell_above

        pixel.x, pixel.y = old_x, old_y - 1
        water.x, water.y = old_x, old_y

        simulation.grid[pixel.x][pixel.y] = pixel
        simulation.grid[old_x][old_y] = water

        pixel.updated = True
        water.updated = True
        simulation.movement_queue.append(pixel)
        simulation.movement_queue.append(water)
        simulation.changed = True
        return True

    return False
