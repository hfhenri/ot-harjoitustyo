from simulation import Simulation
from ui import Ui

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
            self.ui.add_pixel_to_image(recent_pixel)
            self.simulation.add_pixel(recent_pixel)
            self.ui.recent_pixel_added = None

        for pixel in self.simulation.movement_queue:
            self.ui.move_pixel(pixel)
        
        self.simulation.clear_queue()

        if self.simulation.moved:
            self.ui.update_display()
        
        self.ui.master.after(33, self.loop)

if __name__ == "__main__":
    app = App()




    