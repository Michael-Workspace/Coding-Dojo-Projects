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

    def enroll(self):
        if self.is_rewards_member == True:
            print ("You are already a member")
            return 
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return
        
    def spend_points(self,amount):
        if self.gold_card_points < amount:
            return "You don't have enough Points!"
        else:
            self.gold_card_points = self.gold_card_points - amount
            return
        
first_user = user("Michael","Ngo", "michaelngo@gmail.com", 26) #first user input
first_user.enroll() #enroll first user
first_user.spend_points(50) #spend reward points
first_user.display_info() #display first user info
first_user.enroll()

second_user = user("Alexis", "Miller", "alexismiller@gmail.com", 24) #second user input
second_user.enroll() #enroll second user
second_user.spend_points(80) #spend reward points
second_user.display_info() #display second user info

third_user = user("Tana", "Inzar", "tanainzar@gmail.com", 29) #third user input
third_user.spend_points(40)
third_user.display_info() #display third user info


