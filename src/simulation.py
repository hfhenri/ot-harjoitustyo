from pixels.empty import Empty

class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.changed = False

        self.grid = []

        for x in range(self.width):
            new_row = []
            for y in range(self.height):
                new_row.append(Empty(x, y))

            self.grid.append(new_row)

        self.movement_queue = []

    def can_move(self, x2, y2):
        if 0 <= x2 < self.width and 0 <= y2 < self.height:
            return isinstance(self.grid[x2][y2], Empty)
        return False

    def can_move_return(self, x2, y2):
        if 0 <= x2 < self.width and 0 <= y2 < self.height:
            return self.grid[x2][y2]
        return None

    def clear_queues(self):
        self.movement_queue.clear()

    def add_pixel(self, pixel):
        self.changed = True
        self.grid[pixel.x][pixel.y] = pixel
        self.movement_queue.append(self.grid[pixel.x][pixel.y])

    def remove_pixel(self, x, y):
        self.changed = True
        self.grid[x][y] = Empty(x, y)
        self.movement_queue.append(self.grid[x][y])

    def get_pixel(self, x, y):
        return self.grid[x][y]

    def move_pixel(self, pixel, old_x, old_y):
        self.grid[old_x][old_y] = Empty(old_x, old_y)
        self.grid[pixel.x][pixel.y] = pixel

        self.movement_queue.append(self.grid[old_x][old_y])
        self.movement_queue.append(self.grid[pixel.x][pixel.y])

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

    def swap_places(self, pixel1, pixel2):

        self.grid[pixel1.x][pixel1.y] = pixel2
        self.grid[pixel2.x][pixel2.y] = pixel1

        pixel1.move_self(pixel2.x, pixel2.y)
        pixel2.move_self(pixel1.x, pixel1.y)

        self.movement_queue.append(pixel1)
        self.movement_queue.append(pixel2)

    def simulate(self):

        self.changed = True

        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y].updated = False

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
