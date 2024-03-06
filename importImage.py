import tkinter as tk
from tkinter import filedialog
import shutil
import os

# Create a tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Ask the user to select an image file
file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

if file_path:
    # Destination directory
    destination_folder = "images"
    
    # Check if the destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Extract the file name
    file_name = os.path.basename(file_path)
    
    # Construct the destination path
    destination_path = os.path.join(destination_folder, file_name)
    
    # Copy the file to the destination folder
    shutil.copy(file_path, destination_path)
    
    print("Image has been saved to:", destination_path)
else:
    print("No image selected.")