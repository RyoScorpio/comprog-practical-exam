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

print()
print("Menu: [A]dd  [R]emove  [U]pdate  [L]ist  [E]xit")

while True: # This loop ensures that the program is always running until it's prompted to stop via [E]
    menuInput = str(input("Option: "))
    if menuInput == "A": # User adds a product on the list
        prodName = input("Product: ") # Prompts the user to add a product
        prodName = prodName.upper() # Converts the input to uppercase
        if prodName in shop:
            print("*This product already exists.*")
            print()
        else:
            shop.append(prodName) # Adds the inputted product to the list
        while True:
            try:
                price.append(float(input("Price (PhP): "))) # Prompts the user to assign a price
                print("*Successfully added the product.*")
                print()
                break
            except ValueError: # Prints an error if the inputted price is NOT a number
                print("*Invalid input. Please enter a number.*")
                print()
                continue
    elif menuInput == "R": # User removes a product from the list
        prodName = input("Product: ")
        prodName = prodName.upper()
        if prodName in shop: # Checks if the product exists in the product list
            priceIndex = shop.index(prodName) # Matches the product with its corresponding price
            price.pop(priceIndex) # Removes the price from the price list
            shop.remove(prodName) # Removes the product from the price list
            print("*Product removed successfully.*")
            print()
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
        prodName = input("Product: ")
        prodName = prodName.upper()
        if prodName in shop: # Checks if the product exists in the product list
            priceIndex = shop.index(prodName) # Matches the product with its corresponding price
            while True:
                try:
                    price[priceIndex] = float(input("Price: ")) # Prompts the user to change the selected product's price
                    print("*Price successfully changed.*")
                    print()
                    break
                except ValueError: # Prints an error if the inputted price is NOT a number
                    print("*Invalid input. Please enter a number.*")
                    print()
                    continue
        else: # Executes if the input is invalid
            print("*The product does not exist.*")
            print()
    elif menuInput == "E": # Stops the program
        break
    else: # Prints an error if the user selects an invalid menu option
        print("*Invalid input.*")
        print()

