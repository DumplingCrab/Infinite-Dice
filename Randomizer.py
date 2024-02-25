import tkinter as tk
from tkinter import ttk
import random
import os

class RandomLineGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Random Line Generator")
        master.attributes('-fullscreen', True)  # Make the window fullscreen

        # Get the screen dimensions
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Calculate the center of the window
        center_x = screen_width // 2
        center_y = screen_height // 2

        style = ttk.Style()
        style.theme_use('clam')  # Use the 'clam' theme for a sleeker appearance

        self.label = ttk.Label(master, text="", font=("Helvetica", 36), wraplength=800, justify='center')  # Larger font size
        self.label.place(relx=0.5, rely=0.5, anchor='center')  # Center the text

        self.money_button = ttk.Button(master, text="Money", command=self.generate_money)
        self.monster_button = ttk.Button(master, text="Monster", command=self.generate_monster)
        self.num_button = ttk.Button(master, text="Number", command=self.generate_number)
        self.generate_button = ttk.Button(master, text="Generate", command=self.generate_random_line)

        self.money_button.pack(side='bottom', pady=20, padx=20)  # Padding added to the bottom and side of the buttons
        self.monster_button.pack(side='bottom', pady=20, padx=20)
        self.num_button.pack(side='bottom', pady=20, padx=20)
        self.generate_button.pack(side='bottom', pady=20, padx=20)  # Generate button placed last

        # Get the current directory
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # List of file names
        file_names = [
            "Animals.txt", "Food.txt", "Game_Actions.txt", "Magic_Items.txt",
            "Monsters.txt", "Money.txt", "Num.txt", "Plains.txt", "Politics.txt",
            "Real_Actions.txt", "Real_Towns.txt", "Spells.txt", "Status.txt",
            "Words.txt", "Words_2.txt", "Wiki.txt", "Punish.txt"  # Added Punish.txt here
        ]

        # Construct full file paths
        self.file_paths = [os.path.join(current_directory, file_name) for file_name in file_names if os.path.exists(os.path.join(current_directory, file_name))]

    def generate_random_line(self):
        if any(self.file_paths):
            file_path = random.choice(self.file_paths)
            print("Selected file:", file_path)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                    random_line = random.choice(lines).strip()
                    if os.path.basename(file_path) == "Spells.txt":
                        random_line = "Spell: " + random_line
                        if random.random() < 0.5:
                            random_line += " (+)"
                        else:
                            random_line += " (-)"
                    elif os.path.basename(file_path) == "Plains.txt":
                        random_line = "Plain: " + random_line
                    elif os.path.basename(file_path) == "Magic_Items.txt":
                        random_line = "Magic Item: " + random_line
                    elif os.path.basename(file_path) == "Monsters.txt":
                        if random.random() < 0.5:  # 50% chance for the number to be 1
                            random_number = 1
                        else:
                            random_number = random.randint(2, 50)
                        random_line = f"{random_number} {random_line}"
                    elif os.path.basename(file_path) == "Real_Actions.txt":
                        punish_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Punish.txt")
                        with open(punish_file_path, "r", encoding="utf-8") as punish_file:
                            punish_lines = punish_file.readlines()
                            random_punish_line = random.choice(punish_lines).strip()
                            random_line += " OR " + random_punish_line
                    self.label.config(text=random_line)
            except UnicodeDecodeError:
                print("Error: Unable to decode file", file_path)
                self.label.config(text="Error: Unable to decode file")
        else:
            self.label.config(text="No files found.")


    def generate_number(self):
        number_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Num.txt")
        try:
            with open(number_file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                random_line = random.choice(lines).strip()
                self.label.config(text=random_line)
        except UnicodeDecodeError:
            print("Error: Unable to decode file", number_file_path)
            self.label.config(text="Error: Unable to decode file")

    def generate_monster(self):
        monster_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Monsters.txt")
        try:
            with open(monster_file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                random_line = random.choice(lines).strip()
                if random.random() < 0.5:  # 50% chance for the number to be 1
                    random_number = 1
                else:
                    random_number = random.randint(2, 50)
                random_line = f"{random_number} {random_line}"
                self.label.config(text=random_line)
        except UnicodeDecodeError:
            print("Error: Unable to decode file", monster_file_path)
            self.label.config(text="Error: Unable to decode file")

    def generate_money(self):
        money_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Money.txt")
        try:
            with open(money_file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                random_line = random.choice(lines).strip()
                self.label.config(text=random_line)
        except UnicodeDecodeError:
            print("Error: Unable to decode file", money_file_path)
            self.label.config(text="Error: Unable to decode file")

root = tk.Tk()
app = RandomLineGenerator(root)
root.mainloop()
