class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Reward Member: {self.is_rewards_member}")
        print(f"Reward Point: {self.gold_card_points} Points")
        print("=================================")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print ("You are already a member")
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self
        
    def spend_points(self,amount):
        if self.gold_card_points < amount:
            print("You don't have enough Points!")
            return self
        else:
            self.gold_card_points = self.gold_card_points - amount
            return self
        
first_user = user("Michael","Ngo", "michaelngo@gmail.com", 26) #first user input
first_user.enroll().spend_points(50).display_info().enroll()

second_user = user("Alexis", "Miller", "alexismiller@gmail.com", 24) #second user input
second_user.enroll().spend_points(80).display_info()

third_user = user("Tana", "Inzar", "tanainzar@gmail.com", 29) #third user input
third_user.spend_points(40).display_info()


