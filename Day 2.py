total_bill = float(input('What was the total bill ? $'))
tip_percent = int(input(
    'What percent of tip would you like to give ? 10 , 12 , 15? '))
split_bet = int(input('How many people to split the bill ? '))
print(
    f'each person should pay: ${round((total_bill  / split_bet) * (1 + (tip_percent / 100)) , 2)}')
