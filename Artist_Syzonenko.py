import turtle

class Artist:

    def __init__(self, t):
        self.t = t
    
    def triangle(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)
    
    def square(self, size = 100):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)
    
    def star(self, size = 100):
        for i in range(5):
            self.t.right(144)
            self.t.forward(size)

    def circle(self, size = 5):
       for i in range(75):
            self.t.right(5)
            self.t.forward(size)

    def polygon(self, size = 100):
        n = int(input("Write the number of the sides of the polygon : "))
        x = int(input("Write the length of the sides of the polygon : "))
        for i in range(n):
            self.t.right(360/n)
            self.t.forward(x)

    def c(self):
            self.t.circle(25, -180)
    
            
    def o(self, size = 2):
        for i in range(75):
            self.t.right(5)
            self.t.forward(size)

    def l(self, size = 50):
            self.t.right(70)
            self.t.backward(size)
            self.t.right(90)
            self.t.forward(40)         

    def u(self, size = 20):
            self.t.right(90)
            self.t.forward(size)
            self.t.circle(25,180)
            self.t.forward(size)

    def m(self):
            self.t.forward(50)
            self.t.left(30)
            self.t.backward(40)
            self.t.right(60)
            self.t.forward(40)
            self.t.left(30)
            self.t.backward(50)

    def b(self):
        self.t.forward(40)
        self.t.right(180)
        self.t.circle(15,-240)
        self.t.right(180)
        self.t.circle(15,-240)
        self.t.left(207)
        self.t.forward(25)
        
    def i(self):
        self.t.right(85)
        self.t.forward(50)

    def a(self):
        self.t.left(90)
        self.t.forward(30)
        self.t.left(45)
        self.t.forward(30)
        self.t.backward(70)
        self.t.left(45)
        self.t.forward(65)

    def crown(self):
        self.t.left(180)
        self.t.forward(50)
        self.t.left(30)
        self.t.backward(40)
        self.t.right(60)
        self.t.forward(40)
        self.t.left(30)
        self.t.backward(40)
        self.t.right(60)
        self.t.forward(40)
        self.t.left(30)
        self.t.backward(50)
        self.t.left(105)
        self.t.forward(55)

    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

def main():

    canvas = turtle.Screen()
    canvas.bgcolor("pink")
    canvas.title("Turtle Example")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(1)
    art = Artist(t)
    art.move(-200,300)
    art.triangle()
    art.move(-100, 250)
    art.square()
    art.move(50, 250)
    art.star()
    art.move(200, 300)
    art.circle()
    art.move(250, 150)
    art.polygon()
    art.move(-200, -100)
    art.c()
    art.move(-150, -100)
    art.o()
    art.move(-100, -50)
    art.l()
    art.move(-50, -60)
    art.u()
    art.move(20, -100)
    art.m()
    art.move(90, -100)
    art.b()
    art.move(160, -100)
    art.i()
    art.move(230, -80)
    art.a()
    art.move(20, -200)
    art.crown()
    art.move(20, -250)
    
    
    


if __name__ == "__main__":
    main()
