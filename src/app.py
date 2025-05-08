from ui import Ui
from simulation import Simulation
from database import Database


class App:

    """
    Main class of the program.
    Connects the program logic to the UI.

    Attributes:
        simulation: Logic part of the program
        ui: UI part of the program
        database: Save handler
    """

    def __init__(self):
        self.simulation = Simulation(100, 80)
        self.ui = Ui(100, 80)
        self.database = Database()

        self.loop()
        self.ui.ui_loop()

    """Adds the pixel to the place the user clicked.
    """

    def __add_requested_pixel(self):
        recent_pixel = self.ui.recent_pixel_added
        if recent_pixel is not None:
            self.simulation.add_pixel(recent_pixel)
            self.ui.recent_pixel_added = None

    """
    Resizes the simulation and canvas according to the request of the UI.
    """

    def __do_requested_resize(self):
        resize_parameters = self.ui.resize_parameters
        if resize_parameters is not None:
            self.ui.resize_image(resize_parameters[0], resize_parameters[1])
            self.simulation.resize_grid(
                resize_parameters[0], resize_parameters[1])
            self.ui.resize_parameters = None

    """
    Saves the current game from the UI request.
    """

    def __do_requested_save(self):
        save_request = self.ui.save_request
        if save_request is not None:
            self.database.save_game(
                save_request, self.simulation, self.ui.sim_delay)
            self.ui.show_messagebox(
                "Save Game", f"Game '{save_request}' saved successfully.")
            self.ui.save_request = None

    """
    Loads the save the UI has requested.
    """

    def __do_requested_load(self):
        load_ui_request = self.ui.load_ui_request
        if load_ui_request:
            saves = self.database.list_saves()
            self.ui.init_load_ui(saves)
            self.ui.load_ui_request = None

        if self.ui.load_request is not None:
            result = self.database.load_game(self.ui.load_request)
            if result:
                w, h, delay, grid_data = result
                self.simulation.apply_loaded_save(w, h, grid_data)
                self.ui.apply_loaded_save(w, h, delay, grid_data)
                self.ui.show_messagebox("Game", "Game loaded successfully!")
            self.ui.load_request = None

    """
    Deletes the save the UI has requested.
    """

    def __do_requested_delete(self):
        if self.ui.delete_request is not None:
            self.database.delete_save(self.ui.delete_request)
            self.ui.show_messagebox(
                "Delete Save", f"Save ID {self.ui.delete_request} deleted.")
            new_saves = self.database.list_saves()
            self.ui.init_load_ui(new_saves)
            self.ui.delete_request = None

    """
    Synchronises the canvas of the UI to match the simulation state.
    """

    def __update_ui_image(self):
        for pixel in self.simulation.movement_queue:
            self.ui.add_pixel_to_image(pixel)

        self.simulation.clear_queues()
        self.ui.update_display()

    """
    Starts the main loop of the program.
    """

    def __begin_loop(self):
        self.ui.master.after(self.ui.sim_delay, self.loop)

    """
    The main loop of the program.
    Does everything the UI has requested, and steps the simulation.
    """

    def loop(self):
        self.simulation.simulate()
        self.__add_requested_pixel()
        self.__do_requested_resize()
        self.__do_requested_save()
        self.__do_requested_load()
        self.__update_ui_image()
        self.__do_requested_delete()

        self.__begin_loop()


if __name__ == "__main__":
    app = App()
