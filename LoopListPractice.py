
def return7(l):

    for i in range (len(l)-1):

        if l[i] == 7 and l[i+1] == 7: 

            return ("True")
    return ("False")


def totalexcept5(l2):
    total = 0
    for i in range (len(l2)) :
        if l2[i] == 2 or l2[i] == 3 or l2[i] == 5 or l2[i] == 7 or l2[i] == 11:
             break
        else:
            total = total + l2[i]
    return(total)

def everythingexcept23(l3):
    add23 = True
    sum = 0
    for i in range (0, len(l3)):
            if l3[i] == 2:
               add23 = False
            elif add23 == False and l3[i] == 3:
                add23 = True
            elif add23 == True:
                sum = sum + l3[i]
    return sum

def main():
    #list1 = input("Write down the numbers in a list")
    myList = [1, 2, 3, 7, 7]
    print(return7(myList))
    List2 = [1, 7, 2, 7]
    print(return7(List2))
    List3 = [7, 8, 7]
    print(return7(List3))
    List4 = [1, 4, 2, 3, 6]
    print(totalexcept5(List4))
    List8 = [1, 20, 12, 8, 5, 8, 10]
    print(totalexcept5(List8))
    List9 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(totalexcept5(List9))
    List5 = [1, 4, 4]
    print(everythingexcept23(List5))
    List6 = [1, 5, 6, 2, 99, 56, 3]
    print(everythingexcept23(List6))
    List7 = [1, 3, 4, 2, 3, 8]
    print(everythingexcept23(List7))


        

if __name__ == "__main__":
    main()
