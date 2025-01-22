'''
ComProg 1 Practical Exam #2
BSCS 1-1

Main Contributions:
	Belandres: Overall code structure, menu functionality, first version of the code, program comments
	Metillo: Rewrote code using custom functions, improving code for [L]ist command, sorting the list alphabetically and by price
	Vertudazo: Truncating product names longer than 25 characters
	Casabal: Additional advice regarding the code
'''


shop = []
price = []
print("Menu: [A]dd  [R]emove  [U]pdate  [L]ist  [E]xit")

def main(): # Called at the end of every command so the program continues to run
    print()
    while True: 
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
    prodName = input("Product: ").upper().strip() # Prompts the user to add a product and Converts the input to uppercase
    if prodName in shop:
        print("*This product already exists.*", end="\n")
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

def display_cart(): # Lists the product currently available
    while True:
        print()
        print("Display product list: [D]efault  [A]lphabetically  [L]ow to High  [H]igh to Low")
        display_input = input("Option: ").upper() # Prompts the user to choose how to sort the list
        valid_input = ['D', 'A', 'L', 'H']
        if display_input not in valid_input: # Prints an error if input is invalid
            print("*Invalid Input.*", end="\n")
            continue

        # Sort by Default 
        if display_input == "D":
            print()
            print("{:25} {}".format("Product", "Price")) # Prints the labels for both lists
            for x, y in zip(shop, price):
                if len(x) > 25: # Checks if the product name is longer than 25 characters
                    print("{:22}... {:.2f}".format(x[:22], y))
                else:
                    print("{:25} {:.2f}".format(x, y))
            print()
            break

        # Sort Alphabetically
        elif display_input == "A":
            sorted_shop = sorted(shop) # Sorts the product list alphabetically
            shop_count = len(shop) 
            sorted_price = []
            for product in sorted_shop: # Sorts the price list according to its matching product
                for i in range(shop_count):
                    if shop[i] == product:
                        sorted_price.append(price[i])

            print()
            print("{:25} {}".format("Product", "Price"))
            for x, y in zip(sorted_shop, sorted_price): # Prints the updated lists
                if len(x) > 25: # Checks if the product name is longer than 25 characters
                    print("{:22}... {:.2f}".format(x[:22], y))
                else:
                    print("{:25} {:.2f}".format(x, y))
            print()
            break

        # Sort Price by Lowest to Highest
        elif display_input == "L":
            sorted_price = sorted(price) # Sorts the price list from lowest to highest
            price_count = len(price)
            sorted_shop = []
            for p in sorted_price: # Sorts the product list according to its matching price
                for i in range(price_count):
                    if price[i] == p:
                        sorted_shop.append(shop[i])

            print()
            print("{:25} {}".format("Product", "Price"))
            for x, y in zip(sorted_shop, sorted_price): # Prints the updated lists
                if len(x) > 25: # Checks if the product name is longer than 25 characters
                    print("{:22}... {:.2f}".format(x[:22], y))
                else:
                    print("{:25} {:.2f}".format(x, y))
            print()
            break

        # Sort Price by Highest to Lowest
        elif display_input == "H":
            sorted_price = sorted(price, reverse=True)
            # Sorts the price list from highest to lowest
            price_count = len(price)
            sorted_shop = []
            for p in sorted_price: # Sorts the product list according to its matching price
                for i in range(price_count):
                    if price[i] == p:
                        sorted_shop.append(shop[i])

            print()
            print("{:25} {}".format("Product", "Price"))
            for x, y in zip(sorted_shop, sorted_price): # Prints the updated lists
                if len(x) > 25: # Checks if the product name is longer than 25 characters
                    print("{:22}... {:.2f}".format(x[:22], y))
                else:
                    print("{:25} {:.2f}".format(x, y))
            print()
            break




if __name__ == "__main__":
    main()
