import random as rn
import Arts as art


def intial_cards(cards):
    global player, computer, total_player
    player = rn.sample(cards.keys(), 2)
    computer = rn.sample(cards.keys(), 2)
    total_player = 0
    for i in player:
        total_player += cards[i]
    return f"Your cards : {player} , current score {total_player} \nComputer's first card: {computer[0]}"


def second_card(cards):
    global final_score
    final_card = rn.sample(cards.keys(), 1)
    for i in final_card:
        player.append(i)
        final_score = total_player + cards[i]
    return f"\n\nYour cards : {player} , your final score {final_score} \nComputer's first card: {computer[0]}"


def results(cards):
    computer_score = 0
    for i in computer:
        computer_score += cards[i]
    while computer_score <= 16:
        computer_card = rn.sample(cards.keys(), 1)
        for i in computer_card:
            computer.append(i)
            computer_score += cards[i]
    won = winner(computer_score, final_score)
    return (f"\nComputer's final hand: {computer} , computer final score: {computer_score}\n\n{won}")


def show_hand(cards):
    computer_score = 0
    for i in computer:
        computer_score += cards[i]
    while computer_score <= 16:
        computer_card = rn.sample(cards.keys(), 1)
        for i in computer_card:
            computer.append(i)
            computer_score += cards[i]
    won = winner(computer_score, total_player)
    return (f"\n\nYour cards : {player[:2]} , your final score {total_player} \nComputer's final hand: {computer} , computer final score: {computer_score} \n\n{won}")


def winner(c_score, p_score):
    if p_score == c_score and c_score == 21:
        return f"Looks like the dealer got Black Jack \n {art.lose}"
    elif p_score == c_score and c_score == 21:
        return f"It's Draw .... Better luck next time \n {art.draw}"
    elif p_score > 21:
        p_score -= 10
        return f"You went over 21. You lose 😭 \n {art.lose}"
    elif p_score < c_score:
        return f"You lose ....Wrong Choice it seems .... \n {art.lose}"
    else:
        return f"Congrats you have the bet..... \n {art.win}"
