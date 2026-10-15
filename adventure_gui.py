import tkinter as tk
import random


HP = 5
MAX_HP = 5
current_barrier = 1
LEVEL = 1
LEVEL_PROGRESS = 0
inventory = []


#barrier data

barriers = [
    {
        "name": "Rock 🪨",
        "options": ["Climb", "Go Around", "Break"],
        "chances": [75, 45, 30],
        "success": [
            "You climbed the rock! 🎉🌟✨",
            "You found your way around the rock! 🎉",
            "You successfully broke the rock! 💥🎉"
        ],
        "fail": [
            "You slipped and fell! 💀",
            "You couldn't find your way around and got lost! 💀",
            "The rock collapsed on you! 💀"
        ]
    },
    {
        "name": "Crocodile 🐊",
        "options": ["Sneak", "Run", "Attack"],
        "chances": [75, 45, 30],
        "success": [
            "The crocodile couldn't see you! 🎉🌟✨",
            "You successfully ran past the crocodile! 🎉",
            "You defeated the crocodile! 🎉"
        ],
        "fail": [
            "The crocodile saw you! 💀",
            "The crocodile caught you! 💀",
            "You lost the fight! 💀"
        ]
    }
    
,
    {
        "name": "Logs 🪵",
        "options": ["Jump", "Swim", "Walk over"],
        "chances": [45, 30, 70],
        "success": [
            "You jumped over the log! 🎉🌟✨",
            "You successfully swam across the logs! 🎉",
            "You carefully walked over the logs! 🎉"
        ],
        "fail": [
            "You hit the log! 💀",
            "You got stuck inside the logs! 💀",
            "You slipped and fell! 💀"
        ]
    },
    {
        "name": "Snake 🐍",
        "options": ["Stay still", "Attack", "Run"],
        "chances": [45, 30, 75],
        "success": [
            "You stayed still and avoided the snake! 🎉🌟✨",
            "The venom was strong but you are stronger! 🎉",
            "You escaped the snake! 🎉"
        ],
        "fail": [
            "The snake attacked you! 💀",
            "The snake bit you during the fight! 💀",
            "You were too slow! 💀"
        ]
    },
    {
        "name": "Storm 🌪️",
        "options": ["Push forward", "Hide", "Wait"],
        "chances": [45, 70, 30],
        "success": [
            "You pushed forward and escaped the storm! 🎉🌟✨",
            "You found shelter! 🎉",
            "The storm passed safely! 🎉"
        ],
        "fail": [
            "The storm threw you away! 💀",
            "The storm found your hiding spot! 💀",
            "The storm got even stronger! 💀"
        ]
    },
    {
        "name": "Shark 🦈",
        "options": ["Swim fast", "Float", "Dive"],
        "chances": [30, 70, 45],
        "success": [
            "You swam faster than the shark! 🎉🌟✨",
            "The shark thought you were dead! 🎉",
            "You escaped the shark by diving! 🎉"
        ],
        "fail": [
            "The shark caught you! 💀",
            "You moved and attracted the shark! 💀",
            "You drowned while diving! 💀"
        ]
    },
    {
        "name": "Rock 🪨",
        "options": ["Climb", "Go around", "Break"],
        "chances": [30, 70, 45],
        "success": [
            "You climbed the rock! 🎉🌟✨",
            "You found your way around the rock! 🎉",
            "You successfully broke the rock! 💥🎉"
        ],
        "fail": [
            "You slipped and fell! 💀",
            "The water was too deep! 💀",
            "The rock collapsed on you! 💀"
        ]
    },
    {
        "name": "Final Crocodile 🐊",
        "options": ["Sneak", "Run", "Trick it"],
        "chances": [30, 70, 45],
        "success": [
            "The crocodile couldn't see you! 🎉🌟✨",
            "You were too fast for the crocodile! 🎉",
            "You tricked the crocodile! 🎉"
        ],
        "fail": [
            "The crocodile saw you! 💀",
            "The crocodile caught you! 💀",
            "Your trick failed! 💀"
        ]
    },
    {
        "name": "Bridge 🌉",
        "options": ["Cross carefully", "Run", "Jump"],
        "chances": [70, 45, 30],
        "success": [
            "Slow is steady and steady is fast! 🎉🌟✨",
            "You ran across the bridge before it collapsed! 🎉",
            "You jumped over the bridge! 🎉"
        ],
        "fail": [
            "The bridge collapsed! 💀",
            "You were too slow! 💀",
            "You fell into the abyss! 💀"
        ]
    }

]


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

    barrier = barriers[current_barrier - 1]
    roll = random.randint(1, 100)

    if roll <= barrier["chances"][choice]:
        result_label.config(text=barrier["success"][choice])

        update_level(True)


        #award potion for success

        if current_barrier in [1, 8] and barrier["chances"][choice] == min(barrier["chances"]):
            inventory.append("🧪 Health Potion")
            result_label.config(
                text=result_label.cget("text") + "\n🎁 You found a Health Potion!"
            )



        current_barrier += 1

        if current_barrier > len(barriers):
            title.config(text="🏆 YOU MADE IT!")
            story_label.config(
            text="✨ Thank you, brave traveller!\n"
             "The path is now safe because of you! 🏝️"
            )
            result_label.config(text="🎉 YOU WIN! 🎉")

            choice1.config(state="disabled")
            choice2.config(state="disabled")
            choice3.config(state="disabled")
        else:
            show_barrier()

    else:
        HP -= 1

        update_level(False)

        health_label.config(
            text="❤️ " * HP + "🖤 " * (MAX_HP - HP)
        )

        result_label.config(
            text=barrier["fail"][choice] + "\nTry again!"
        )

        if HP <= 0:
            result_label.config(text="💀 GAME OVER! Your journey ends here.")
            choice1.config(state="disabled")
            choice2.config(state="disabled")
            choice3.config(state="disabled")



def update_level(success):
    global LEVEL, LEVEL_PROGRESS, MAX_HP, HP

    if success:
        LEVEL_PROGRESS += 1
    else:
        LEVEL_PROGRESS -= 1

    LEVEL_PROGRESS = max(0, LEVEL_PROGRESS)

    if LEVEL_PROGRESS >= 4:
        LEVEL += 1
        LEVEL_PROGRESS = 0

        MAX_HP += 1
        HP = MAX_HP

        result_label.config(
            text=f"🎉 LEVEL UP! You reached Level {LEVEL}!\n"
                 f"Your health is fully restored!"
        )

    filled = "█" * (LEVEL_PROGRESS * 3)
    empty = "░" * (12 - LEVEL_PROGRESS * 3)

    level_label.config(
        text=f"{LEVEL} {filled}{empty} {LEVEL + 1}"
    )

    health_label.config(
        text="❤️ " * HP + "🖤 " * (MAX_HP - HP)
    )



def show_barrier():
    barrier = barriers[current_barrier - 1]

    story_label.config(
        text=f"Barrier {current_barrier}: {barrier['name']}"
    )

    choice1.config(text=f"1. {barrier['options'][0]}")
    choice2.config(text=f"2. {barrier['options'][1]}")
    choice3.config(text=f"3. {barrier['options'][2]}")



def show_inventory():
    potion_count = inventory.count("🧪 Health Potion")

    if potion_count == 0:
        result_label.config(text="🎒 Your inventory is empty.")
    else:
        result_label.config(
            text=f"🎒 Inventory:\n🧪 Health Potion ×{potion_count}"
        )


def use_potion():
    global HP

    if "🧪 Health Potion" not in inventory:
        result_label.config(text="❌ You don't have a Health Potion!")
        return

    if HP == MAX_HP:
        result_label.config(text="❤️ Your health is already full!")
        return

    inventory.remove("🧪 Health Potion")
    HP = min(HP + 1, MAX_HP)

    health_label.config(
        text="❤️ " * HP + "🖤 " * (MAX_HP - HP)
    )

    result_label.config(text="🧪 You used a Health Potion! +1 HP")





    #accept quest function

def accept_quest(name, quest_label, accept_button, decline_button):


    global health_label, story_label,level_label
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
        text="Level 1  ░░░░░░░░░░░░  Level 2",
        font=("Arial", 14)
    )
    level_label.pack(pady=10)

    story_label = tk.Label(
        window,
        text="The journey begins...",
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

    show_barrier()

    inventory_button = tk.Button(
        window,
        text="🎒 Inventory",
        font=("Arial", 12),
        command=show_inventory
    )
    inventory_button.pack(pady=15)

    potion_button = tk.Button(
    window,
    text="🧪 Use Potion",
    font=("Arial", 12),
    command=use_potion
    )
    potion_button.pack(pady=5)


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