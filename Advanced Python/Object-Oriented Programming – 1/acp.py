# Robot Introduction using OOP

class Robot:
    # Constructor
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    # Method to introduce the robot
    def introduce(self):
        print("Hello! My name is", self.name)
        print("My model is", self.model)
        print("My purpose is", self.purpose)
        print("Nice to meet you!")

# Create an object
robot1 = Robot("Robo", "X-100", "Helping humans with daily tasks")

# Call the method
robot1.introduce()