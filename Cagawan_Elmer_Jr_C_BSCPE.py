import time
import sys

def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def andok():
    print("------------------------------------------------")
    print("           THE SECRETS OF RAVENWOOD             ")
    print("------------------------------------------------")
    print(" ")

def baldo():
    while True:
        print(" ")
        c = input("What is your next move, Detective? (A, B, or C): ")
        print(" ")
        
        if c == "A":
            return c
        elif c == "B":
            return c
        elif c == "C":
            return c
        else:
            slow_print("That choice leads nowhere. You must pick A, B, or C.")
            print(" ")

def dusurb():
    andok()
    slow_print("The year is 1947. Rain slickens the cobblestone streets of the city.")
    slow_print("You are Detective Elias Thorne, a man with a tired heart and a sharp mind.")
    slow_print("A wealthy widow has hired you to find a stolen diamond necklace.")
    slow_print("The trail has led you to Ravenwood Manor, a house full of secrets.")
    slow_print("The iron gates groan as you push them open, stepping into the fog.")
    slow_print("You reach into your trench coat and check your supplies:")
    print(" ")
    
    for item in "A Silver Lighter", "A Loaded Revolver", "A Scratched Notepad":
        slow_print(" POCKET ITEM: " + item)
        
    print(" ")
    slow_print("The manor stands like a giant beast against the stormy sky.")
    slow_print("How do you intend to start your investigation?")
    slow_print("A) Approach the Grand Front Entrance and knock loudly.")
    slow_print("B) Creep around to the Servant's Entrance in the back.")
    slow_print("C) Scale the trellis to the second-story Balcony.")

    bisa = baldo()

    if bisa == "A":
        hatdog()
    elif bisa == "B":
        inam()
    elif bisa == "C":
        jamming()

def hatdog():
    slow_print("You hammer your fist against the heavy oak doors.")
    slow_print("A pale butler with eyes like cold marbles opens the door.")
    slow_print("He looks at your muddy shoes with deep disgust.")
    slow_print("'The Master is not seeing visitors,' he sneers, trying to close the door.")
    print(" ")
    slow_print("A) Push the door open and demand entry.")
    slow_print("B) Slip him a twenty-dollar bill to let you in.")
    slow_print("C) Ask him about the mysterious lady in the red dress.")

    olats = baldo()
    if olats == "B":
        slow_print("The butler's eyes brighten. He lets you into the Grand Hall.")
        print(" ")
        oblak()
    else:
        slow_print("He slams the door on your hand! You are forced to leave.")
        print(" ")
        muntanga()
        
def inam():
    slow_print("You slip through the shadows of the kitchen garden.")
    slow_print("The smell of damp earth and rotting leaves is thick here.")
    slow_print("You find the servant's door unlocked. Inside, the kitchen is dark.")
    print(" ")
    slow_print("A) Search the pantry for hidden documents.")
    slow_print("B) Hide in the shadows and wait for someone to pass.")
    slow_print("C) Try to find the basement stairs.")

    nigs = baldo()
    if nigs == "B":
        slow_print("You see a maid carrying a heavy velvet box toward the study.")
        print(" ")
        oblak()
    else:
        slow_print("A cook finds you and screams for the guards!")
        print(" ")
        muntanga()

def jamming():
    slow_print("The wooden trellis creaks under your weight as you climb.")
    slow_print("You reach the balcony and peer through the glass doors.")
    print(" ")
    slow_print("A) Break the glass and jump inside.")
    slow_print("B) Use a lockpick to open the latch.")
    slow_print("C) Wait and watch the room for activity.")

    pake = baldo()
    if pake == "B":
        slow_print("You slip inside the Master Bedroom quietly.")
        print(" ")
        oblak()
    else:
        slow_print("The trellis breaks! You fall into the rose bushes.")
        print(" ")
        muntanga()

def oblak():
    slow_print("You have made it inside the inner sanctum of the manor.")
    slow_print("The walls are lined with old paintings that seem to watch you.")
    print(" ")
    slow_print("A) Search behind the large portrait of Lord Ravenwood.")
    slow_print("B) Inspect the desk for secret compartments.")
    slow_print("C) Check the fireplace for hidden levers.")

    banana = baldo()
    if banana == "A":
        slow_print("The painting swings open, revealing a heavy iron safe!")
        print(" ")
        rara()
    else:
        slow_print("You trigger a silent alarm. The guards are coming!")
        print(" ")
        muntanga()

def rara():
    slow_print("The safe is locked with a complex combination.")
    print(" ")
    slow_print("A) Try to crack the code using your stethoscope.")
    slow_print("B) Blow the door off with a small explosive.")
    slow_print("C) Look for the code written under the desk lamp.")

    sup = baldo()
    if sup == "C":
        slow_print("You find the numbers 4-10-22. The safe clicks open!")
        print(" ")
        timang()
    else:
        slow_print("The safe locks permanently. You have failed.")
        print(" ")
        muntanga()

def timang():
    slow_print("Inside the safe lies the diamond necklace, glittering like ice.")
    slow_print("Suddenly, you hear footsteps outside the door.")
    print(" ")
    slow_print("A) Hide in the wardrobe and wait.")
    slow_print("B) Jump out the window with the jewels.")
    slow_print("C) Face the intruder with your revolver.")

    uno = baldo()
    if uno == "B":
        lalers()
    else:
        slow_print("You are outnumbered and trapped.")
        print(" ")
        muntanga()
        
def lalers():
    print(" ")
    slow_print(" The Good Ending: Case Closed ")
    print(" ")
    slow_print("You land in the grass and disappear into the night.")
    slow_print("The necklace is returned, and justice is served.")

def muntanga():
    print(" ")
    slow_print(" The Bad Ending: Case Closed ")
    print(" ")
    slow_print("The mystery of Ravenwood Manor swallows you whole.")
    slow_print("You walk back into the rain, empty-handed and defeated.")

while True:
    dusurb()
    print(" ")
    again = input("Would you like to try the mystery again? (YES/NO): ")
    
    if again == "YES":
        print("Restarting...")
        print(" ")
    elif again == "yes":
        print("Restarting...")
        print(" ")
    elif again == "Yes":
        print("Restarting...")
        print(" ")
    else:
        slow_print("Thanks for playing, Detective. Goodbye!")
        break