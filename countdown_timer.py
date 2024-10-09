import tkinter as tk
from tkinter import Label, Entry, Button, StringVar

# Function to exit the timer and close the app
def exit_timer():
    root.destroy()

def start_countdown(total_seconds):
    global root, timer_label, exit_button  # Use global to access in nested function
    root = tk.Tk()
    root.title("Countdown Timer")
    root.geometry("300x150")
    root.config(bg='black')
    root.overrideredirect(True)  # Remove window borders for rounded corner effect

    # Timer label to display the countdown
    timer_label = Label(root, font=("Helvetica", 40), fg="cyan", bg="black")  # Cyan font
    timer_label.pack(expand=True)

    # Exit button to terminate the countdown and close the window
    exit_button = Button(root, text="Exit", font=("Helvetica", 12), command=exit_timer, relief="groove", bd=4, bg="red", fg="white")  # Red button
    exit_button.pack(side="bottom", pady=5)

    def update_timer():
        nonlocal total_seconds
        if total_seconds > 0:
            hrs, remainder = divmod(total_seconds, 3600)
            mins, secs = divmod(remainder, 60)
            time_str = f"{hrs:02d}:{mins:02d}:{secs:02d}"
            timer_label.config(text=time_str)
            total_seconds -= 1
            root.after(1000, update_timer)
        else:
            timer_label.config(text="Time's up!")

    update_timer()  # Start the countdown timer

def set_timer():
    # Get the user input for hours, minutes, and seconds
    try:
        hours = int(hour_input.get()) if hour_input.get() else 0
        minutes = int(minute_input.get()) if minute_input.get() else 0
        seconds = int(second_input.get()) if second_input.get() else 0
        total_seconds = hours * 3600 + minutes * 60 + seconds
        
        input_window.destroy()  # Close input window
        start_countdown(total_seconds)  # Start the countdown
    except ValueError:
        error_label.config(text="Please enter valid numbers.")  # Error message

# Create the input window for setting the time
input_window = tk.Tk()
input_window.title("Set Timer")
input_window.geometry("300x200")
input_window.configure(bg="black")

# Add input labels and text boxes for hours, minutes, and seconds
Label(input_window, text="Enter hours:", font=("Helvetica", 12), bg="black", fg="cyan").grid(row=0, column=0, pady=5, padx=10)
hour_input = StringVar()
Entry(input_window, textvariable=hour_input, font=("Helvetica", 12), width=5).grid(row=0, column=1)

Label(input_window, text="Enter minutes:", font=("Helvetica", 12), bg="black", fg="cyan").grid(row=1, column=0, pady=5, padx=10)
minute_input = StringVar()
Entry(input_window, textvariable=minute_input, font=("Helvetica", 12), width=5).grid(row=1, column=1)

Label(input_window, text="Enter seconds:", font=("Helvetica", 12), bg="black", fg="cyan").grid(row=2, column=0, pady=5, padx=10)
second_input = StringVar()
Entry(input_window, textvariable=second_input, font=("Helvetica", 12), width=5).grid(row=2, column=1)

# Add error label (hidden by default)
error_label = Label(input_window, text="", font=("Helvetica", 10), fg="red", bg="black")
error_label.grid(row=3, columnspan=2)

# Add Start button with smooth corners
start_button = Button(input_window, text="Start Countdown", font=("Helvetica", 12), command=set_timer, relief="groove", bd=4, bg="green", fg="white")  # Green button
start_button.grid(row=4, columnspan=2, pady=10)

# Start the input window loop
input_window.mainloop()
