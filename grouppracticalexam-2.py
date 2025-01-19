"""
WORK IN PROGRESS!!!
Mostly complete na sya except:
    1. Paano i-truncate yung first column pag ini-display
yung list gamit yung [L]ist command? Max 25 characters sya pero di ko
alam paano ilagay yung "..." pag sobra sa 25 characters.
    2. Wala pa yung bonus points which is sorting the list "by
alphabetical" and "by price".

Yun lang yung kulang as far as I know. Paki-triple check nalang yung code ko thank you!!!
"""

shop = []
price = []
def main():
    print()
    while True: # This loop ensures that the program is always running until it's prompted to stop via [E]
        print("Menu: [A]dd  [R]emove  [U]pdate  [L]ist  [E]xit")
        menuInput = input("Option: ").upper()
        if menuInput == "A": # User adds a product on the list
            add_product()

        elif menuInput == "R": # User removes a product from the list
            remove_product()

        elif menuInput == "L": # User views the list of available products
            display_cart()

        elif menuInput == "U": # User updates the price of an existing product
            update_price()

        elif menuInput == "E": # Stops the program
            break

        else: # Prints an error if the user selects an invalid menu option
            print("*Invalid input.*", end="\n\n")



def add_product():
    prodName = input("Product: ").upper() # Prompts the user to add a product and Converts the input to uppercase
    if prodName in shop:
        print("*This product already exists.*", end="\n\n")
    else:
        shop.append(prodName) # Adds the inputted product to the list
    while True:
        try:
            price.append(float(input("Price (PhP): "))) # Prompts the user to assign a price
            print("*Successfully added the product.*", end="\n\n")
            break
        except ValueError: # Prints an error if the inputted price is NOT a number
            print("*Invalid input. Please enter a number.*", end="\n\n")
            continue

def remove_product():
    prodName = input("Product: ").upper()
    if prodName in shop: # Checks if the product exists in the product list
        priceIndex = shop.index(prodName) # Matches the product with its corresponding price
        price.pop(priceIndex) # Removes the price from the price list
        shop.remove(prodName) # Removes the product from the price list
        print("*Product removed successfully.*", end="\n\n")
    else: # Executes if the input is invalid
        print("*The product does not exist.*", end="\n\n")

def update_price():
    prodName = input("Product: ").upper()
    if prodName in shop: # Checks if the product exists in the product list
        priceIndex = shop.index(prodName) # Matches the product with its corresponding price
        price[priceIndex] = float(input("Price: ")) # Prompts the user to change the selected product's price
        print("*Price successfully changed.*", end="\n\n")
    else: # Executes if the input is invalid
        print("*The product does not exist.*", end="\n\n")

def display_cart():
    while True:
        print()
        print("Display product list: [D]efault  [A]lphabetically  [L]ow to High  [H]igh to Low")
        display_input = input("Option: ").upper()
        valid_input = ['D', 'A', 'L', 'H']
        if display_input not in valid_input:
            print("*Invalid Input.*", end="\n\n")
            continue

        if display_input == "D":
            print("{:25} {}".format("Product", "Price")) # Prints the labels for both lists
            for x, y in zip(shop, price):
                if len(x) > 25:
                    print("{:22}... {:.2f}".format(x[:22], y))
                else:
                    print("{:25} {:.2f}".format(x, y))
            break

        elif display_input == "A":
            sorted_shop = sorted(shop)
            shop_count = len(shop)
            sorted_price = []
            for product in sorted_shop:
                for i in range(shop_count):
                    if shop[i] == product:
                        sorted_price.append(price[i])

            print("{:25} {}".format("Product", "Price"))
            for x, y in zip(sorted_shop, sorted_price):
                if len(x) > 25:
                    print("{:22}... {:.2f}".format(x[:22], y))
                else:
                    print("{:25} {:.2f}".format(x, y))
            break

        elif display_input == "L":
            sorted_price = sorted(price)
            price_count = len(price)
            sorted_shop = []
            for p in sorted_price:
                for i in range(price_count):
                    if price[i] == p:
                        sorted_shop.append(shop[i])

            print("{:25} {}".format("Product", "Price"))
            for x, y in zip(sorted_shop, sorted_price):
                if len(x) > 25:
                    print("{:22}... {:.2f}".format(x[:22], y))
                else:
                    print("{:25} {:.2f}".format(x, y))
            break

        elif display_input == "H":
            sorted_price = sorted(price, reverse=True)
            price_count = len(price)
            sorted_shop = []
            for p in sorted_price:
                for i in range(price_count):
                    if price[i] == p:
                        sorted_shop.append(shop[i])

            print("{:25} {}".format("Product", "Price"))
            for x, y in zip(sorted_shop, sorted_price):
                if len(x) > 25:
                    print("{:22}... {:.2f}".format(x[:22], y))
                else:
                    print("{:25} {:.2f}".format(x, y))
            break




if __name__ == "__main__":
    main()
