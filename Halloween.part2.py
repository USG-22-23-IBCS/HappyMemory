from random import randint
from random import choice

class House:

    def __init__(self):

        self.rating = randint(1,10)

        
    def getRating(self):
        return self.rating


def randPath(m, num):
    p = []
    
    while (len(p) < num):
        p = []

        x = randint(0,4)
        y = randint(0,4)
        pVal = m[x][y]
        p.append([x,y])

        for i in range(num - 1):
            neighbors = [[x, y-1], [x-1, y], [x+1, y], [x, y+1]]

            stuck = True
            for n in neighbors:
                if (n[0] < 5) and (n[0] > -1):
                    if (n[1] < 5) and (n[1] > -1):
                        if n not in p :

                            stuck = False

            if stuck:
                break

            while True:
                
                neighbor = choice(neighbors)
            

                if (neighbor[0] < 5) and (neighbor[0] > -1):
                    if (neighbor[1] < 5) and (neighbor[1] > -1):
                        if neighbor not in p:
                            p.append(neighbor)
                            x = neighbor[0]
                            y = neighbor[1]
                            pVal = pVal + m[x][y]
                            break

        return pVal, p
             
                
def main():
    
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            l.append(House().getRating())
    for l in m:
        print("\n")
        for house in l:
            print(house, end = "  ")
    print("\n")


    num = int(input("how many houses do you want to visit?"))
    p, pVal = randPath(m, num)
    print(p, pVal)

if __name__ == "__main__":
    main()


    
