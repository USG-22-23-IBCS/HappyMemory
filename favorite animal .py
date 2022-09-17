
class favoriteanimal:

    #constructor method has all of the instance variables (values/data)
    def __init__(self, animal, kind, gender, col, x):
        self.gender = gender
        self.animal = animal 
        self.color = col
        self.kind = kind
        self.age = x
        

    
    def setgender(self, b):
        self.gender = b
        
    def getgender(self):
        return self.gender
        
    def getanimal(self):
        return self.animal

    def getkind(self):
        return self.kind
    
    def setcolor(self, c):
        self.color = c

    def getcolor(self):
        return self.color

    def setage(self, a):
        self.age = a

    def getage(self):
        return self.age

def main():

    animal1 = favoriteanimal("alpaca", "mammal", "female", "brown", 16)

    print(animal1.getanimal())
    print(animal1.getgender())
    animal1.setgender("male")
    print(animal1.getgender())
    print(animal1.getkind())
    print(animal1.getcolor())
    animal1.setcolor("white")
    print(animal1.getcolor())
    print(animal1.getage())
    animal1.setage(10)
    print(animal1.getage())
    



if __name__ == "__main__":
    main()

