'''
Simple Text based BlackJack game
'''

import random


class Account():
    '''
    This is the bank account of the player, player can deposit and withdraw case
    '''

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        '''
        This is used to withdraw case from account
        '''
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Sorry sir, Your account does not have sufficient balance to withdraw")
            return False

    def deposit(self, amount):
        '''
        This is used to deposit case in account
        '''
        self.balance += amount

    def __str__(self):
        '''
        This represent the length of account in terms of balance in account
        '''
        return f"The account have ${self.balance} balance"


def random_card():
    '''
    :return: It returns a random card from the deck of 52 cards
    '''

    special_cards_list = ['JACK', 'QUEEN', 'KING', 'ACE']
    special_card = random.choice(special_cards_list)
    card_with_numbers = random.randint(2, 10)
    final_card_list = [special_card, card_with_numbers]
    final_card = random.choice(final_card_list)

    return final_card


def show_cards(card_list, card1_list):
    print("\n"*100)
    print("Player Cards:")
    for cards in card_list:
        print(f"{cards}\n")
    print("Computer Cards:")
    for cards in card1_list:
        print(f"{cards}\n")


def cards_sum(temp_list, temp1_list):
    for i in range(len(temp_list)):
        if temp_list[i] == "JACK" or temp_list[i] == 'QUEEN' or temp_list[i] == 'KING':
            temp_list[i] = 10
            continue
        elif temp_list[i] == 'ACE':
            ace = int(input("Please choose number for ACE (1/11): "))
            temp_list[i] = ace
            continue
    for i in range(len(temp1_list)):
        if temp1_list[i] == "JACK" or temp1_list[i] == 'QUEEN' or temp1_list[i] == 'KING':
            temp1_list[i] = 10
            continue
        elif temp1_list[i] == 'ACE':
            temp1_list[i] = 0
            if sum(temp_list) > sum(temp1_list) and sum(temp1_list) < 21:
                ace = 11
            elif sum(temp_list) < sum(temp1_list) and sum(temp1_list) < 21:
                ace = 1
            temp1_list[i] = ace
            continue


if __name__ == '__main__':
    print("WELCOME IN BLACKJACK GAME MADE BY KD SINGH")
    print("-------------------------------------------\n\n")
    print("-------------------------------------------")
    amount = int(input("Please deposit cash into your game account: "))
    account = Account(0)
    account.deposit(amount)

    while True:
        print(account)
        bet = int(input("Please enter your bet: "))
        if account.withdraw(bet) and bet != 0:
            player_cards_list = [random_card()]
            player_cards_list.append(random_card())
            computer_cards_list = [random_card()]
            count1 = 2
            count2 = 1
            while True:
                show_cards(player_cards_list, computer_cards_list)
                temp_list = player_cards_list
                temp1_list = computer_cards_list
                if True:
                    player_choice = int(input("Please enter 1 for 'HIT' or 2 for 'STAND'"))
                    if player_choice == 1:
                        count1 += 1
                        player_cards_list.append(random_card())
                    elif player_choice == 2:
                        count2 += 1
                        computer_cards_list.append(random_card())
                        temp_list = player_cards_list
                        temp1_list = computer_cards_list
                        cards_sum(temp_list, temp1_list)
                        while True:
                            temp_list = player_cards_list
                            temp1_list = computer_cards_list
                            cards_sum(temp_list, temp1_list)
                            if sum(temp_list) > sum(temp1_list) and sum(temp1_list) < 21 and sum(temp1_list):
                                count2 += 1
                                computer_cards_list.append(random_card())
                                continue
                            elif sum(temp_list) < sum(temp1_list) and sum(temp1_list) < 21:
                                break
                            elif sum(temp1_list) == 21 or sum(temp_list) == sum(temp1_list) or sum(temp_list):
                                break
                            else:
                                break
                temp_list = player_cards_list
                temp1_list = computer_cards_list
                cards_sum(temp_list, temp1_list)
                if sum(temp_list) > 21:
                    show_cards(player_cards_list, computer_cards_list)
                    print("The player is burst and player lose the game!")
                    break
                elif sum(temp_list) == 21 and count1 == 2:
                    show_cards(player_cards_list, computer_cards_list)
                    print("BLACKJACK! Player wins")
                    win_case = bet+(1.5*bet)
                    account.deposit(win_case)
                    break
                elif sum(temp1_list) > 21:
                    show_cards(player_cards_list, computer_cards_list)
                    print("The computer is burst and player win the game!")
                    account.deposit(2*bet)
                    break
                elif sum(temp1_list) == 21 and count2 == 2:
                    show_cards(player_cards_list, computer_cards_list)
                    print("BLACKJACK! computer wins")
                    break
                if player_choice == 2:
                    if sum(temp_list) < sum(temp1_list):
                        show_cards(player_cards_list, computer_cards_list)
                        print('Computer wins the game')
                        break
                    elif sum(temp1_list) < sum(temp_list):
                        show_cards(player_cards_list, computer_cards_list)
                        print("Player wins the game")
                        account.deposit(2*bet)
                        break
                    elif sum(temp_list) == sum(temp1_list):
                        show_cards(player_cards_list, computer_cards_list)
                        print("The game is draw!")
                        account.deposit(bet)
                        break

        replay = input("Do yo want to play again (y/n): ")
        if replay == 'y':
            continue
        elif replay == 'n':
            break