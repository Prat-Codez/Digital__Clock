from tkinter import *
from time import strftime

root = Tk()

root.title("Digital-Clock")
root.resizable(width=False, height=False)

# Define the colors and font
bg_color = "#0A1428"  # Dark blue background
fg_color = "#B0E0E6"  # Powder blue
font_style = ("Orbitron", 70, "bold")

# Create the label with new styling
label = Label(root, font=font_style, fg=fg_color, width=12 , bg=bg_color, bd=20, relief="sunken")
label.pack(anchor="center")

# This is the function to get and update the time
def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

time()
root.mainloop()