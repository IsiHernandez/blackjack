import random



def shuffle():
    deck = []
    for i in range(1, 14):
        deck.append(i)
        deck.append(i)
        deck.append(i)
        deck.append(i)
        
    
        random.shuffle(deck)
    return deck

deck_of_cards = shuffle()


def dealer_cards():
    dealer_hand = []
    
    for i in range(1,3):
        dealer_hand.append(random.choice(deck_of_cards))
    print(f'The dealer has cards: X and {dealer_hand[1]}')
    return dealer_hand

d_hand = dealer_cards()


def player_cards():
    player_hand = []
    for i in range(1,3):
        player_hand.append(random.choice(deck_of_cards))
    print(f'You have cards: {player_hand[0]} and {player_hand[1]}')
    return player_hand

p_hand = player_cards()


def add_cards():
    if sum(d_hand) == 21:
        print("Dealer won :(")
    elif sum(d_hand) > 21:
        print('You won ;)')


while sum(p_hand) < 21:
    decision = str(input('hit or stay? '))
    if decision == 'hit':
        p_hand.append(random.choice(deck_of_cards))
        print(f'{p_hand} give you a total of {sum(p_hand)}')
    else:
        print(f'{d_hand} gives the dealer a total of {sum(d_hand)}')
        print(f'{p_hand} give you a total of {sum(p_hand)}')
        if sum(d_hand) > sum(p_hand):
            print('You lose, dealer wins.')
        else:
            print('you won!')

if sum(p_hand) > 21:
    print('You busted!')
elif sum(p_hand) == 21:
    print('BLACKJACK!')



# class Player:
#     pass

# class Dealer(Player):
#     pass

# class Game:
#     pass

# def main():

# main()