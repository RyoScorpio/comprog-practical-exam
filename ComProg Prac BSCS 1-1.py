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

priceIndex = 1
prodPrice = 1
shop = []
price = []

print()
print("Menu: [A]dd  [R]emove  [U]pdate  [L]ist  [E]xit")

while True: # This loop ensures that the program is always running until it's prompted to stop via [E]
    userInput = input("Option: ")
    menuInput = userInput.upper() # Converts the input into uppercase
    if menuInput == "A": # User adds a product on the list
        while True:
            if prodPrice == 0: # Stops [A]dd command when cancelled from the price input
                prodPrice = 1
                break
            print()
            print("(Enter [E] to cancel.)")
            prodName = input("Product: ") # Prompts the user to add a product
            prodName = prodName.upper() # Converts the input to uppercase
            if prodName in shop: # Stops the user from adding the same product
                print("*This product already exists.*")
                print()
            elif prodName == "E": # Stops [A]dd command
                print("*Operation cancelled.*")
                print()
                break
            else:
                shop.append(prodName) # Adds the inputted product to the list
            while True:
                try:
                    print("(Enter [0] to cancel.)")
                    prodPrice = float(input("Price (PhP): ")) # Prompts user to input the price
                    if prodPrice == 0: # Stops [A]dd command
                        shop.remove(prodName)
                        print("*Operation cancelled.*")
                        print()
                        break
                    else:
                        price.append(prodPrice) # Prompts the user to assign a price
                        print("*Successfully added the product.*")
                        break
                except ValueError: # Prints an error if the inputted price is NOT a number
                    print("*Invalid input. Please enter a number.*")
                    print()
    elif menuInput == "R": # User removes a product from the list
        while True:
            print("(Enter [E] to cancel.)")
            prodName = input("Product: ")
            prodName = prodName.upper()
            if prodName in shop: # Checks if the product exists in the product list
                priceIndex = shop.index(prodName) # Matches the product with its corresponding price
                price.pop(priceIndex) # Removes the price from the price list
                shop.remove(prodName) # Removes the product from the price list
                print("*Product removed successfully.*")
                print()
            elif prodName == "E": # Stops [R] command
                print("*Operation cancelled.*")
                print()
                break
            else: # Executes if the input is invalid
                print("*The product does not exist.*")
                print()
    elif menuInput == "L": # User views the list of available products
        print()
        print("{:25} {}".format("Product", "Price")) # Prints the labels for both lists
        itemList = "\n".join("{:25} {:.2f}".format(x, y) for x, y in zip(shop, price))
        # ^^^ This line allows both lists to be printed side by side with proper formatting
        print(itemList)
        print()
    elif menuInput == "U": # User updates the price of an existing product
        while True:
            # if prodPrice == 0: # Stops [U]pdate command if cancelled from price input
                # prodPrice = 1
                # break
            print()
            print("(Enter [E] to cancel.)")
            prodName = input("Product: ")
            prodName = prodName.upper()
            if prodName in shop: # Checks if the product exists in the product list
                priceIndex = shop.index(prodName) # Matches the product with its corresponding price
                break
            elif prodName == "E": # Stops [U]pdate command
                print("*Operation cancelled.*")
                print()
                break
            else:  # Executes if the input is invalid
                print("*The product does not exist.*")
        while True:
            try:
                print("(Enter [0] to cancel.)")
                prodPrice = float(input("Price: ")) # Prompts the user to change the selected product's price
                if prodPrice == 0: # Stops [U]pdate command
                    print("*Operation cancelled.*")
                    print()
                    break
                else:
                    price[priceIndex] = prodPrice # Changes the selected product price
                    print("*Price successfully changed.*")
                    print()
                    break
            except ValueError: # Prints an error if the inputted price is NOT a number
                print("*Invalid input. Please enter a number.*")
                print()
    elif menuInput == "E": # Stops the program
        print("*Program successfully stopped.*")
        break
    else: # Prints an error if the user selects an invalid menu option
        print("*Invalid input.*")
        print()

