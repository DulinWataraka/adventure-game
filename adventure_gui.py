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
        command=lambda: show_quest(
            name_entry.get(),
            name_label,
            name_entry,
            continue_button
        )
    )
    continue_button.pack(pady=20)

def show_quest(name, name_label, name_entry, continue_button):

    name_label.destroy()
    name_entry.destroy()
    continue_button.destroy()

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
        command=lambda: accept_quest(name, quest_label, accept_button, decline_button)
    )
    accept_button.pack(pady=10)

    decline_button = tk.Button(
        window,
        text="❌ DECLINE",
        font=("Arial", 14, "bold"),
        width=15
    )
    decline_button.pack(pady=10)


    #accept quest function

def accept_quest(name, quest_label, accept_button, decline_button):

    quest_label.destroy()
    accept_button.destroy()
    decline_button.destroy()

    title.config(text="The Journey Begins...")

    health_label = tk.Label(
        window,
        text="❤️ ❤️ ❤️ ❤️ ❤️",
        font=("Arial", 16)
    )
    health_label.pack(pady=10)

    level_label = tk.Label(
        window,
        text="Level 1  ███░░░░░░░  Level 2",
        font=("Arial", 14)
    )
    level_label.pack(pady=10)

    story_label = tk.Label(
        window,
        text="You stand before your first barrier...",
        font=("Arial", 18)
    )
    story_label.pack(pady=30)

    
    choice1.pack(pady=5)

    choice2 = tk.Button(
        window,
        text="2. Go Around",
        font=("Arial", 14),
        width=20
    )
    choice2.pack(pady=5)

    choice3 = tk.Button(
        window,
        text="3. Break Through",
        font=("Arial", 14),
        width=20
    )
    choice3.pack(pady=5)

    inventory_button = tk.Button(
        window,
        text="🎒 Inventory",
        font=("Arial", 12)
    )
    inventory_button.pack(pady=15)


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