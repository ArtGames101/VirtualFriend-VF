# (c) ArtGames101 2017
import sys, os, subprocess, time, psutil, random
from data import new
from data import name

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def welcome():
    if new.new == True:
        welcomer()
    else:
        main()


def welcomer():
    clear_screen()
    print("Hello! I am your Virtual Friend :D")
    input("\nEnter")
    clear_screen()
    print("Before We begin what is your name?")
    name = open("data/name.py", "w")
    choice = user_choice()
    name.write("name = '{}'".format(choice))
    clear_screen()
    input("Welcome!\n"
          "\n"
          "Enter")
    name.close()
    clear_screen()
    print("One more thing before we start!\n"
          "i have to tell you my features!")
    print("Features:\n"
          "\n"
          "* I can tell the time/date/year\n"
          "* I can talk to you\n"
          "* I can tell you a joke\n"
          "* I can remember things for you")
    newno = open("data/new.py", "w")
    newno.write("new = False")
    input("Have Fun with your new Virtual Friend!\n"
          "\n"
          "Enter")
    newno.close()
    subprocess.call((sys.executable, "run.py"))
    

def main():
    clear_screen()
    print("Hello {}!                                     v1.1".format(name.name))
    print("\n"
          "Your Virtual Friend is waiting for a responce!")
    print("\n"
          "1. Tell a joke   2. What is the time\n\n"
          "   3. Remember something for me\n"
          "               or\n"
          "    Type anything to talk to me!\n")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        from VFdata import jokes
        input("Here is a joke!\n"
              "\n"
              "{}".format(random.choice(jokes.jokes)))
        main()
    if choice == "2":
        clear_screen()
        input("The Time is currently:\n"
              "{}".format(time.ctime()))
        main()
    if choice == "3":
        from VFdata import remember
        if remember.text == None:
            clear_screen()
            print("Type something for me to remember!")
            choice = user_choice()
            rem = open("VFdata/remember.py", "w")
            rem.write("text = '{}'".format(choice))
            input("Come Back here to see your message!")
            rem.close()
            subprocess.call((sys.executable, "run.py"))
        else:
            from VFdata import remember
            clear_screen()
            print("I remember what you said here you go!\n"
                  "\n"
                  "{}".format(remember.text))
            print("\n"
                  "1. Delete the message  2. Save and Exit")
            choice = user_choice()
            if choice == "1":
                clear_screen()
                rem = open("VFdata/remember.py", "w")
                rem.write("text = None")
                input("Message Deleted!")
                rem.close()
                subprocess.call((sys.executable, "run.py"))
            if choice == "2":
                main()
                
        
    else:
        clear_screen()
        from VFdata import speach
        input(random.choice(speach.text))
        main()
    
welcome()
