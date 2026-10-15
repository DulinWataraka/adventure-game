import tkinter as tk
import random


HP = 5
MAX_HP = 5
current_barrier = 1

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




def choose_barrier(choice):
    global HP, current_barrier

    chances = [75, 45, 30]

    success_messages = [
        "You climbed the rock! 🎉🌟✨",
        "You found your way around the rock! 🎉",
        "You successfully broke the rock! 💥🎉"
    ]

    fail_messages = [
        "You slipped and fell! 💀",
        "You couldn't find your way around and got lost! 💀",
        "The rock collapsed on you! 💀"
    ]

    roll = random.randint(1, 100)

    if roll <= chances[choice]:
        result_label.config(text=success_messages[choice])

        current_barrier += 1
        story_label.config(
            text=f"Barrier {current_barrier}: The next obstacle awaits!"
        )

    else:
        HP -= 1

        health_label.config(
            text="❤️ " * HP + "🖤 " * (MAX_HP - HP)
        )

        result_label.config(
            text=fail_messages[choice] + "\nTry again!"
        )

        if HP <= 0:
            result_label.config(text="💀 GAME OVER! Your journey ends here.")
            choice1.config(state="disabled")
            choice2.config(state="disabled")
            choice3.config(state="disabled")

    #accept quest function

def accept_quest(name, quest_label, accept_button, decline_button):

    global health_label, story_label
    global choice1, choice2, choice3

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


    choice1 = tk.Button(
    window,
    text="1. Climb",
    font=("Arial", 14),
    width=20,
    command=lambda: choose_barrier(0)
    )
    
    choice1.pack(pady=5)

    choice2 = tk.Button(
    window,
    text="2. Go Around",
    font=("Arial", 14),
    width=20,
    command=lambda: choose_barrier(1)
    )
    choice2.pack(pady=5)



    choice3 = tk.Button(
    window,
    text="3. Break Through",
    font=("Arial", 14),
    width=20,
    command=lambda: choose_barrier(2)
    )
    choice3.pack(pady=5)

    global result_label

    result_label = tk.Label(
    window,
    text="",
    font=("Arial", 16, "bold")
    )
    result_label.pack(pady=15)

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