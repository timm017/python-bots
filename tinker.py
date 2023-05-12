import tkinter as tk

def handle_click(event):
    print("Mouse clicked at ({}, {})".format(event.x, event.y))

# Create a Tkinter window
window = tk.Tk()

tk.Label(window, text="Red Text in Times Font")

window.geometry("500x500")

# Set the window title
window.title("Click Detection")

# Create a label widget
label = tk.Label(window, text="Click inside the window")

# any click within the window will be handled by the handle_click function
window.bind("<Button-1>", handle_click)

# click the label
label.bind("<Button-1>", handle_click)

# Pack the label widget into the window
label.pack()

# Start the Tkinter event loop
window.mainloop()