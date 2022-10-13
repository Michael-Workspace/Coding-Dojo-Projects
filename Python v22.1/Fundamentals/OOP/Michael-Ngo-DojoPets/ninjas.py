from pets import *

class Ninja():
    def __init__(self,first_name:str,last_name:str,treats:str, pet_food:str):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet(name='Bob',type='Cat',tricks='backflip')
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()
        return self
    
    def display_pet(self):
        self.pet.display_pet()
        return self

pet = Pet('Bob','Cat','Backflip')
ninja = Ninja('Michael', 'Ngo', 'Cake', 'Steak')
ninja.feed().walk().bathe().display_pet()