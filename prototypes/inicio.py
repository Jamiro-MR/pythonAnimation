import time
import sys

words = ["[REBOOTED]", "[REARMED]", "[RECHARGED]", "[REBUILT]", "[RESURRECTED!]"]

def show_loading_bar():
    width = 40  # Width of the loading bar
    duration = 0.1  # Duration of each loading step in seconds

    for word in words:
        print("Loading...")

        for i in range(width + 1):
            progress = i / width * 100
            loading_bar = f"[{'=' * i}>{' ' * (width - i)}] {progress:.0f}%"
            print(loading_bar, end='\r')
            time.sleep(duration)

        print(f"\n{word}\n")
        time.sleep(1)  # Pause after displaying the word

    # New line after the boot sequence
    print()
    
    # Formatting for "[INITIATING OBJECT_HUMAN]"
    init_sequence = "\033[95m\033[1m[INITIATING OBJECT_HUMAN]\033[0m"
    # Delay in seconds between printing each character for init_sequence
    init_delay = 0.1

    for char in init_sequence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(init_delay)

show_loading_bar()