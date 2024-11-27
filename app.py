totalPrice = 0
selected_items = []
totalItems = 0
def menu():
    global totalPrice, selected_items
    print("1: Browse store")
    print("2: Purchase an Item")
    print("3: Check Out")
    menuSelection = input()
    if menuSelection == "1":
        print("""
        1 - Playstation 4                  $499
        2 - Xbox One                       $399
        3 - Nintendo Switch                $449
        4 - Dualshock 4 Wireless Controller $89
        5 - Xbox One Wireless Controller    $89
        6 - Joycon Controller               $69
        7 - FIFA 19                         $99
        8 - Madden 19                       $99
        9 - NBA 2K19                        $99
        10 - Horizon Zero Dawn              $49
        11 - Sea of Thieves                 $99
        12 - No Man’s Sky                   $49
        13 - Breath of the Wild             $89
        14 - Super Mario Odyssey            $79
        15 - Mario Tennis Aces              $79
        """)
        menu()
    elif menuSelection == "2":
        global totalItems
        itemPrice = 0
        if totalItems < 3:
            itemNumber = int(input("What item would you like to purchase? "))
            if itemNumber == 1:
                selected_items.append("Playstation 4")
                itemPrice = 499
            elif itemNumber == 2:
                selected_items.append("Xbox One")
                itemPrice = 399
            elif itemNumber == 3:
                selected_items.append("Nintendo Switch")
                itemPrice = 449
            elif itemNumber == 4:
                selected_items.append("Dualshock 4 Wireless Controller")
                itemPrice = 89
            elif itemNumber == 5:
                selected_items.append("Xbox One Wireless Controller")
                itemPrice = 89
            elif itemNumber == 6:
                selected_items.append("Joycon Controller")
                itemPrice = 69
            elif itemNumber == 7:
                selected_items.append("FIFA 19")
                itemPrice = 99
            elif itemNumber == 8:
                selected_items.append("Madden 19")
                itemPrice = 99
            elif itemNumber == 9:
                selected_items.append("NBA 2K19")
                itemPrice = 99
            elif itemNumber == 10:
                selected_items.append("Horizon Zero Dawn")
                itemPrice = 49
            elif itemNumber == 11:
                selected_items.append("Sea of Thieves")
                itemPrice = 99
            elif itemNumber == 12:
                selected_items.append("No Man’s Sky")
                itemPrice = 49
            elif itemNumber == 13:
                selected_items.append("Breath of the Wild")
                itemPrice = 89
            elif itemNumber == 14:
                selected_items.append("Super Mario Odyssey")
                itemPrice = 79
            elif itemNumber == 15:
                selected_items.append("Mario Tennis Aces")
                itemPrice = 79
            else:
                print("Invalid item number")
                menu()
            totalItems = totalItems + 1   
            totalPrice = totalPrice + itemPrice
            menu()
        else:
            print("You can not purchase any more items at the moment. You will now be taken to the checkout")
            checkout()
    elif menuSelection == "3":
        checkout()
    else:
        print('Unknown selection.')
        menu()

def checkout():
    global totalPrice, selected_items
    print(f"You have {selected_items} in your cart")
    print("Your total is $" + str(totalPrice) + " before tax and discounts")
    discount = totalPrice * 0.4
    print("You saved $" + str(discount) + " thanks to our sale")
    beforeTaxTotal = totalPrice - discount
    print("Your new total before tax is $" + str(beforeTaxTotal))
    tax = beforeTaxTotal * 0.11
    print("GST: $" +str(tax))
    finalTotal = beforeTaxTotal + tax
    print("Amount owed: $" + str(finalTotal))
    paymentMethod = input("""
                          How would you like to pay
                          1: Cash
                          2: Card
                          """)
    if paymentMethod == "1":
        paid = 0
        while paid < finalTotal:
            cashAmount = float(input("How much cash have you paid? $"))
            paid = paid + cashAmount
            if paid < finalTotal:
                remaining = finalTotal - paid
                print("You still owe $" + str(remaining))
            elif paid > finalTotal:
                    change = paid - finalTotal
                    print("You are owed $" + str(change) + " change")
                    return
            elif paid == finalTotal:
                return
    if paymentMethod == "2":
        print("Please tap, swipe or insert your card")
        return

menu()

print("thank you for your purchase")