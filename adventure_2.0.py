import random
import sys
import time

Hearts="❤️ ❤️ ❤️ ❤️ ❤️ "
HP=5


print("Welcome fellow traveller")

name=input("What's thy name? ")

print(f'{name}.....I have a quest for you Would you like to accept it? ')

qa=input("yes/no ")

if qa=="yes":
    print("Well that's what I like to here....")
    print("All you have to do is help cross to the other side")
    
    
    
    print(f'This is your health bar \n {Hearts}')
   

    
    
    print("🧍‍♂️➡️  ≋≋≋≋≋≋≋≋❓≋≋≋≋≋≋≋≋❓≋≋≋≋≋≋≋≋❓≋≋≋≋≋≋≋≋❓≋≋≋≋≋≋≋≋❓≋≋≋≋≋≋≋≋❓≋≋≋≋≋≋≋≋❓≋≋≋≋≋≋≋≋❓➡️🏝️🏆\n")
    print("Let the journey start!")


    
    def health():
        global HP
        HP -= 1
        print("HP:", "❤️" * HP)

        if HP <= 0:
            print("\n💀 Your journey ends here... but the story of the traveller remains")
            sys.exit()






    # 1st barrier 🪨
    print("\nBarrier 1: Rock 🪨")
    print("1 Climb | 2 Go around | 3 Break")
    first = input("> ") 


    choice = random.choice('123')

    if first=="1":
        if first==choice:
            print("You climbed the rock! 🎉🌟✨")
        elif not first==choice:
            print("You slipped and died 💀")
            health()


    

    
    if first=="2":
        if first==choice:
            print("You safely went around the rock! 🎉🌟✨")
        elif not first==choice:
            print("The water was too deep, you drowned 💀")
            health()

    
    
    
    if first=="3":
        if first==choice:
            print("You broke the rock! 🎉🌟✨")
        elif not first==choice:
            print("The rock collapsed on you 💀")
            health()



    
    # 2nd barrier 🐊
    print("\nBarrier 2: Crocodile 🐊")
    print("1 Sneak | 2 Run | 3 Attack")
    second = input("> ")

    choice = random.choice('123')
    


    if second=="1":
        if second==choice:
            print("The crocodile couldn't see you! 🎉🌟✨")
        elif not second==choice:
            print("The crocodiile saw you while sneaking 💀")
            health()

    

    
    if second=="2":
        if second==choice:
            print("The crocodile was too slow! 🎉🌟✨")
        elif not second==choice:
            print("The crocodile caught you 💀")
            health()

    
    
    
    if second=="3":
        if second==choice:
            print("You beat the crocodile! 🎉🌟✨")
        elif not second==choice:
            print("You lost the fight 💀")
            health()



    # 3rd barrier 🪵
    print("\nBarrier 3: Logs 🪵")
    print("1 Jump | 2 Swim | 3 Walk over")
    third = input("> ")
    
    choice = random.choice('123')

    if third=="1":
        if third==choice:
            print("You jumped over the log! 🎉🌟✨")
        elif not third==choice:
            print("You hit the log and died while trying to jump 💀")
            health()

    

    
    if third=="2":
        if third==choice:
            print("You swimmed through the log 🎉🌟✨")
        elif not third==choice:
            print("You got stuck inside the log 💀")
            health()

    
    
    
    if third=="3":
        if third==choice:
            print("You walked over the log! 🎉🌟✨")
        elif not third==choice:
            print("You slipped and fell 💀")
            health()





    
    # 4th barrier 🐍
    print("\nBarrier 4: Snake 🐍")
    print("1 Stay still | 2 Attack | 3 Run")
    fourth = input("> ")

    choice = random.choice('123')
    
    if fourth=="1":
        if fourth==choice:
            print("You avoided the snake! 🎉🌟✨")
        elif not fourth==choice:
            print("The snaked attacked you 💀")
            health()

    

    
    if fourth=="2":
        if fourth==choice:
            print("You killed the snake 🎉🌟✨")
        elif not fourth==choice:
            print("The snake bit you 💀")
            health()

    
    
    
    if fourth=="3":
        if fourth==choice:
            print("The snake was too slow! 🎉🌟✨")
        elif not fourth==choice:
            print("You were too slow 💀")
            health()


    # 5th barrier 🌪️
    print("\nBarrier 5: Storm 🌪️")
    print("1 Push forward | 2 Hide | 3 Wait")
    fifth = input("> ")

    
    choice = random.choice('123')

    if fifth=="1":
        if fifth==choice:
            print("You escaped the storm! 🎉🌟✨")
        elif not fifth==choice:
            print("You flew away, while trying to escape 💀")
            health()

    

    
    if fifth=="2":
        if fifth==choice:
            print("The storm couldn't catch you! 🎉🌟✨")
        elif not fifth==choice:
            print("The storm caught you 💀")
            health()

    
    
    
    if fifth=="3":
        if fifth==choice:
            print("The storm disappeared! 🎉🌟✨")
        elif not fifth==choice:
            print("The storm got even stronger 💀")
            health()


    # 6th barrier 🦈
    print("\nBarrier 6: Shark 🦈")
    print("1 Swim fast | 2 Float | 3 Dive")
    sixth = input("> ")

    choice = random.choice('123')

    if sixth=="1":
        if sixth==choice:
            print("The shark was too slow! 🎉🌟✨")
        elif not sixth==choice:
            print("You got caught 💀")
            health()

    

    
    if sixth=="2":
        if sixth==choice:
            print("The shark thought you were dead! 🎉🌟✨")
        elif not sixth==choice:
            print("You moved 💀")
            health()

    
    
    
    if sixth=="3":
        if sixth==choice:
            print("The shark couldn't reach deeper 🎉🌟✨")
        elif not sixth==choice:
            print("You drowned while trying to dive 💀")
            health()



    # 7th barrier 🪨
    print("\nBarrier 7: Rock 🪨")
    print("1 Climb | 2 Break | 3 Go around")
    seventh = input("> ")

    

    choice = random.choice('123')

    if seventh=="1":
        if seventh==choice:
            print("You climbed the rock! 🎉🌟✨")
        elif not seventh==choice:
            print("You slipped and died 💀")
            health()

    

    
    if seventh=="2":
        if seventh==choice:
            print("You safely went around the rock! 🎉🌟✨")
        elif not seventh==choice:
            print("The water was too deep, you drowned 💀")
            health()

    
    
    
    if seventh=="3":
        if seventh==choice:
            print("You broke the rock! 🎉🌟✨")
        elif not seventh==choice:
            print("The rock collapsed on you 💀")
            health()





    # 8th barrier 🐊
    print("\nBarrier 8: Final Crocodile 🐊")
    print("1 Sneak | 2 Run | 3 Trick it")
    eighth = input("> ")

    choice = random.choice('123')

    if eighth=="1":
        if eighth==choice:
            print("The crocodile couldn't see you! 🎉🌟✨")
        elif not eighth==choice:
            print("The crocodiile saw you while sneaking 💀")
            health()

    

    
    if eighth=="2":
        if eighth==choice:
            print("The crocodile was too slow! 🎉🌟✨")
        elif not eighth==choice:
            print("The crocodile caught you 💀")
            health()

    
    
    
    if eighth=="3":
        if eighth==choice:
            print("You beat the crocodile! 🎉🌟✨")
        elif not eighth==choice:
            print("You lost the fight 💀")
            health()


    
    # Final bridge 🌉
    print("\nFinal Barrier: Bridge 🌉")
    print("1 Cross carefully | 2 Run | 3 Jump")
    ninth = input("> ")

    choice = random.choice('123')

    if ninth=="1":
        if ninth==choice:
            print("Slow is steady and steady is fast! 🎉🌟✨")
        elif not ninth==choice:
            print("You were too late, the bridge collasped 💀")
            health()

    

    
    if ninth=="2":
        if ninth==choice:
            print("You ran before the bridge collasped! 🎉🌟✨")
        elif not ninth==choice:
            print("You were too slow, the bridge collasped 💀")
            health()

    
    
    
    if ninth=="3":
        if ninth==choice:
            print("You jumped over the bridge! 🎉🌟✨")
        elif not ninth==choice:
            print("You jumped through the bridge and fell into the abyss 💀")
            health()

    print("\n✨ Thank you, brave traveller. The path is now safe because of you 🏝️🏆")

    

   

    frames = [
    "   🎆   ",
    "  ✨🎆✨  ",
    " 🎆✨💥✨🎆 ",
    "✨🎇✨🎇✨",
    ]

    for f in frames:
        print("\r" + f, end="")
        time.sleep(0.5)

    print("\n🏝️ YOU MADE IT! YOU WIN 🏆")
    




elif qa=="no":
    print(f'My apologies {name}, continue on your journey')

else:
    print("I couldn't properly hear ya!")

