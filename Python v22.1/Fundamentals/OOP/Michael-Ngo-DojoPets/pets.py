class Pet:
    def __init__(self, name:str, type:str, tricks:str):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        
    def sleep(self):
        self.energy +=25
        return self
    
    def eat(self):
        self.energy +=5
        self.health +=10
        return self
    
    def play(self):
        self.health -=5
        return self
    
    def noise(self):
        print("meow")
        return self
    
    def display_pet(self):
        print(f"Pet: {self.name}, Type: {self.type}, Trick: {self.tricks}, Health: {self.health}, Energy: {self.energy}")
        return self