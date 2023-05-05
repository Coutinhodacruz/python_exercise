import time
import random

# Get the current time in seconds since the Epoch
current_time = int(time.time())

# Use the current time as the seed for the random number generator
random.seed(current_time)

# Generate a random uppercase letter
letter = chr(random.randint(65, 90))

print(f"The random uppercase letter is {letter}.")
