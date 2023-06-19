import time
import sys

def boot_sequence_terminal():
    boot_sequence = "[REBOOTED] -- -- [REARMED]\n" \
                    "[RECHARGED] -- -- [REBUILT]\n" \
                    "[RESURRECTED!]"
    
    # Delay in seconds between printing each character
    delay = 0.05

    for char in boot_sequence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

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

boot_sequence_terminal()