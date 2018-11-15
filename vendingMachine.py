
#define the program
def vendingMachine():

    #initial count is 0
    #initial totalCredit is 0

    count = 0
    totalCredit=0

    #variable coinsTotal
    #shows the total number of coins entered
    coinsTotal = int(input("Enter the total number of coins: "))
    while count in range(coinsTotal):
        coin = float(input("Enter the coin in Korean Won: "))
        totalCredit = totalCredit + coin
        count = count + 1


    print("You have entered {0} Korean Won".format(round(totalCredit, 2)))

    print(" ")
    print("Choose the type of coffee: ")
    print(" ")
    print("1. Americano")
    print("2. Cappuccino")
    print("3. Cafe Latte")
    print("4. Ristretto")
    print("5. Espresso")
    print("6. Cafe Mocha ")
    print(" ")

    #round off total amount to 2 decimal places
    finalCredit = totalCredit
    round(totalCredit, 2)

    coffeeType = int(input("Select the coffee type number: "))

    #if user select a number < 1 or > 5,
    #the vending machine will show that it is not available
    #the user will be given another option to choose the coffeeType

    while coffeeType < 1 or coffeeType > 6:
        print("The coffee type is not available")
        coffeeType = int(input("Select the coffee type number: "))
    if coffeeType == 1:

        #Americano costs 2,500 Korean Won
        finalCredit = totalCredit - 2,500
        print("Enjoy Americano at 2,500 Korean Won")
        print("You have {0} balance".format(round(finalCredit, 2)))

    elif coffeeType == 2:

        #Cappuccino costs 2,000 Korean Won
        finalCredit = totalCredit - 2,000
        print("Enjoy Cappuccino at 2,000 Korean Won")
        print("You have {0} balance".format(round(finalCredit, 2)))

    elif coffeeType == 3:

        #Cafe Latte costs 2,000 Korean Won
        finalCredit = totalCredit - 2,000
        print("Enjoy Cafe Latte at 2,000 Korean Won")
        print("You have {0} balance".format(round(finalCredit, 2)))

    elif coffeeType == 4:

        #Ristretto costs 1,800 Korean Won
        finalCredit = totalCredit - 1,800
        print("Enjoy Ristretto at 1,800 Korean Won")
        print("You have {0} balance".format(round(finalCredit, 2)))

    elif coffeeType == 5:

        #Espresso costs 2,000 Korean Won
        finalCredit = totalCredit - 2,000
        print("Enjoy Espresso at 2,000 Korean Won")
        print("You have {0} balance".format(round(finalCredit, 2)))

    elif coffeeType == 6:

        #Cafe Mocha costs 1,900 Korean Won
        finalCredit = totalCredit - 1,900
        print("Enjoy Cafe Mocha at 1,900 Korean Won")
        print("You have {0} balance".format(round(finalCredit, 2)))

    else:
        print("This is not an option")

    print(" ")
    print("The rest of the money {0} has been outputted".format(round(finalCredit, 2)))
    return 0

#call the function at the end

vendingMachine()













