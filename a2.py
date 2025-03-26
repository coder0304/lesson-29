from abc import ABC, abstractmethod

class animal(ABC):
    def move(self):
        print
class human(animal):
    def move(self):
        print("I can walk and run")
class Snake(animal):
    def move(self):
        print("I can crawl")
class dog(animal):
    def move(self):
        print("I can bark")
class lion(animal):
    def move(self):
        print("I can roar")
R=human()
R.move() 

K=Snake()
K.move() 

R=dog()
R.move() 

K=lion()
K.move() 