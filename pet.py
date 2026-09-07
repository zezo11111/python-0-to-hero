import re
import time
class pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
    def __str__(self):
        return f"{self.name} - Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}"
    def feed_pet(self):
        self.hunger -= 10
        self.energy += 5
        print (f"{self.name} has been fed. Hunger: {self.hunger}, Energy: {self.energy}")
    def play_with_pet(self):
        self.happiness += 10
        self.energy -= 5
        self.hunger += 5
        print (f"{self.name} has played. Happiness: {self.happiness}, Energy: {self.energy}, Hunger: {self.hunger}")
    def sleep(self):
        self.energy += 20
        self.hunger += 10

g_time = 0


print("Your goal is to reach 100 points in each category. You can feed, play with, or let your pet sleep to increase their stats. Be careful not to let any stat drop too low!")
pet1 = pet(input("Enter your pet's name: "))
while True:
    b=input("Do you want to feed, play with, or let your pet sleep? (feed/play/sleep): ")
    if re.search(r'^f(e{2})d$', b, re.IGNORECASE):
         pet1.feed_pet()
    elif b.startswith("pl") and len(b) > 3:
        pet1.play_with_pet()
    else:
        pet1.sleep()
    print(f"{pet1.name} - Hunger: {pet1.hunger}, Energy: {pet1.energy}, Happiness: {pet1.happiness}")
    g_time += 1
    print(f"Time: {g_time}")
    time.sleep(1)
    if pet1.hunger <= 0 or pet1.energy <= 0 or pet1.happiness <= 0:
        pet1.hunger=0
        pet1.energy=0
        pet1.happiness=0
        print(f"{pet1.name} has passed away. Game over.")
        break
    elif pet1.hunger >= 100 and pet1.energy >= 100 and pet1.happiness >= 100:
        print(f"{pet1.name} has reached all goals! You win!")
        pet1.hunger = 100
        pet1.energy = 100
        pet1.happiness = 100
        break
        print(f"You finished the game in {g_time} seconds.")