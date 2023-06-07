import random


class Cart():
    
    def __init__(self):
        self.shop_cart= {}
        self.random_add = ["Here ya go!", "Voila!", "Pop goes the weasel!", "Shazam!", "BOOM BABY!"]
        self.random_remove = ["I'll take that!", "Up Up and Away!", "Go'n Git!", "Get outta my garbage", "Sayonara Sucka!"]

    def add_item(self):
        item = input("What would you like to add? ")
        quantity = int(input(f"how many {item} would you like? "))
        print(random.choice(self.random_add))

        if item not in self.shop_cart:
            self.shop_cart[item] = quantity

    def remove_item(self):
        item = input("What would you like to remove?")
        del self.shop_cart[item]
        print(random.choice(self.random_remove))

    def see_cart(self):
        print(self.shop_cart)

    def checkout(self):
        print("Thanks for shopping!")
        print(f"Your cart: {self.shop_cart}")


def run():
    go = Cart()
    while True:
        welcome = input("Welcome to your shopping cart! Tell me if you would like to add, remove, or show items in your shopping cart: ").lower()
        if welcome == 'quit':
            go.checkout()
            break
        elif welcome == 'remove':
            go.remove_item()
        elif welcome == 'show':
            go.see_cart()
        elif welcome == 'add':
            go.add_item()
        else:
            print("Please enter add, remove, show, or quit")
run()
