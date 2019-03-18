from random import shuffle


def war():
    cards = []
    for _ in range(4):
        for i in range(2, 15):
            cards.append(i)
    shuffle(cards)
    player = cards[:26]
    computer = cards[26:]
    player_pile = []
    computer_pile = []
    table_cards = []
    count = 0
    while len(player) > 0 and len(computer) > 0:
        count += 1
        print(count)
        print(player_pile)
        player_card = player.pop()
        computer_card = computer.pop()
        table_cards.append(computer_card)
        if player_card > computer_card:
            print('player beats computer {} to {}'.format(
                player_card, computer_card))
            # player_pile.append(player_card)
            # player_pile.append(computer_card)
            player_pile.extend(table_cards.copy())
            table_cards.clear()
        elif player_card < computer_card:
            print('computer beats player {} to {}'.format(
                computer_card, player_card))
            # computer_pile.append(player_card)
            # computer_pile.append(computer_card)
            computer_pile.extend(table_cards.copy())
            table_cards.clear()
        else:
            for _ in range(3):
                if len(player) == 0:
                    shuffle(player_pile)
                    player.extend(player_pile[:])
                    player_pile = []
                if len(computer) == 0:
                    shuffle(computer_pile)
                    computer.extend(computer_pile[:])
                    computer_pile = []
                if len(player) == 0 or len(computer) == 0:
                    break
                table_cards.append(player.pop())
                table_cards.append(computer.pop())
                # table_cards.append(player.pop())
                # table_cards.append(computer.pop())
            # table_cards.append(player.pop())
            # table_cards.append(player.pop())
            # table_cards.append(player.pop())
            # table_cards.append(computer.pop())
            # table_cards.append(computer.pop())
            # table_cards.append(computer.pop())

        if len(player) == 0:
            shuffle(player_pile)
            player.extend(player_pile[:])
            player_pile = []
        if len(computer) == 0:
            shuffle(computer_pile)
            computer.extend(computer_pile[:])
            comperter_pile = []


def main():
    war()


if __name__ == '__main__':
    main()
