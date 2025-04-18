class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5       
        self.energy = 5       
        self.happiness = 5    
        self.tricks = []

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} eats well!")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} sleeps nice.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"{self.name} plays and always has fun")
        else:
            print(f"{self.name} is  tired to play.")

    def get_status(self):
        print(f"\n {self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 1, 10)
        self.energy = max(self.energy - 1, 0)
        print(f"{self.name} learned some new tricks: {trick}")

    def show_tricks(self):
        print(f"\n {self.name}'s Tricks:")
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            for trick in self.tricks:
                print(f"- {trick}")