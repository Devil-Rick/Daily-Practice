import replit
import coffee_maker as cm

serving = True
profit = 0
while serving:
    replit.clear()
    money = 0
    user = input("What would you like to drink \n(espresso / latte / cappuccino) ?").lower()
    if user == "report":
        cm.report(profit)
        continue
    if user == "off":
        break
    print("Please insert coins")
    money += int(input("How many quarters : ")) * 0.25
    money += int(input("How many dines : ")) * 0.10
    money += int(input("How many nickels : ")) * 0.05
    money += int(input("How many pennies : ")) * 0.01
    prepare = cm.make_coffee(user, money)
    print(prepare[0])
    profit += prepare[1]
    another = input("\nDo you want another serving\nType 'yes' or 'no': ").lower()
    print()
    if another == 'no':
        serving = False
