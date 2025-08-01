# Import tkinter for creating the window and widgets
from tkinter import *

# Import strftime to get current time
from time import strftime


# Create the main window
root = Tk()


# Set the window title
root.title("Digital-Clock")

# Prevent window from being resized
root.resizable(width=False, height=False)


# Choose colors for the clock
bg_color = "#0A1428"  # Dark blue background color
fg_color = "#B0E0E6"  # Light blue text color

# Choose font style and size
font_style = ("Orbitron", 70, "bold")


# Create a label to show the time
label = Label(root, 
              font=font_style,        # Use the font we chose
              fg=fg_color,           # Text color (light blue)
              width=12,              # Fixed width to prevent window jumping
              bg=bg_color,           # Background color (dark blue)
              bd=20,                 # Border thickness
              relief="sunken")       # Border style (sunken look)

# Put the label in the center of the window
label.pack(anchor="center")


# Function to update the time every second
def time():
    # Get current time in hour:minute:second AM/PM format
    string = strftime("%H:%M:%S %p")
    
    # Update the label with new time
    label.config(text=string)
    
    # Call this function again after 1000 milliseconds (1 second)
    label.after(1000, time)


# Start the time function
time()

# Keep the window running and responsive
root.mainloop()
