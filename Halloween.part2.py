from random import randint
from random import choice

class House:

    def __init__(self):

        self.rating = randint(1,10)

        
    def getRating(self):
        return self.rating


def greedyPath(m, num):
    bestHouses = []
    houses = []
    coordinates = []

    for i in range(5):
        for j in range(5):
            houses.append(m[i][j])
            coordinates.append([i,j])
    for i in range(25):
        maxHouse = houses[0]
        for h in houses:
            if h > maxHouse:
                maxHouse = h

        position = houses.index(maxHouse)
        bestHouses.append(coordinates.pop(position))
        houses.pop(position)
    
    #sort the houses in terms of best to worst
    

    #try to add coordinates to the path
    #if the path were to get stuck or be 'unfinished' in anyway, try again
    #using a new starting position
    #return once a fair path is generated
    #if no fair path found, return list of zeros as coordinates
    for i in range(25):
        p = []



        #keep track of the value of the path
        #pick the next best house to start with
        
        start = bestHouses[i]
        x = start[0]
        y = start[1]
        pVal = m[x][y]
        p.append(start)
        #add neighbors to the path after comparing to see which neighbor is best
        for i in range(num - 1):
            #check to see if we are stuck. If we get stuck, break

            neighbors = [[x, y-1], [x-1, y], [x+1, y], [x, y+1]]
            bad = []
            

 
            for n in neighbors:
                if (n[0] > 4) or (n[0] < 0):
                    bad.append(n)
                elif (n[1] > 4) or (n[1] < 0):
                    bad.append(n)
                elif n in p:
                    bad.append(n)

            for b in bad:
                neighbors.remove(b)

            if len(neighbors) == 0:

                break
            

            
            #check all possible neighbors. Choose the best neighbor
            #add it to the path and add to the value
            bestN = neighbors[0]
            broken = False
            for b in bestHouses:
                if broken:
                    break
                for n in neighbors:
                    if n == b:
                        bestN = n
                        broken = True
                        break

            p.append(bestN)
            x = bestN[0]
            y = bestN[1]
            pVal = pVal + m[x][y]


            #if path is complete, return path and path value
            if len(p) == num:

                return pVal, p
    
        return 0, [[0,0]]

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
            bad = []
            

 
            for n in neighbors:
                if (n[0] > 4) or (n[0] < 0):
                    bad.append(n)
                elif (n[1] > 4) or (n[1] < 0):
                    bad.append(n)
                elif n in p:
                    bad.append(n)

            for b in bad:
                neighbors.remove(b)

            if len(neighbors) == 0:

                break

                
            neighbor = choice(neighbors)
            p.append(neighbor)
            x = neighbor[0]
            y = neighbor[1]
            pVal = pVal + m[x][y]
                

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

    pVal, p = greedyPath(m,num)
    
    
    
    '''total = 0
    for i in range(5):
        for j in range(5):
            total = total + m[i][j]'''


    '''average = total/25
    
    pVal, p = randPath(m, num)
    
    while (average > pVal/num):
        pVal, p = randPath(m, num)'''

 
    print(p)

    #print("the average value in the path is:" +str(pVal/num))
    #print("The average value in the neigborhood is:" + str(average))

if __name__ == "__main__":
    main()


    
