import random as r

# ace == 1
# jack == 11
# queen == 12
# king == 13
# joker == 99


deck_len = 52
max_cards = 13
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
special_cards = {
    1: "Ace",
    11: "Jack",
    12: "Queen",
    13: "King",
    14: "Joker"
}


class Deck:
    def __init__(self):
        self.cards = []
        self.compose()

    def compose(self):
        for suit in suits:
            for value in range(1, max_cards+1):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        r.shuffle(self.cards)

    def remaining(self):
        return len(self.cards)

    def deal(self):
        try:
            return self.cards.pop()
        except:
            print("No more cards are left in deck.")


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.suit == other.suit and self.value == other.value

    def suit(self):
        return self.suit

    def value(self):
        return self.value

    def suitAsString(self):
        return self.suit

    def valueAsString(self):
        if self.value in special_cards:
            return special_cards[self.value]
        else:
            return str(self.value)

    def toString(self):
        return self.valueAsString() + " of " + self.suitAsString()


class Hand:
    def __init__(self):
        self.hand = []

    def __repr__(self):
        return str(self.hand)

    def __eq__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        return self.hand == other.hand

    def addCard(self, Card):
        self.hand.append(Card)

    def removeCard(self, Card):
        self.hand.remove(Card)

    def sortBySuit(self):
        pass

    def sortByValue(self):
        pass

