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


# ---------------- START GAME ----------------

def start_game():
    title.config(text="Welcome, fellow traveller!")

    start_button.destroy()

    name_label = tk.Label(
        window,
        text="What's thy name?",
        font=("Arial", 18)
    )
    name_label.pack(pady=20)

    name_entry = tk.Entry(
        window,
        font=("Arial", 16),
        width=25
    )
    name_entry.pack()

    continue_button = tk.Button(
        window,
        text="Continue",
        font=("Arial", 14),
        command=lambda: show_quest(name_entry.get())
    )
    continue_button.pack(pady=20)


def show_quest(name):
    title.config(text=f"{name}..... I have a quest for you.")

    quest_label = tk.Label(
        window,
        text="Will you accept this quest?",
        font=("Arial", 18)
    )
    quest_label.pack(pady=30)

    accept_button = tk.Button(
        window,
        text="⚔️ ACCEPT",
        font=("Arial", 14, "bold"),
        width=15,
        command=lambda: accept_quest(name)
    )
    accept_button.pack(pady=10)

    decline_button = tk.Button(
        window,
        text="❌ DECLINE",
        font=("Arial", 14, "bold"),
        width=15
    )
    decline_button.pack(pady=10)

    def accept_quest(name):
        title.config(text=f"Good choice, {name}...")


# ---------------- START BUTTON ----------------

start_button = tk.Button(
    window,
    text="START JOURNEY",
    font=("Arial", 16, "bold"),
    width=18,
    height=2,
    command=start_game
)

start_button.pack()


# ---------------- RUN ----------------

window.mainloop()