import replit
import coffee_maker as cm

serving = True
profit = 0
while serving:
    replit.clear()
    user = input("What would you like to drink \n(espresso / latte / cappuccino) ?").lower()
    if user == "report":
        cm.report(profit)
        continue
    if user == "off":
        break
    print("Please insert coins")
    quarters = int(input("How many quarters : "))
    dines = int(input("How many dines : "))
    nickels = int(input("How many nickels : "))
    pennies = int(input("How many pennies : "))
    prepare = cm.make_coffee(user, quarters, dines, nickels, pennies)
    print(prepare[0])
    profit += prepare[1]
    another = input("\nDo you want another serving\nType 'yes' or 'no': ").lower()
    print()
    if another == 'no':
        serving = False
