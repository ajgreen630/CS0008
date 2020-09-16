import card_class
import random

def main():

    name = input("Name? ")
    bal = 1000

    print(name + " has $" + str(bal))

    bet = input("Bet? (0 to quit, Enter to stay at $25) ")

    print()
        
    if bet == "0":
        quit()
    elif bet == "":
        bet = 25
    else:
        bet = int(bet)

    while bet > bal:
        print("Error: Cannot place bet higher than balance.")
        bet = input("Bet? 0 to quit, Enter to stay at $25) ")

    while bet != "0" and bal > 0:
        deck = card_class.Deck()

        dealer_hand = []
        player_hand = []

        # Append 1 card to dealer_hand, and 2 cards to
        # player_hand.
        dealer_hand.append(deck.get_card())
        player_hand.append(deck.get_card())
        player_hand.append(deck.get_card())

        print("Bet: $" + str(bet))
        print("Dealer's hand:", end=" ")
        show_hand(dealer_hand)
        dealer_score = total(dealer_hand) # Updates dealer score.
        print("Value:", dealer_score)

        print(name + "'s hand:", end=" ")
        show_hand(player_hand)
        player_score = total(player_hand) # Updates player score.
        print("Value:", player_score)
        print()

        if player_score == 21: # In case player hits 21
            print(name + " wins") # in the first round.
            bal += bet
            print()
            
        elif player_score != 21:                # Player wouldn't
            move = input("Move? (hit/stay) ")   # exceed 21 first round.
            print()

            while player_score < 21 and move == "h":
                # Append another card to player_hand
                # if user chooses to hit.
                player_hand.append(deck.get_card())

                print("Bet: $" + str(bet))
                print("Dealer's hand:", end=" ")
                show_hand(dealer_hand)
                dealer_score = total(dealer_hand) # Updates dealer score.
                print("Value:", dealer_score)

                print(name + "'s hand:", end=" ")
                show_hand(player_hand)
                player_score = total(player_hand) # Updates player score.
                print("Value:", player_score)
                print()

                # Check if certain conditions were met to
                # have an affect or to let user hit or stay
                # again.
                if player_score < 21:
                    move = input("Move? (hit/stay) ")
                    print()
                elif player_score > 21:
                    print("Player bust")
                    bal -= bet
                    print()
                elif player_score == 21:
                    print(name + " wins")
                    print()
                    
            # check if the dealer needs to go (player score < 21 is good enough)
            if player_score < 21:
                # If the player chooses to stay and has
                # not won or busted, the dealer may play.
                while dealer_score < 21:
                    # Dealer draws cards while his score
                    # is low enough.
                    dealer_hand.append(deck.get_card())

                    print("Bet: $" + str(bet))
                    print("Dealer's hand:", end=" ")
                    show_hand(dealer_hand)
                    dealer_score = total(dealer_hand) # Updates dealer score.
                    print("Value:", dealer_score)

                    print(name + "'s hand:", end=" ")
                    show_hand(player_hand)
                    player_score = total(player_hand) # Updates player score.
                    print("Value:", player_score)
                    print()

                    # Check if conditions were met for dealer
                    # to win or bust.
                    if dealer_score > 21:
                        print("Dealer bust")
                        bal += bet
                        print()
                    elif dealer_score == 21:
                        print("Dealer wins")
                        bal -= bet
                        print()
                            
        # Player's new balance after the round.
        print(name + " has $" + str(bal))
        print()
        # Auto-bet has now been set to 100.
        bet = input("Bet? (0 to quit, Enter to stay at $100) ")
        print()
        
        if bet == "0":
            quit()
        elif bet == "":
            bet = 100
        else:
            bet = int(bet)

        while bet > bal:
            print("Error: Cannot place bet higher than balance.")
            bet = input("Bet? 0 to quit, Enter to stay at $100) ")        

def show_hand(hand):
    for c in hand:
        print(c, end=" ")
    print()

def total(hand):
    total = 0

    for c in hand:
        if c.get_value() != "Ace":
            total += c.get_value()
    for c in hand:
        if c.get_value == "Ace":
            if total < 10:
                total += 11
            else:
                total += 1

    return total

# Call the main function.
main()
