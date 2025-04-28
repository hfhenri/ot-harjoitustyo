from pixels.empty import Empty
from pixels.shared import pixel_from_name
class Simulation:
    """
    A collection of all the pixels on screen.
    Make the pixels interact with eachother and handles the grid.

    Attributes:
        width: Width of the grid.
        height: Height of the grid.
        movement_queue: A batch of pixels that have moved since the last cycle.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__init_grid()

        self.movement_queue = []

    """
    Initializes the grid with empty pixels.
    """

    def __init_grid(self):
        self.grid = []

        for x in range(self.width):
            new_row = []
            for y in range(self.height):
                new_row.append(Empty(x, y))

            self.grid.append(new_row)

    """
    Initializes the grid with empty pixels.
    """

    def apply_loaded_save(self, width, height, grid_data):
        self.width = width
        self.height = height
        self.__init_grid()
        for x in range(self.width):
            for y in range(self.height):
                pixel_dict = grid_data[x][y]
                pixel = pixel_from_name(pixel_dict["type"])
                for attr, value in filter(lambda i: i[0] != "type", pixel_dict.items()):
                    setattr(pixel, attr, value)
                self.grid[x][y] = pixel

    """
    Checks if a pixel can move to the specified location.

    Returns:
        True if the desired location is empty, False otherwise.
    """

    def can_move(self, x2, y2):
        if 0 <= x2 < self.width and 0 <= y2 < self.height:
            return isinstance(self.grid[x2][y2], Empty)
        return False

    """
    Checks if a pixel can move to the specified location.
    
    Args:
        x: Desired x position of the pixel
        y: Desired y position of the pixel

    Returns:
        The pixel at the desired location if not empty, None if available.
    """

    def can_move_return(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[x][y]
        return None

    """
    Swaps the places of two pixels.

    Args:
        pixel1: First pixel
        pixel2: Second pixel
    """
    def swap_places(self, pixel1, pixel2):

        self.grid[pixel1.x][pixel1.y] = pixel2
        self.grid[pixel2.x][pixel2.y] = pixel1

        pixel1.move_self(pixel2.x, pixel2.y)
        pixel2.move_self(pixel1.x, pixel1.y)

        self.movement_queue.append(pixel1)
        self.movement_queue.append(pixel2)

    """
    Clears the movement queue.
    """

    def clear_queues(self):
        self.movement_queue.clear()

    """
    Adds a pixel to the grid.

    Args:
        pixel: The pixel to add.
    """

    def add_pixel(self, pixel):
        self.grid[pixel.x][pixel.y] = pixel
        self.movement_queue.append(self.grid[pixel.x][pixel.y])

    """
    Removes the pixel at the specified coordinates, replacing it with an empty pixel.

    Args:
        x: x position of the pixel
        y: y position of the pixel
    """

    def remove_pixel(self, x, y):
        self.grid[x][y] = Empty(x, y)
        self.movement_queue.append(self.grid[x][y])

    """
    Gets the pixel at the specified coordinates

    Args:
        x: x position of the pixel
        y: y position of the pixel
    """
    def get_pixel(self, x, y):
        return self.grid[x][y]

    """
    Moves a pixel to a new location.

    Args:
        pixel: The pixel to move.
        old_x: Previous x position of the pixel
        old_y: Previous y position of the pixel
    """

    def move_pixel(self, pixel, old_x, old_y):
        self.grid[old_x][old_y] = Empty(old_x, old_y)
        self.grid[pixel.x][pixel.y] = pixel

        self.movement_queue.append(self.grid[old_x][old_y])
        self.movement_queue.append(self.grid[pixel.x][pixel.y])

    """
    Resizes the grid.

    Args:
        width: New width of the grid.
        height: New height of the grid.
    """

    def resize_grid(self, width, height):
        self.movement_queue.clear()
        self.width = width
        self.height = height
        self.grid.clear()

        for x in range(self.width):
            new_row = []
            for y in range(self.height):
                new_row.append(Empty(x, y))

            self.grid.append(new_row)

    """
    Resets the updated state of every pixel to False.
    Called at the beginning of every simulation cycle.
    """

    def __reset_updates(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y].updated = False

    """
    Steps the simulation forward one cycle without resetting the grid updates.
    """

    def __step_simulation(self):
        for x in range(self.width):
            for y in range(self.height):
                cell = self.grid[x][y]

                if isinstance(cell, Empty) or cell.updated:
                    continue
                old_x, old_y = cell.x, cell.y

                try:
                    changed = cell.step(self)
                except TypeError:
                    changed = False

                if changed:
                    self.move_pixel(cell, old_x, old_y)
                    cell.updated = True

    """
    Steps the simulation forward one cycle and resets the grid updates.
    """

    def simulate(self):
        self.__reset_updates()
        self.__step_simulation()
