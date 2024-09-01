from tkinter import *

# Create the main window
root = Tk()
root.title("Simple Tasbeeh")
root.geometry("300x500")

# Create a label at the top to display the number with a different font
text_box = Label(root, font=("Helvetica", 36, "bold"), justify="center")
text_box.pack(pady=10)

# Create a frame to hold the buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

# Add buttons to the frame and position them side by side using grid
button_edit = Button(button_frame, text="Edit", font=("Helvetica", 14), command=lambda: edit())
button_reset = Button(button_frame, text="Reset", font=("Helvetica", 14), command=lambda: reset())

button_edit.grid(row=0, column=0, padx=10)
button_reset.grid(row=0, column=1, padx=10)

# Create a canvas to center the round button
canvas = Canvas(root, width=300, height=300)
canvas.pack()

# Create a centered large round button
large_round_button = canvas.create_oval(100, 50, 200, 150, fill="lightgreen", outline="darkgreen", width=3)
canvas.create_text(150, 100, text="^", font=("Helvetica", 69, "bold"))

# Create a smaller round button directly below the large round button with no space
small_round_button = canvas.create_oval(125, 150, 175, 200, fill="lightcoral", outline="darkred", width=3)
canvas.create_text(150, 175, text="v", font=("Helvetica", 30, "bold"))

# Define the reset and edit functions
def reset():
    text_box.config(text="")

def edit():
    # Placeholder function, add functionality if needed
    pass

# Run the application
root.mainloop()
