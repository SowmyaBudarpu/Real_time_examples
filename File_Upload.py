from tkinter import *
from tkinter import filedialog

# Function for opening the file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("Text files", "*.txt*"), ("all files", "*.*")),
    )

    
    label_file_explorer.configure(text="File Opened: " + filename)

window = Tk()
window.title("File Explorer")
window.geometry("600x200")
window.config(background="#f2f2f2")

#screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculation of the x and y coordinates to center the window
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (400 / 2)

window.geometry("%dx%d+%d+%d" % (900, 400, x, y))

# Creation of File Explorer label
label_file_explorer = Label(
    window,
    text="File Explorer",
    width=60,
    height=2,
    fg="#333",
    font=("Arial", 24),
    bg="#f2f2f2",
)

# the Browse Files button
button_explore = Button(
    window,
    text="Browse Files",
    command=browseFiles,
    font=("Arial", 14),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=6,
    border=0,
    cursor="hand2",
)

# the Exit button
button_exit = Button(
    window,
    text="Exit",
    command=exit,
    font=("Arial", 14),
    bg="#F44336",
    fg="white",
    padx=10,
    pady=6,
    border=0,
    cursor="hand2",
)

label_file_explorer.grid(row=0, column=0, padx=20, pady=(20, 10))
button_explore.grid(row=1, column=0, pady=10)
button_exit.grid(row=2, column=0, pady=(10, 20))


window.mainloop()
