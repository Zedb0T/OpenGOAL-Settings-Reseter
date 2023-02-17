import tkinter as tk
from tkinter import messagebox
import os
import sys
appdata_dir = os.getenv('APPDATA') #not ai
path =  appdata_dir  + r"\OpenGOAL\jak1\settings\pc-settings.gc" #not ai


#this function is not AI
def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename

def show_message_box():
    try:
        # Show the success message box
        messagebox.showinfo("Success", "File has been reset! You should see a broken-pc-settings.gc file where this application was ran from that you can send to the developers so they can find/fix the issue!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
# Function to check if a file exists at the given path and prompt the user for yes or no
def check_file_exists():
    if os.path.exists(path):
        while True:
            user_input = messagebox.askquestion("File exists", f"Possibly corrupt settings file found at '{path}'. Do you want to overwrite it?")
            if user_input == 'yes':
                # Do something if the user clicks yes, such as overwrite the file
                
                old_path = path
                new_path = os.getcwd()
                new_filename = "broken-pc-settings.gc"

                # Check if the file already exists and remove it
                if os.path.exists(new_path + "\\" + new_filename):
                    os.remove(new_path + "\\" + new_filename)
        
                # Rename the file
                os.rename(old_path, new_path + "\\" + new_filename)

                # Move the file to the new directory
                os.replace(new_path + "\\" + new_filename, new_path  + "\\" + new_filename)
                show_message_box()
                break
            elif user_input == 'no':
                # Do something if the user clicks no, such as cancel the operation
                break
    else:
        # Do something if the file does not exist, such as create a new file
        user_input = messagebox.askquestion("Settings file not found", f"ERROR: Did not find any settings file at '{path}'.")
        if user_input == 'yes':
            # Do something if the user clicks ok, such as close the window
            root.destroy()
        elif user_input == 'no':
                # Do something if the user clicks no, such as cancel the operation
            root.destroy()

# Create the GUI window
root = tk.Tk()
root.title("OpenGOAL settings reseter")

# Set the window to open in full screen mode
root.attributes('-fullscreen', True)

# Set the window icon
icon = tk.PhotoImage(file=get_path("joshvaccum.PNG"))
root.iconphoto(True, icon)

# Set the background image
bg_image = tk.PhotoImage(file=get_path("mod launcher splash 1.png"))
root.geometry(f"{bg_image.width()}x{bg_image.height()}")
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the OK button LOL AI originally just called this the OK button and the text was just "OK"
button1 = tk.Button(root, text="Reset the pc-settings.gc file", command=check_file_exists)

# Add the OK button to the GUI window and center it
button1.place(relx=0.5, rely=0.5, anchor="center")

# Start the GUI event loop
root.mainloop()
