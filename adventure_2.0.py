
import random
import sys
import time

HP = 5


# ---------------- HEALTH ----------------

def show_health():
    print("Health:", "❤️ " * HP)


def health():
    global HP

    HP -= 1
    show_health()

    if HP <= 0:
        print("\n💀 Your journey ends here...")
        print("But the story of the traveller remains.")
        sys.exit()



def get_choice():
            while True:
                choice = input("> ")

                if choice in ["1", "2", "3"]:
                    return choice

                print("❌ Please choose 1, 2, or 3.")

# ---------------- BARRIER FUNCTION ----------------


def play_barrier(name, options, success_messages, fail_messages):

    while True:

        print(f"\n{name}")

        print(f"1. {options[0]}")
        print(f"2. {options[1]}")
        print(f"3. {options[2]}")

        

        player_choice = get_choice()


        # Randomly choose the correct answer
        correct_choice = random.choice(["1", "2", "3"])

        if player_choice == correct_choice:
            print(random.choice(success_messages))
            return True

        else:
            print(random.choice(fail_messages))
            health()

            print("\n⚠️ You must try this barrier again!")




# ---------------- START GAME ----------------

print("Welcome fellow traveller")

name = input("What's thy name? ")

print(f"\n{name}..... I have a quest for you.")
qa = input("Would you like to accept it? yes/no: ").lower()


if qa == "yes":

    print("\nWell that's what I like to hear....")
    print("All you have to do is help cross to the other side.")

    print("\nThis is your health bar:")
    show_health()

    print(
        "\n🧍‍♂️➡️  ≋≋≋≋≋≋❓≋≋≋≋≋❓≋≋≋≋≋❓"
        "≋≋≋≋≋❓≋≋≋≋≋❓≋≋≋≋≋❓≋≋≋≋≋❓"
        "≋≋≋≋≋❓➡️🏝️🏆\n"
    )

    print("Let the journey start!")


    # ---------------- BARRIER 1 ----------------

    play_barrier(
        "Barrier 1: Rock 🪨",
        ["Climb", "Go around", "Break"],
        [
            "You climbed the rock! 🎉🌟✨",
            "You successfully passed the rock! 🎉"
        ],
        [
            "You slipped and fell! 💀",
            "The rock collapsed on you! 💀"
        ]
    )


    # ---------------- BARRIER 2 ----------------

    play_barrier(
        "Barrier 2: Crocodile 🐊",
        ["Sneak", "Run", "Attack"],
        [
            "The crocodile couldn't see you! 🎉🌟✨",
            "You successfully got past the crocodile! 🎉"
        ],
        [
            "The crocodile saw you! 💀",
            "The crocodile caught you! 💀",
            "You lost the fight! 💀"
        ]
    )


    # ---------------- BARRIER 3 ----------------

    play_barrier(
        "Barrier 3: Logs 🪵",
        ["Jump", "Swim", "Walk over"],
        [
            "You jumped over the log! 🎉🌟✨",
            "You successfully crossed the logs! 🎉"
        ],
        [
            "You hit the log! 💀",
            "You got stuck inside the log! 💀",
            "You slipped and fell! 💀"
        ]
    )


    # ---------------- BARRIER 4 ----------------

    play_barrier(
        "Barrier 4: Snake 🐍",
        ["Stay still", "Attack", "Run"],
        [
            "You avoided the snake! 🎉🌟✨",
            "You escaped the snake! 🎉"
        ],
        [
            "The snake attacked you! 💀",
            "The snake bit you! 💀",
            "You were too slow! 💀"
        ]
    )


    # ---------------- BARRIER 5 ----------------

    play_barrier(
        "Barrier 5: Storm 🌪️",
        ["Push forward", "Hide", "Wait"],
        [
            "You escaped the storm! 🎉🌟✨",
            "The storm passed safely! 🎉"
        ],
        [
            "The storm threw you away! 💀",
            "The storm caught you! 💀",
            "The storm got even stronger! 💀"
        ]
    )


    # ---------------- BARRIER 6 ----------------

    play_barrier(
        "Barrier 6: Shark 🦈",
        ["Swim fast", "Float", "Dive"],
        [
            "The shark was too slow! 🎉🌟✨",
            "You escaped the shark! 🎉"
        ],
        [
            "The shark caught you! 💀",
            "You moved and attracted the shark! 💀",
            "You drowned while diving! 💀"
        ]
    )


    # ---------------- BARRIER 7 ----------------

    play_barrier(
        "Barrier 7: Rock 🪨",
        ["Climb", "Break", "Go around"],
        [
            "You climbed the rock! 🎉🌟✨",
            "You successfully crossed the rock! 🎉"
        ],
        [
            "You slipped and fell! 💀",
            "The rock collapsed on you! 💀",
            "The water was too deep! 💀"
        ]
    )


    # ---------------- BARRIER 8 ----------------

    play_barrier(
        "Barrier 8: Final Crocodile 🐊",
        ["Sneak", "Run", "Trick it"],
        [
            "The crocodile couldn't see you! 🎉🌟✨",
            "You tricked the crocodile! 🎉"
        ],
        [
            "The crocodile saw you! 💀",
            "The crocodile caught you! 💀",
            "Your trick failed! 💀"
        ]
    )


    # ---------------- FINAL BARRIER ----------------

    play_barrier(
        "Final Barrier: Bridge 🌉",
        ["Cross carefully", "Run", "Jump"],
        [
            "Slow is steady and steady is fast! 🎉🌟✨",
            "You safely crossed the bridge! 🎉"
        ],
        [
            "The bridge collapsed! 💀",
            "You were too slow! 💀",
            "You fell into the abyss! 💀"
        ]
    )


    # ---------------- WIN ----------------

    print("\n✨ Thank you, brave traveller.")
    print("The path is now safe because of you! 🏝️🏆")

    frames = [
        "   🎆   ",
        "  ✨🎆✨  ",
        " 🎆✨💥✨🎆 ",
        "✨🎇✨🎇✨"
    ]

    for f in frames:
        print("\r" + f, end="")
        time.sleep(0.5)

    print("\n🏝️ YOU MADE IT! YOU WIN 🏆")


elif qa == "no":

    print(f"\nMy apologies {name}, continue on your journey.")


else:

    print("I couldn't properly hear ya!")

