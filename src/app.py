from ui import Ui
from simulation import Simulation

class App:

    def __init__(self):
        self.simulation = Simulation(100, 80)
        self.ui = Ui(100, 80)

        self.loop()
        self.ui.ui_loop()

    def loop(self):
        self.simulation.simulate()

        recent_pixel = self.ui.recent_pixel_added
        if recent_pixel is not None:
            self.simulation.add_pixel(recent_pixel)
            self.ui.recent_pixel_added = None

        resize_parameters = self.ui.resize_parameters
        if self.ui.resize_parameters is not None:
            self.ui.resize_image(resize_parameters[0], resize_parameters[1])
            self.simulation.resize_grid(
                resize_parameters[0], resize_parameters[1])
            self.ui.resize_parameters = None

        for pixel in self.simulation.movement_queue:
            self.ui.add_pixel_to_image(pixel)

        self.simulation.clear_queues()

        if self.simulation.changed:
            self.ui.update_display()

        self.ui.master.after(self.ui.sim_delay, self.loop)


if __name__ == "__main__":
    app = App()
