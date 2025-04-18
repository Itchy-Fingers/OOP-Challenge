# This is a simple pet simulation program. The user can create a pet, feed it, play with it, and train it to perform tricks.
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5 # Initial hunger level; 0 = very hungry, 10 = very full
        self.energy = 5 # Initial energy level; 0 = very tired, 10 = very energetic
        self.happiness = 5 # Initial happiness level; 0 = very sad, 10 = very happy
        self.tricks = []

    def eat(self):
        #reduce hunger by 3 points but not below 0
        self.hunger = max(0, self.hunger - 3)
        
        #increase happiness by 1
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating.")
        
        
        
    def sleep(self):
        #increase energy by 5 points but not above 10
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping.")
        
        
        
        
    def play(self):
        # decrease energy by 2
        self.energy = max(0, self.energy - 2)
        
        #Increase hapiness by 2 points 
        self.happiness = min(10, self.happiness + 2)
        print(f"{self.name} is playing.")
        
        
        
        
    def train(self, trick):
        #teaches the pet a new tricks and store in the tricks in a list
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}.")
        
        
        

    def show_tricks(self):
        # display the tricks the pet has learned
        if self.tricks:
            print(f"{self.name} can do the following tricks: {', '.join(self.tricks)}")
            for trick in self.tricks:
                print(f"{self.name} can {trick}.")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
            
            
            
            
    def get_status(self):
        # display the pet's current status
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None'}")
        print("")


#Create a pet named "Max"
my_pet = Pet("Simba")

#Show pet's initial status
my_pet.get_status()

#Feed the pet and check the status
my_pet.eat()

#Let the pet sleep and check the status
my_pet.sleep()

#Teach the pet some tricks
my_pet.train("Sit")
my_pet.train("Roll Over")

#Show the tricks learned by the pet
my_pet.show_tricks()

#Let the pet play and check the status
my_pet.play()
my_pet.get_status()

