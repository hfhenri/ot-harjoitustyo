import sqlite3
import json


class Database:

    """
    The Database class handles the saving and loading of the game.

    Attrs:
        db_file: Database file path
        conn: Connection to the database
        cursor: Executes SQL statements
        DB_FILE: The default filename
    """

    DB_FILE = "saves.db"

    def __init__(self, db_file=None):
        self.db_file = db_file or self.DB_FILE
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        self._create_table()

    """
    Creates the table where the games are stored.
    """

    def _create_table(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS saves (
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   width INTEGER,
                   height INTEGER,
                   sim_delay INTEGER,
                   grid TEXT
            )"""
        )
        self.conn.commit()

    """
    Converts a pixel class to a dictionary.

    Returns:
        The dictionary.
    """

    @staticmethod
    def __pixel_to_dict(pixel):
        pixel_dict = pixel.__dict__
        pixel_dict["type"] = pixel.__class__.__name__
        return pixel_dict

    """
    Saves the game into the database.

    Args:
        name: Name of the save.
        simulation: The simulation handler.
        sim_delay: Time of each simulation cycle.
    """

    def save_game(self, name, simulation, sim_delay):
        payload = json.dumps(simulation.grid, default=self.__pixel_to_dict)
        self.cursor.execute(
            "INSERT INTO saves (name, width, height, sim_delay, grid) VALUES (?, ?, ?, ?, ?)",
            (name, simulation.width, simulation.height, sim_delay, payload)
        )
        self.conn.commit()

    """
    Deletes the specified save from the database.

    Args:
        save_id: Database ID of the save.
    """

    def delete_save(self, save_id):
        self.cursor.execute("DELETE FROM saves WHERE id=?", (save_id,))
        self.conn.commit()

    """
    Lists all the saves in the database.

    Returns:
        All the saves.
    """

    def list_saves(self):
        self.cursor.execute("SELECT id, name FROM saves")
        return self.cursor.fetchall()

    """
    Loads the specified save from the database.

    Returns:
        Width of the simulation grid.
        Height of the simulation grid.
        Time of each simulation cycle.
        Grid data in JSON format.
    """

    def load_game(self, save_id):
        self.cursor.execute(
            "SELECT width, height, sim_delay, grid FROM saves WHERE id=?",
            (save_id,)
        )
        row = self.cursor.fetchone()
        if not row:
            return None
        width, height, delay, grid_json = row
        grid = json.loads(grid_json)
        return width, height, delay, grid

    """
    Closes the database connection.
    """

    def close(self):
        self.conn.close()
