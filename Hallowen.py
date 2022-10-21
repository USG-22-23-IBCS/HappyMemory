import random

class House:

    def __init__(self):

        self.visiting = False

        self.rating = random.randint(1,10)

    def visitedhouse(self):
        self.visiting = True
         
    def getRating(self):
        return self.rating

def bestHouse(m):

    besthouse = None
    bestlocation = (0, 0)
    
    for x in range(len(m)):
        l= m[x]
        for y in range(len(l)):
            house = l[y]
            if besthouse is None:
                besthouse = house
                continue
        
            if house.getRating() > besthouse.getRating():
                bestlocation = (x,y)
                besthouse = house

    return(bestlocation)



def getadjacenthouses(m, x, y):

    ratings = []
    
    if (x+1 < 5) and (m[x+1][y].visiting == False):
        ratings.append(m[x+1][y].getRating())
    if (y+1 < 5) and (m[x][y+1].visiting == False):
        ratings.append(m[x][y+1].getRating())
    if (x-1 > -1) and (m[x-1][y].visiting == False):
        ratings.append(m[x-1][y].getRating())
    if (y-1 > -1) and (m[x][y-1].visiting == False):
        ratings.append(m[x][y-1].getRating())  

    maxnum = max(ratings)

    indexI = ratings.index(maxnum)

    if indexI == 0:
        return [x+1, y, ratings[0]]
    if indexI == 1:
        return [x, y+1, ratings[1]]
    if indexI == 2:
        return [x-1, y, ratings[2]]
    if indexI == 3:
        return [x, y-1, ratings[3]]   


def main():
    
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            l.append(House())
    for l in m:
        print("\n")
        for house in l:
            print(house.getRating(), end = "  ")
    print("\n")



  
    bestlocation = bestHouse(m)
    sums = m[bestlocation[0]][bestlocation[1]].getRating()
    print(sums)
    print(bestlocation)
    
    
    num = int(input("how many houses do you want to visit?"))

    for k in range(num):
        temp = getadjacenthouses(m, bestlocation[0], bestlocation[1])
        m[temp[0]][temp[1]].visitedhouse()
        
        
        sums = sums + temp[2]
        print(temp)

        for l in m:
            print("\n")
            for house in l:
                print(house.visiting, end = "  ")
        print("\n")

        x = temp[0]
        y = temp[1]

    print(sums/num)
        
        
        
if __name__ == "__main__":
    main()
