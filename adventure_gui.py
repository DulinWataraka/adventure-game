import tkinter as tk

# ---------------- WINDOW ----------------

window = tk.Tk()
window.title("The Traveller")
window.geometry("800x600")
window.resizable(False, False)

# ---------------- TITLE ----------------

title = tk.Label(
    window,
    text="⚔️ THE TRAVELLER ⚔️",
    font=("Arial", 28, "bold")
)

title.pack(pady=80)

# ---------------- START BUTTON ----------------

start_button = tk.Button(
    window,
    text="START JOURNEY",
    font=("Arial", 16, "bold"),
    width=18,
    height=2
)

start_button.pack()

# ---------------- RUN ----------------

window.mainloop()