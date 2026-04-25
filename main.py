import os
os.system('cls')

from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def jump(self):
        pass

    @abstractmethod
    def kick(self):
        pass


class Vector(Player):
    def __init__(self, ball, heart):
        self.ball = ball
        self.heart = heart
    
    def run(self):
        print("Vector is running...")
    
    def kick(self):
        print("Vector is kicking...")
    
    def jump(self):
        print("Vector is jumping...")

    def fly(self):
        print("Vector is flying...")

v1 = Vector(100, 5)
v1.jump()
v1.run()
v1.kick()
v1.fly()