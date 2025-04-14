# pylint: skip-file
import tkinter as tk

from pixels.shared import *
from pixels.empty import Empty
from pixels.sand import Sand
from pixels.water import Water
from pixels.stone import Stone
from pixels.lava import Lava
from pixels.wood import Wood

CELL_SIZE = 8


class Ui:

    def __init__(self, width, height):

        self.master = tk.Tk()
        self.master.title("Falling sand")
        self.width = width
        self.height = height

        self.recent_pixel_added = None
        self.resize_parameters = None

        control_frame = tk.Frame(self.master)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        self.sim_delay = 33

        self.current_pixel_type = tk.IntVar(value=Sand.type_id)

        tk.Radiobutton(control_frame, text="Sand",
                       variable=self.current_pixel_type,
                       value=Sand.type_id).pack(side=tk.LEFT)

        tk.Radiobutton(control_frame, text="Water",
                       variable=self.current_pixel_type,
                       value=Water.type_id).pack(side=tk.LEFT)

        tk.Radiobutton(control_frame, text="Stone",
                       variable=self.current_pixel_type,
                       value=Stone.type_id).pack(side=tk.LEFT)
        
        tk.Radiobutton(control_frame, text="Lava",
                       variable=self.current_pixel_type,
                       value=Lava.type_id).pack(side=tk.LEFT)

        tk.Radiobutton(control_frame, text="Wood",
                       variable=self.current_pixel_type,
                       value=Wood.type_id).pack(side=tk.LEFT)

        tk.Radiobutton(control_frame, text="Empty",
                       variable=self.current_pixel_type,
                       value=Empty.type_id).pack(side=tk.LEFT)
        
        settings_btn = tk.Button(control_frame, text="Settings", command=self.open_settings_window)
        settings_btn.pack(side=tk.LEFT, padx=10)


        self.display_label = tk.Label(self.master)
        self.display_label.pack()

        self.image = tk.PhotoImage(width=width, height=height)

        for x in range(width):
            for y in range(height):
                self.image.put(Empty.color, (x, y))

        self.display_label.bind("<Button-1>", self.add_pixel_event)
        self.display_label.bind("<B1-Motion>", self.add_pixel_event)

        self.update_display()

    def open_settings_window(self):
        settings_win = tk.Toplevel(self.master)
        settings_win.title("Simulation Settings")

        tk.Label(settings_win, text="Grid Width:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        width_entry = tk.Entry(settings_win, width=7)
        width_entry.insert(0, str(self.width))
        width_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(settings_win, text="Grid Height:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        height_entry = tk.Entry(settings_win, width=7)
        height_entry.insert(0, str(self.height))
        height_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(settings_win, text="Simulation Delay (ms):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        sim_delay_entry = tk.Entry(settings_win, width=7)
        sim_delay_entry.insert(0, str(self.sim_delay))
        sim_delay_entry.grid(row=2, column=1, padx=5, pady=5)

        def apply_settings():
            try:
                new_width = int(width_entry.get())
                new_height = int(height_entry.get())
                new_delay = int(sim_delay_entry.get())
                if new_width <= 0 or new_height <= 0 or new_delay < 0:
                    raise ValueError
            except ValueError:
                print("Please enter positive integer values (delay can be 0 or more).")
                return

            self.resize_parameters = (new_width, new_height)

            self.sim_delay = new_delay
            settings_win.destroy()

        apply_btn = tk.Button(settings_win, text="Apply", command=apply_settings)
        apply_btn.grid(row=3, column=0, columnspan=2, pady=10)


    def update_display(self):
        self.zoomed_image = self.image.zoom(CELL_SIZE, CELL_SIZE)
        self.display_label.config(image=self.zoomed_image)
        self.display_label.image = self.zoomed_image

    def resize_image(self, width, height):
        self.width = width
        self.height = height

        self.image = tk.PhotoImage(width=self.width, height=self.height)
        for x in range(self.width):
            for y in range(self.height):
                self.image.put(Empty.color, (x, y))

        self.update_display()

    def add_pixel_to_image(self, pixel):
        self.image.put(pixel.color, (pixel.x, pixel.y))


    def remove_from_image(self, x, y):
        self.image.put(Empty.color, (x, y))
        self.update_display()

    def move_pixel(self, pixel, old_x, old_y):
        self.image.put(pixel.color, (pixel.x, pixel.y))
        self.image.put(Empty.color, (old_x, old_y))

    def resize_image_event(self):
        try:
            new_width = int(self.width_entry.get())
            new_height = int(self.height_entry.get())
            if new_width <= 0 or new_height <= 0:
                raise ValueError
        except ValueError:
            print("Please enter positive integer values for grid dimensions.")
            return

        self.resize_parameters = (new_width, new_height)

    def add_pixel_event(self, event):
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE
        if 0 <= x < self.width and 0 <= y < self.height:
            pixel_added = pixel_from_id(self.current_pixel_type.get())
            pixel_added.x = x
            pixel_added.y = y

            self.recent_pixel_added = pixel_added

    def ui_loop(self):
        self.master.mainloop()
