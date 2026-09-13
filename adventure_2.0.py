import random
import sys
import time

HP = 5
inventory = []
LEVEL_PROGRESS = 0
LEVEL = 1


# ---------------- HEALTH ----------------

def show_health():
    print("Health:", "❤️ " * HP)


def show_inventory():
    print("\n🎒 Inventory:")

    if len(inventory) == 0:
        print("Your inventory is empty.")

    else:
        potion_count = inventory.count("🧪 Health Potion")

        if potion_count > 0:
            print(f"🧪 Health Potion ×{potion_count}")


def health():
    global HP

    HP -= 1
    show_health()

    if HP <= 0:
        print("\n💀 Your journey ends here...")
        print("But the story of the traveller remains.")
        sys.exit()


#inventory use

def use_potion():
    global HP

    if "🧪 Health Potion" in inventory:

        if HP == 5:
            print("\n❤️ Your health is already full!")

        else:
            HP += 1
            inventory.remove("🧪 Health Potion")
            print("\n🧪 You used the Health Potion!")
            show_health()

    else:
        print("\n❌ You don't have a Health Potion.")





#####      xp bar      #####

def update_level(success):
    global LEVEL, LEVEL_PROGRESS

    if success:
        LEVEL_PROGRESS += 1
    else:
        LEVEL_PROGRESS -= 1

    # Level up
    if LEVEL_PROGRESS >= 4:
        LEVEL += 1
        LEVEL_PROGRESS = 0
        print(f"\n🎉 YOU REACHED LEVEL {LEVEL}!")

    # Don't let progress go below 0
    if LEVEL_PROGRESS < 0:
        LEVEL_PROGRESS = 0

    filled = "█" * (LEVEL_PROGRESS * 3)
    empty = "░" * (12 - (LEVEL_PROGRESS * 3))

    print(f"\n{LEVEL} {filled}{empty} {LEVEL + 1}")

# ---------------- CHOICE FUNCTION ----------------

def get_choice():
    while True:
        choice = input("> ").lower()

        if choice == "inventory":
            show_inventory()
            continue

        if choice == "potion":
            use_potion()
            continue

        if choice in ["1", "2", "3"]:
            return choice

        print("❌ Please choose 1, 2, or 3, or type 'inventory' or 'potion'.")

# ---------------- BARRIER FUNCTION ----------------

def play_barrier(name, options, chances, success_messages, fail_messages, reward=None):

    while True:

        print(f"\n{name}")

        print(f"1. {options[0]}")
        print(f"2. {options[1]}")
        print(f"3. {options[2]}")

        player_choice = get_choice()

        # Get the position of the player's chosen option
        index = int(player_choice) - 1

        # Get the chance for that option
        chance = chances[index]

        # Generate a random number between 1 and 100
        roll = random.randint(1, 100)

        if roll <= chance:

            print(success_messages[index])

            update_level(True)

            lowest_chance = min(chances)

            if chance == lowest_chance and reward is not None:
                inventory.append(reward)
                print(f"\n🎁 You found {reward}!")
                show_inventory()

            return True

        else:

            # Show the failure message for the chosen option
            print(fail_messages[index])

            update_level(False)

            health()

        


            print("\n⚠️ You must try this barrier again!")


# ---------------- START GAME ----------------




print("Welcome fellow traveller")


name = input("What's thy name? ")
time.sleep(2)


print(f"\n{name}..... I have a quest for you.")
time.sleep(2)
qa = input("Would you like to accept it? yes/no: ").lower()
time.sleep(2)


if qa == "yes":

    print("\nWell that's what I like to hear....")
    time.sleep(3)
    print("All you have to do is help cross to the other side.")

    time.sleep(3)
    print("\nThis is your health bar:")
    time.sleep(2)
    show_health()
    time.sleep(2)

    



    print(
        "\n🧍➡️  ≋≋≋≋≋≋❓≋≋≋≋≋❓≋≋≋≋≋❓"
        "≋≋≋≋≋❓≋≋≋≋≋❓≋≋≋≋≋❓≋≋≋≋≋❓"
        "≋≋≋≋≋❓➡️🏝️ 🏆 \n"
    )
    time.sleep(2)

    while True:
        press=input("Press enter to start...")
        if press == "":
            break




    print("Let the journey start!")
    time.sleep(2)


    # ---------------- BARRIER 1 ----------------

    play_barrier(
        "Barrier 1: Rock 🪨",
        ["Climb", "Go around", "Break"],
        [75, 45, 30],
        [
            "You climbed the rock! 🎉🌟✨",
            "You found your way around the rock! 🎉",
            "You successfully broke the rock! 💥🎉"
        ],
        [
            "You slipped and fell! 💀",
            "You couldn't find your way around and got lost! 💀",
            "The rock collapsed on you! 💀"
        ],
        reward="🧪 Health Potion"
    )
    time.sleep(2)


    # ---------------- BARRIER 2 ----------------

    play_barrier(
        "Barrier 2: Crocodile 🐊",
        ["Sneak", "Run", "Attack"],
        [75, 45, 30],
        [
            "The crocodile couldn't see you! 🎉🌟✨",
            "You successfully ran past the crocodile! 🎉",
            "You defeated the crocodile! 🎉"
        ],
        [
            "The crocodile saw you! 💀",
            "The crocodile caught you! 💀",
            "You lost the fight! 💀"
        ],
        
    )
    time.sleep(2)


    # ---------------- BARRIER 3 ----------------

    play_barrier(
        "Barrier 3: Logs 🪵",
        ["Jump", "Swim", "Walk over"],
        [45, 30, 70],
        [
            "You jumped over the log! 🎉🌟✨",
            "You successfully swam across the logs! 🎉",
            "You carefully walked over the logs! 🎉"
        ],
        [
            "You hit the log! 💀",
            "You got stuck inside the logs! 💀",
            "You slipped and fell! 💀"
        ]
    )
    time.sleep(2)


    # ---------------- BARRIER 4 ----------------

    play_barrier(
        "Barrier 4: Snake 🐍",
        ["Stay still", "Attack", "Run"],
        [45, 30, 75],
        [
            "You stayed still and avoided the snake! 🎉🌟✨",
            "The venom was strong but you are stronger! 🎉",
            "You escaped the snake! 🎉"
        ],
        [
            "The snake attacked you! 💀",
            "The snake bit you during the fight! 💀",
            "You were too slow! 💀"
        ]
    )
    time.sleep(2)


    # ---------------- BARRIER 5 ----------------

    play_barrier(
        "Barrier 5: Storm 🌪️",
        ["Push forward", "Hide", "Wait"],
        [45, 70, 30],
        [
            "You pushed forward and escaped the storm! 🎉🌟✨",
            "You found shelter! 🎉",
            "The storm passed safely! 🎉"
        ],
        [
            "The storm threw you away! 💀",
            "The storm found your hiding spot! 💀",
            "The storm got even stronger! 💀"
        ]
    )
    time.sleep(2)


    # ---------------- BARRIER 6 ----------------

    play_barrier(
        "Barrier 6: Shark 🦈",
        ["Swim fast", "Float", "Dive"],
        [30, 70, 45],
        [
            "You swam faster than the shark! 🎉🌟✨",
            "The shark thought you were dead! 🎉",
            "You escaped the shark by diving! 🎉"
        ],
        [
            "The shark caught you! 💀",
            "You moved and attracted the shark! 💀",
            "You drowned while diving! 💀"
        ],
        
    )
    time.sleep(2)


    # ---------------- BARRIER 7 ----------------

    play_barrier(
        "Barrier 7: Rock 🪨",
        ["Climb", "Go around", "Break"],
        [30, 70, 45],
        [
            "You climbed the rock! 🎉🌟✨",
            "You found your way around the rock! 🎉",
            "You successfully broke the rock! 💥🎉"
        ],
        [
            "You slipped and fell! 💀",
            "The water was too deep! 💀",
            "The rock collapsed on you! 💀"
        ]
    )
    time.sleep(2)


    # ---------------- BARRIER 8 ----------------

    play_barrier(
        "Barrier 8: Final Crocodile 🐊",
        ["Sneak", "Run", "Trick it"],
        [30, 70, 45],
        [
            "The crocodile couldn't see you! 🎉🌟✨",
            "You were too fast for the crocodile! 🎉",
            "You tricked the crocodile! 🎉"
        ],
        [
            "The crocodile saw you! 💀",
            "The crocodile caught you! 💀",
            "Your trick failed! 💀"
        ],
        reward="🧪 Health Potion"
    )
    time.sleep(2)


    # ---------------- FINAL BARRIER ----------------

    play_barrier(
        "Final Barrier: Bridge 🌉",
        ["Cross carefully", "Run", "Jump"],
        [70, 45, 30],
        [
            "Slow is steady and steady is fast! 🎉🌟✨",
            "You ran across the bridge before it collapsed! 🎉",
            "You jumped over the bridge! 🎉"
        ],
        [
            "The bridge collapsed! 💀",
            "You were too slow! 💀",
            "You fell into the abyss! 💀"
        ]
    )
    time.sleep(2)


    # ---------------- WIN ----------------

    print("\n✨ Thank you, brave traveller.")
    time.sleep(2)
    print("The path is now safe because of you! 🏝️🏆")
    time.sleep(2)

    frames = [
        "   🎆   ",
        "  ✨🎆✨  ",
        " 🎆✨💥✨🎆 ",
        "✨🎇✨🎇✨"
    ]

    for f in frames:
        print("\r" + f, end="")
        time.sleep(0.5)

    time.sleep(2)

    print("\n🏝️ YOU MADE IT! YOU WIN 🏆")


elif qa == "no":

    print(f"\nMy apologies {name}, continue on your journey.")


else:

    print("I couldn't properly hear ya!")
