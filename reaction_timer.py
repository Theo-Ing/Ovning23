import time
import random

# Bestäm slumpmässig tid
wait_time = random.randint(1, 6)

# Vänta slumpmässig tid
time.sleep(wait_time)

# Starta tidmätning
start = time.time()

# Be om enter (och vänta på enter)
input("Tryck på enter!")

# Slutför tidmätning
end = time.time()

# Skriv ut hur lång tid det tog
print("Reaction time:", round(end - start, 6))