import random


class Card:
    def __init__(self, type, color=None):
        self.type = type
        self.color = color

    def __str__(self):
        return "Type: " + self.type + ", Color: " + self.color


class NumberCard(Card):
    def __init__(self, type, color, number):
        super().__init__(type, color)

        self.number = number

    def __str__(self):
        return "Type: " + self.type + ", Color: " + self.color + ", Number: " + str(self.number)


class Deck:
    def __init__(self, cards=None):
        self.cards = []
        if isinstance(cards, list):
            self.cards = cards
        else:
            self.cards = self.new()
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, amount):
        cards = []
        for i in range(amount):
            randomIndex = random.randint(1, len(self.cards))
            cards.append(self.cards[randomIndex])
            self.cards.pop(randomIndex)
        return cards

    def display(self):
        print("\n-------------- Your Deck ------------------")
        for i, card in enumerate(self.cards):
            print('Index: ' + str(i) + " " + str(card))

    def __append__(self, card):
        self.cards.append(card)

    def __remove__(self, card):
        self.cards.remove(card)

    def new(self):
        types = ["number", "skip",
                 "drawTwo", "wildDrawFour", "wild"]  # "reverse", "blank",
        colors = ["red", "green", "blue", "yellow"]
        cards = []

        for type in types:
            if type == "number":
                for color in colors:
                    for number in range(1, 9):
                        cards.append(NumberCard(type, color, number))
            if type == "skip":
                for color in colors:
                    for number in range(1, 2):
                        cards.append(Card(type, color))
            if type == "reverse":
                for color in colors:
                    for number in range(1, 2):
                        cards.append(Card(type, color))
            if type == "drawTwo":
                for color in colors:
                    for number in range(1, 2):
                        cards.append(Card(type, color))
            if type == "wild":
                for number in range(1, 4):
                    cards.append(Card(type, "none"))
            if type == "wildDrawFour":
                for number in range(1, 4):
                    cards.append(Card(type, "none"))
            if type == "blank":
                for number in range(1, 4):
                    cards.append(Card(type, "blank"))

        return cards

    def __str__(self):
        return "Deck Type " + str(len(self.cards))

    def checkWinStatus(self, playerCards, playerCardIndex, topOfDeckCard):
        if playerCards[playerCardIndex].type == "skip":
            print("The card is a skip, skip the turn")
            self.cards.insert(0, playerCards[playerCardIndex])
            del playerCards[playerCardIndex]
            return playerCards
        elif topOfDeckCard.type == "drawTwo":
            print("Added 2 cards to the deck")
            newCards = self.draw(2)
            for card in newCards:
                playerCards.insert(0, card)
            return playerCards
        elif hasattr(playerCards[playerCardIndex], "number") and hasattr(topOfDeckCard, "number") and playerCards[playerCardIndex].number == topOfDeckCard.number:
            print("Cards are the same number, match")
            self.cards.insert(0, playerCards[playerCardIndex])
            del playerCards[playerCardIndex]
            return playerCards

        elif hasattr(playerCards[playerCardIndex], "color") and hasattr(topOfDeckCard, "color") and playerCards[playerCardIndex].color == topOfDeckCard.color:
            print("Cards are the same color, match")
            self.cards.insert(0, playerCards[playerCardIndex])
            del playerCards[playerCardIndex]
            return playerCards

        elif topOfDeckCard.type == "wildDrawFour":
            print("Added 4 cards to the deck")
            newCards = self.draw(4)
            for card in newCards:
                playerCards.append(card)
            tempCard = self.cards.pop(0)
            self.cards.append(tempCard)
            return playerCards

        elif playerCards[playerCardIndex].type == "wildDrawFour":
            print("WildDrawFour added to the heap!")
            self.cards.insert(0, playerCards[playerCardIndex])
            del playerCards[playerCardIndex]
            return playerCards

        elif topOfDeckCard.type == "wild" or playerCards[playerCardIndex].type == "wild":
            print("It's a wild, it works on anything!")
            self.cards.insert(0, playerCards[playerCardIndex])
            del playerCards[playerCardIndex]
            return playerCards

        elif len(playerCards) == 0:
            print("You are a winner !!!!!")

        else:
            card = self.draw(1)
            playerCards.append(card[0])
            return playerCards


def enterPlayers():
    playerAmount = int(input("How many players? "))
    return playerAmount


def determinePlayerTurn(currentPlayer, playerAmount):
    if currentPlayer == playerAmount:
        return 1
    else:
        return currentPlayer + 1


def main():
    playerAmount = enterPlayers()
    currentPlayer = 1

    if playerAmount > 1 and playerAmount <= 10:
        print("Lets get started")
        uno = Deck()
        playerDecks = {}

        for i in range(playerAmount):
            # assign each player a deck
            deck = Deck(uno.draw(7))
            playerDecks[i + 1] = deck

        for i, deck in enumerate(playerDecks):

            print("player" + str(i) + " deck: ")
            playerDecks[deck].display()

        for card in uno.cards:

            topCard = uno.cards[0]
            print("\n---------------------------------------\n")
            print("Card at the top of the deck is: " + str(topCard))
            print("Player" + str(currentPlayer) + " it is your turn")

            playerDecks[currentPlayer].display()
            selectedCardIndex = int(
                input("Enter the index of the card would you like to play? "))

            if selectedCardIndex <= len(playerDecks[currentPlayer].cards):
                playerDecks[currentPlayer].cards = uno.checkWinStatus(
                    playerDecks[currentPlayer].cards, selectedCardIndex, topCard)

            playerDecks[currentPlayer].display()
            currentPlayer = determinePlayerTurn(currentPlayer, playerAmount)
    else:
        print("Invalid amount of players")

    # player1Deck = Deck(uno.draw(7))
    # player1Cards = player1Deck.cards

    # # card game
    # for card in uno.cards:

    #     for playerCard in player1Cards:
    #         topCard = uno.cards[0]

    #         print("\n---------------------------------------")
    #         print("Card at the top of the deck is: \n" + str(topCard))

    #         player1Deck.display()
    #         print("Which card to throw")
    #         cardIndex = int(
    #             input("Enter the index of the card you want to throw: "))

    #         if cardIndex <= len(player1Cards):
    #             player1Deck.cards = uno.checkWinStatus(
    #                 player1Cards, cardIndex, topCard)
    #             uno.display()


main()
