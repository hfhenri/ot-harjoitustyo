from pixels.empty import Empty


class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.moved = False

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

    def clear_queue(self):
        self.movement_queue.clear()

    def add_pixel(self, pixel):
        self.grid[pixel.x][pixel.y] = pixel

    def get_pixel(self, x, y):
        return self.grid[x][y]

    def move_pixel(self, pixel, old_x, old_y):
        self.grid[old_x][old_y] = Empty(old_x, old_y)
        self.grid[pixel.x][pixel.y] = pixel

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
        pixel1_old_x = pixel1.x
        pixel1_old_y = pixel1.y

        pixel2_old_x = pixel2.x
        pixel2_old_y = pixel2.y

        self.grid[pixel1.x][pixel1.y] = pixel2
        self.grid[pixel2.x][pixel2.y] = pixel1

        pixel1.move_self(pixel2.x, pixel2.y)
        pixel2.move_self(pixel1.x, pixel1.y)

        self.movement_queue.append((pixel1, pixel1_old_x, pixel1_old_y))
        self.movement_queue.append((pixel2, pixel2_old_x, pixel2_old_y))

    def simulate(self):
        self.moved = False

        for x in range(self.width):
            for y in range(self.height - 2, -1, -1):
                cell = self.grid[x][y]
                if isinstance(cell, Empty):
                    continue
                old_x, old_y = cell.x, cell.y
                moved = cell.step(self)

                if moved:
                    self.move_pixel(cell, old_x, old_y)
                    self.movement_queue.append((cell, old_x, old_y))
