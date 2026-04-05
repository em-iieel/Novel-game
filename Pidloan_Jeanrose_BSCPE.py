import time
import sys

def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def ganda():
    print("<><><<><><><><><><><><><><><><><><><><><><><><><><><>><")
    print("            ECHOES OF THE CRIMSON MASK                 ")
    print("<><><><><><><><><><><><><><>><><><><><><><><><><><><><>")
    print(" ")

def pogi():
    while True:
        print(" ")
        m = input("What does your heart tell you to do? (A, B, or C): ")
        print(" ")
        
        if m == "A":
            return m
        elif m == "B":
            return m
        elif m == "C":
            return m
        else:
            slow_print("That choice leads to heartbreak. You must pick A, B, or C.")
            print(" ")

def asim():
    ganda()
    slow_print("The year is 1888. The air in Paris is thick with perfume and music.")
    slow_print("You are Clara Valmont, a talented violinist invited to the Grand Gala.")
    slow_print("Rumor has it that the reclusive Duke of Morelle will choose a bride tonight.")
    slow_print("You aren't here for marriage, but for the chance to play for the elite.")
    slow_print("The carriage stops. You step out, clutching your velvet evening bag.")
    slow_print("Inside your bag, you have prepared three things:")
    print(" ")
    
    for item in "A Lace Handkerchief", "A Golden Invitation", "A Scented Love Letter":
        slow_print(" ITEM IN HAND: " + item)
        
    print(" ")
    slow_print("The Opera House glows like a jewel box under the moon.")
    slow_print("How do you wish to make your grand entrance?")
    slow_print("A) Walk up the grand stairs and present your invitation.")
    slow_print("B) Slip through the garden path to avoid the paparazzi.")
    slow_print("C) Climb the side terrace to find a quiet spot to practice.")

    v = pogi()

    if v == "A":
        panot()
    elif v == "B":
        kalbo()
    elif v == "C":
        butaw()

def panot():
    slow_print("The usher bows deeply as you present your golden card.")
    slow_print("Inside, a handsome stranger in a silver mask blocks your path.")
    slow_print("He offers his hand, his eyes sparkling behind the silk.")
    slow_print("'A lady as beautiful as you shouldn't dance alone,' he whispers.")
    print(" ")
    slow_print("A) Politely decline and look for the stage.")
    slow_print("B) Accept the dance and see where it leads.")
    slow_print("C) Ask him if he knows the Duke's true identity.")

    j = pogi()
    if j == "B":
        slow_print("The music swells. He spins you into the center of the ballroom.")
        print(" ")
        sapak()
    else:
        slow_print("He takes offense and walks away. You feel suddenly lonely.")
        print(" ")
        palo()
        
def kalbo():
    slow_print("The garden is filled with the scent of jasmine and roses.")
    slow_print("The moonlight creates silver patterns on the grass.")
    slow_print("You find a hidden gazebo. Inside, a man is sitting in the dark.")
    print(" ")
    slow_print("A) Ask him why he is hiding from the party.")
    slow_print("B) Hide behind a rosebush and listen to him play the flute.")
    slow_print("C) Try to sneak past him toward the back stage.")

    h = pogi()
    if h == "B":
        slow_print("His music is the most beautiful thing you have ever heard.")
        print(" ")
        sapak()
    else:
        slow_print("You trip over a vine! He leaves in a hurry, thinking you're a spy.")
        print(" ")
        palo()

def butaw():
    slow_print("You climb the stone stairs to the high terrace.")
    slow_print("The view of Paris is breathtaking from up here.")
    print(" ")
    slow_print("A) Sing a song to the stars.")
    slow_print("B) Pick the lock of the French doors to enter the VIP lounge.")
    slow_print("C) Lean over the railing and wait for the fireworks.")

    l = pogi()
    if l == "B":
        slow_print("The lock clicks. You find yourself in a private, candle-lit library.")
        print(" ")
        sapak()
    else:
        slow_print("A guest of wind blows your invitation away! You cannot enter.")
        print(" ")
        palo()

def sapak():
    slow_print("You are now in the presence of the mysterious Duke.")
    slow_print("He removes his mask, revealing the man you saw earlier.")
    print(" ")
    slow_print("A) Ask him about the locket hanging from his neck.")
    slow_print("B) Recite the poem you wrote in your letter.")
    slow_print("C) Hand him a glass of vintage wine.")

    f = pogi()
    if f == "A":
        slow_print("He opens the locket. It holds a picture of a violin—your violin!")
        print(" ")
        hansam()
    else:
        slow_print("The moment is awkward. He realizes you aren't the one.")
        print(" ")
        palo()

def hansam():
    slow_print("He confesses he has been looking for the owner of that violin for years.")
    print(" ")
    slow_print("A) Tell him you have a secret to share.")
    slow_print("B) Play a melody for him right there in the room.")
    slow_print("C) Look for the sheet music hidden in his desk.")

    u = pogi()
    if u == "C":
        slow_print("You find a song written for you. The notes match your soul!")
        print(" ")
        # Using palo logic branch here as per original flow
        slow_print("The Duke takes your hand and looks into your eyes.")
        slow_print("The clock begins to strike midnight. The party is ending.")
        print(" ")
        slow_print("A) Run away before the last strike.")
        slow_print("B) Step onto the balcony and share a kiss.")
        slow_print("C) Ask him to meet you at the bridge tomorrow.")

        e = pogi()
        if e == "B":
            # Success ending
            print(" ")
            slow_print(" The Good Ending: Eternal Love ")
            print(" ")
            slow_print("The fireworks explode as you find your true soulmate.")
            slow_print("The night ends, but your story is only beginning.")
        else:
            palo()
    else:
        slow_print("He loses interest as the magic of the night fades away.")
        print(" ")
        palo()

def palo():
    print(" ")
    slow_print(" The Bad Ending: A Lonely Night ")
    print(" ")
    slow_print("The romance of Paris fades as you walk home alone.")
    slow_print("The Duke remains a mystery, and your heart remains heavy.")

while True:
    asim()
    print(" ")
    y = input("Would you like to seek love again? (YES/NO): ")
    
    if y == "YES":
        print("Restarting...")
        print(" ")
    elif y == "yes":
        print("Restarting...")
        print(" ")
    elif y == "Yes":
        print("Restarting...")
        print(" ")
    else:
        slow_print("Farewell, romantic. May you find love elsewhere!")
        break
