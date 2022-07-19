import data


def report(profit):
    for i in data.resources:
        print(f"{i}: {data.resources[i]}ml")
    print(f"Money: ${profit}")


def price(amount, item):
    if amount > data.MENU[item]["cost"]:
        left = amount - data.MENU[item]["cost"]
        return True, left, data.MENU[item]["cost"]
    return False, amount, 0


def coffee_items(item):
    for i in data.MENU[item]["ingredients"]:
        if data.resources[i] > data.MENU[item]["ingredients"][i]:
            data.resources[i] = data.resources[i] - data.MENU[item]["ingredients"][i]
        else:
            return False, data.resources[i]
    return True, ""


def make_coffee(coffee, money_in):
    if coffee in data.MENU:
        available_price = price(money_in, coffee)
        available_resource = coffee_items(coffee)
        if available_price[0]:
            if not available_resource[0]:
                return print(f"Sorry there is not enough {available_resource[1]}."), available_price[2]
            return f"Here is ${round(available_price[1],2)} in change\nHere is your {coffee} Enjoy...", available_price[2]
        return f"Sorry that's not enough money. \nMoney refunded{available_price[1]} ", available_price[2]
    return f"Sorry {coffee} is not available in our store", 0
