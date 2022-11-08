
class Grocerystore:

    def __init__(self):
        
        self.products = {"salmon" : 15.25,
                         "chocolate milk": 4.34,
                         "bananas": 2.23,
                         "dragonfruit": 10.45,
                         "chocolate": 7.75,
                         "grapes": 3.8,
                         "cherry turnover": 1.50,
                         "fruitsnacks": 30.76,
                         "tomatoes": 5.98,
                         "broccoli": 6.78,
                         "rice": 2.45,
                         "pasta": 5.40,
                         "eggs": 7.65,
                         "cereal": 5.67,
                         "avocado": 5.45,
                         "bagel": 3.20,
                         "yogurt": 4.15,
                         "chicken breast": 13.45,
                         "milk": 4.56,
                         "cheese": 8.97,
                         "granola bar": 2.23,
                         "shrimp": 20.05,
                         "cake": 30.99,
                         "pickles": 8.98,
                         "watermelon": 15.45,
                         "tortillas": 7.67,
                         "bread": 4.96,
                         "nuts": 8.07,
                         "feta": 9.87,
                         "ice cream": 6.05,
                         "sour patch kids": 4.02,
                         "ranch": 5.45,
                         "goldfish": 8.78}

        self.sold = ["salmon", "ranch", "goldfish", "chicken breast", "tomatoes", "granola bar", "milk", "pickles", "grapes", "cherry turnover"]


        self.nameofthestore = "Vesna"
        self.nameofthemanager = "Ed Sheeran"



    def getproducts(self):
        listofitems = list(self.products.keys())
        productsavailable = []
        for i in listofitems:
            if i not in self.sold:
                productsavailable.append(i)

        return productsavailable
    
    def getname(self):
        return self.nameofthestore

    def getdictionary(self):
        return self.products

    def getmanager(self):
        return self.nameofthemanager
                    
def main():

    Buy = Grocerystore()

    input("Hello! Welcome to the grocery store " + " " + Buy.getname()+ "!")
    name = input("What is your name?")
    answer = input("How can I help you,"+ name + "?" + "\nPlease pick an option:\n 1. Look at available list of products\n 2. Check whether certain product is available\n 3. Buy groceries\n 4. Talk to the manager\n")
    if answer == '1':
        print(Buy.getproducts())
    if answer == '2':
        available = input("Enter the products you want to check\n")
        if available in Buy.getproducts():
             print("This item is available!")
        else:
            print("Sorry this item is out of stock!")
    if answer == '3':
            g = input("Enter the list of products you are willing to purchase\n")
            L = g.split()

            total = 0
            for f in L:
                Buy.getdictionary().get(f)
                total = total + (Buy.getdictionary().get(f))
            print("Your total is:" + " " + str(total) + " " + "dollars!")
    if answer == '4':
        print("Hello! Nice to meet you! I am your online consultant!\n My name is" + " " + Buy.getmanager() + ", " + "how can I help you?\n")
        concern = input("Choose an option:\n 1. Write a complaint\n 2. Ask a question\n")
        if concern == '1':
            print("Please email vesnasupport@gmail.com or call +12534567865 to address your complaint")
        else:
            question = input("Please write your questions here and your phone number and our manager will reach out to you as soon as possible!")

    print("Thank you for choosing Vesna! Have a fantastic day!")

if __name__ == "__main__":
    main()
                          
        
