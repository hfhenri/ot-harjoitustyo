import tkinter as tk

from pixels.empty import Empty 
from pixels.sand import Sand 
from pixels.shared import pixel_from_id

CELL_SIZE = 8

class Ui:

    def __init__(self, width, height):

        self.master = tk.Tk()
        self.master.title("Falling sand")
        self.width = width
        self.height = height

        self.recent_pixel_added = None

        control_frame = tk.Frame(self.master)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        self.current_pixel_type = tk.IntVar(value=Sand.id)

        tk.Radiobutton(control_frame, text="Sand", variable=self.current_pixel_type, value=Sand.id).pack(side=tk.LEFT)

        self.display_label = tk.Label(self.master)
        self.display_label.pack()

        self.image = tk.PhotoImage(width=width, height=height)

        for x in range(width):
            for y in range(height):
                self.image.put(Empty.color, (x, y))

        self.display_label.bind("<Button-1>", self.add_pixel_event)
        self.display_label.bind("<B1-Motion>", self.add_pixel_event)

        self.update_display()

    def update_display(self):
        self.zoomed_image = self.image.zoom(CELL_SIZE, CELL_SIZE)
        self.display_label.config(image=self.zoomed_image)
        self.display_label.image = self.zoomed_image

    def add_pixel_to_image(self, pixel):
        self.image.put(pixel.color, (pixel.x, pixel.y))
        self.update_display()
    
    def move_pixel(self, pixel):
        self.image.put(pixel.color, (pixel.x, pixel.y))
        self.image.put(Empty.color, (pixel.old_x, pixel.old_y))

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