import time
import pyttsx3

words = ["[REBOOTED]", "[REARMED]", "[RECHARGED]", "[REBUILT]", "[RESURRECTED!]"]

# Initialize the speech engine
engine = pyttsx3.init()

def typewriter_effect(text):
    lines = text.split("\n")
    for line in lines:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.05)  # Delay between each character
        print()  # New line after each line of text

def show_loading_bar():
    width = 40  # Width of the loading bar
    duration = 0.1  # Duration of each loading step in seconds

    intro_text = """
    This program implements an application that
    creates an entity with no meaning or purpose.

    \033[32m@author Jamiro\033[0m
    """

    # Display introduction with typewriter effect
    typewriter_effect(intro_text)

    for word in words:
        print("Loading...")

        for i in range(width + 1):
            progress = i / width * 100
            loading_bar = f"[{'=' * i}>{' ' * (width - i)}] {progress:.0f}%"
            print(loading_bar, end='\r')
            time.sleep(duration)

        print(f"\n\033[35m{word}\033[0m")  # Display word

        # Set the voice to a robotic one
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)  # Index from 0 to 2 decides the voice(2 is the best)

        # Speak the word using text-to-speech
        engine.say(word)
        engine.runAndWait()

        time.sleep(1)  # Pause after displaying the word

    # New line after the boot sequence
    print()

    # Formatting for "[INITIATING OBJECT_HUMAN]"
    init_sequence = "\033[32m\033[1m[INITIATING OBJECT_HUMAN]\033[0m"
    # Delay in seconds between printing each character for init_sequence
    init_delay = 0.1

    # Display init_sequence with typewriter effect
    typewriter_effect(init_sequence)

    # ASCII
    ascii_art = """
    ⠄⣾⣿⡇⢸⣿⣿⣿⠄⠈⣿⣿⣿⣿⠈⣿⡇⢹⣿⣿⣿⡇⡇⢸⣿⣿⡇⣿⣿⣿
    ⢠⣿⣿⡇⢸⣿⣿⣿⡇⠄⢹⣿⣿⣿⡀⣿⣧⢸⣿⣿⣿⠁⡇⢸⣿⣿⠁⣿⣿⣿
    ⢸⣿⣿⡇⠸⣿⣿⣿⣿⡄⠈⢿⣿⣿⡇⢸⣿⡀⣿⣿⡿⠸⡇⣸⣿⣿⠄⣿⣿⣿
    ⢸⣿⡿⠷⠄⠿⠿⠿⠟⠓⠰⠘⠿⣿⣿⡈⣿⡇⢹⡟⠰⠦⠁⠈⠿⠿⠃⠿⣿⡿
    ⡇⢸⠃⢀⣴⡆⠄⢀⣀⠄⣀⣀⡀⠙⣿⡇⢸⣿⣀⣀⡀⠄⢀⣀⠄⢀⣠⣤⣾⣿
    ⢃⠈⠲⣿⡿⠁⢰⣿⣿⡄⠈⠻⣿⣿⠃⢸⣿⡇⢸⣿⣿⡇⠘⢿⣿⣿⠟⣿⣿⣿
    ⢿⣄⠈⠻⢿⣦⡈⠿⢿⣿⡇⢠⣾⣿⠄⠸⣿⡇⢸⣿⣿⡇⢀⣾⡿⠋⢸⣿⡿⠁
    ⡏⠈⢿⣶⣤⡈⠻⠿⠟⠁⠈⠻⠿⠇⢰⣿⣿⣿⣿⠿⠇⣰⣿⣿⠟⠁⢸⠟⠁
    ⡇⢀⠘⠿⣿⣿⣦⣄⣀⡀⠄⠄⠄⢀⣿⣿⣿⠟⠁⢀⣿⣿⣿⡟⠁⣠⣾
    ⢳⣤⡄⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⢀⣾⣿⣿⠿⠋⣀⣾⣿⣿⣷⣿⣿
    ⡸⢿⣿⡀⠄⠄⠈⠻⠿⠿⠿⠿⠿⠿⠋⣠⣾⣿⠟⠋⠄⣀⣴⣿⡿⠟⣿⣿⣿⣿
    ⢇⣿⣿⣇⣀⡀⠄⠄⢀⣀⠄⠄⣀⣴⣿⣿⠟⠄⢠⣾⣿⡿⠁⢀⣾⣿⣿⣿⣿⣿
    ⢸⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    """

    # Display ASCII art with typewriter effect
    typewriter_effect(ascii_art)

show_loading_bar()