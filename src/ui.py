# pylint: skip-file
import tkinter as tk
import tkinter.simpledialog as simpledialog
from pixels.acid import Acid
from pixels.shared import *
from pixels.fire import Fire
from pixels.empty import Empty
from pixels.sand import Sand
from pixels.water import Water
from pixels.stone import Stone
from pixels.lava import Lava
from pixels.wire import Wire
from pixels.wood import Wood
from pixels.oil import Oil

CELL_SIZE = 8


class Ui:

    """
    Handles the entire UI of the program.

    Attributes:
        width: Width of the canvas
        height: Height of the canvas
        recent_pixel_added: request to add a pixel
        save_request: request to save the game
        load_ui_request: request to load the save UI
        load_request: request to load a save
        delete_request: request to delete a save
        sim_delay: delay between each simulation step
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.recent_pixel_added = None
        self.resize_parameters = None
        self.save_request = None
        self.load_ui_request = None
        self.load_request = None
        self.delete_request = None
        self.sim_delay = 33
        self.__init_top_ui()
        self.__init_canvas()

        self.update_display()

    """
    Initializes the buttons of the main UI
    """

    def __init_top_ui(self):
        self.master = tk.Tk()
        self.master.title("Falling sand")
        self.control_frame = tk.Frame(self.master)
        self.control_frame.pack(side=tk.TOP, fill=tk.X)

        self.current_pixel_type = tk.IntVar(value=Sand.type_id)
        for cls in (Sand, Water, Stone, Lava, Wood, Oil, Acid, Wire, Fire, Empty):
            tk.Radiobutton(self.control_frame, text=cls.__name__,
                           variable=self.current_pixel_type, value=cls.type_id).pack(side=tk.LEFT)

        tk.Button(self.control_frame, text="Save Game",
                  command=self.__save_game_request).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Load Game",
                  command=self.__load_game_ui_request).pack(side=tk.LEFT, padx=5)

        settings_btn = tk.Button(
            self.control_frame, text="Settings", command=self.__handle_settings)
        settings_btn.pack(side=tk.LEFT, padx=10)

    """
    Initializes the drawing canvas
    """

    def __init_canvas(self):
        self.display_label = tk.Label(self.master)
        self.display_label.pack()

        self.image = tk.PhotoImage(width=self.width, height=self.height)

        for x in range(self.width):
            for y in range(self.height):
                self.image.put(Empty.color, (x, y))

        self.display_label.bind("<Button-1>", self.__add_pixel_event)
        self.display_label.bind("<B1-Motion>", self.__add_pixel_event)

    """
    Applies the new settings the user input
    """

    def __apply_settings(self):
        try:
            new_width = int(self.width_entry.get())
            new_height = int(self.height_entry.get())
            new_delay = int(self.sim_delay_entry.get())
            if new_width <= 0 or new_height <= 0 or new_delay < 1:
                raise ValueError
        except ValueError:
            self.show_messagebox(
                "Error", "Please enter positive integer values (delay can be 1 or more).")
            return

        self.resize_parameters = (new_width, new_height)
        self.sim_delay = new_delay
        self.settings_win.destroy()

    """
    Initializes the settings UI box
    """

    def __handle_settings(self):
        self.settings_win = tk.Toplevel(self.master)
        self.settings_win.title("Simulation Settings")

        tk.Label(self.settings_win, text="Grid Width:").grid(
            row=0, column=0, padx=5, pady=5, sticky="e")
        self.width_entry = tk.Entry(self.settings_win, width=7)
        self.width_entry.insert(0, str(self.width))
        self.width_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.settings_win, text="Grid Height:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e")
        self.height_entry = tk.Entry(self.settings_win, width=7)
        self.height_entry.insert(0, str(self.height))
        self.height_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.settings_win, text="Simulation Delay (ms):").grid(
            row=2, column=0, padx=5, pady=5, sticky="e")
        self.sim_delay_entry = tk.Entry(self.settings_win, width=7)
        self.sim_delay_entry.insert(0, str(self.sim_delay))
        self.sim_delay_entry.grid(row=2, column=1, padx=5, pady=5)

        apply_btn = tk.Button(self.settings_win, text="Apply",
                              command=self.__apply_settings)
        apply_btn.grid(row=3, column=0, columnspan=2, pady=10)

    """
    Helper function to show a messagebox
    """

    def show_messagebox(self, title, message):
        tk.messagebox.showinfo(title, message)

    """
    Handles the game saving dialog
    """

    def __save_game_request(self):
        name = simpledialog.askstring(
            "Save Game", "Enter a name for this save:")
        if not name:
            return

        self.save_request = name

    """
    Function connected to the save loading UI button
    """

    def __load_game_ui_request(self):
        self.load_ui_request = True

    """
    Initializes the save loading UI
    """

    def init_load_ui(self, saves):
        if not saves:
            self.show_messagebox("Load Game", "No saved games available.")
            return

        load_win = tk.Toplevel(self.master)
        load_win.title("Load Game")

        tk.Label(load_win, text="Select a save:").pack(pady=5)
        self.save_listbox = tk.Listbox(load_win, width=40)
        for save_id, name in saves:
            self.save_listbox.insert(tk.END, f"{save_id}: {name}")
        self.save_listbox.pack(padx=10, pady=5)
        btn_frame = tk.Frame(load_win)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Load", command=self.__do_load_request).pack(
            side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete", command=self.__do_delete_request).pack(
            side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cancel", command=load_win.destroy).pack(
            side=tk.LEFT, padx=5)

    """
    Function connected to the save loading button. 
    Creates the save loading request.
    """

    def __do_load_request(self):
        sel = self.save_listbox.curselection()
        if not sel:
            return
        save_id = int(self.save_listbox.get(sel[0]).split(':')[0])
        self.load_request = save_id

    """
    Function connected to the save deletion button. 
    Creates the save deletion request.
    """

    def __do_delete_request(self):
        sel = self.save_listbox.curselection()
        if not sel:
            return
        save_id = int(self.save_listbox.get(sel[0]).split(':')[0])
        self.delete_request = save_id

    """
    Updates the canvas to reflect the loaded save.

    Args:
        width: width of the save
        height: height of the save
        delay: the simulatino delay of the save
        grid_data: the pixel data of the save
    """

    def apply_loaded_save(self, width, height, delay, grid_data):
        self.width = width
        self.height = height
        self.sim_delay = delay
        self.image = tk.PhotoImage(width=self.width, height=self.height)
        for x in range(self.width):
            for y in range(self.height):
                pixel_dict = grid_data[x][y]
                pixel = pixel_from_name(pixel_dict["type"])
                self.image.put(pixel.color, (x, y))

    """
    Refreshes the canvas when its changed.
    """

    def update_display(self):
        self.zoomed_image = self.image.zoom(CELL_SIZE, CELL_SIZE)
        self.display_label.config(image=self.zoomed_image)
        self.display_label.image = self.zoomed_image

    """
    Resizes the canvas.

    Args:
        width: 
    """

    def resize_image(self, width, height):
        self.width = width
        self.height = height

        self.image = tk.PhotoImage(width=self.width, height=self.height)
        for x in range(self.width):
            for y in range(self.height):
                self.image.put(Empty.color, (x, y))

        self.update_display()

    """
    Adds a singular pixel to the canvas.

    Args:
        pixel: The pixel to add.
    """

    def add_pixel_to_image(self, pixel):
        self.image.put(pixel.color, (pixel.x, pixel.y))

    """
    Handles the pixel addition event.

    Args:
        event: The event trigggered by the mouse click or movement
    """

    def __add_pixel_event(self, event):
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE
        if 0 <= x < self.width and 0 <= y < self.height:
            pixel_added = pixel_from_id(self.current_pixel_type.get())
            pixel_added.x = x
            pixel_added.y = y

            self.recent_pixel_added = pixel_added

    """
    Starts the ui loop.
    """

    def ui_loop(self):
        self.master.mainloop()
