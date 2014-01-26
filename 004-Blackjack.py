# http://www.codeskulptor.org/#user25_d4TjoJQVmMhEEDz.py

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = list()

    def __str__(self):
        return "Hand contains " + " ".join([str(i) for i in self.cards])
    
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0
        for i in self.cards:
            if i.get_rank() == 'A':
                aces += 1
            value += VALUES.get(i.get_rank())
        if aces > 0 and (value + 10) <= 21:
            value += 10
        return value
    
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] = pos[0] + 20
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = list()
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
        
    def __str__(self):
        return "Deck contains " + " ".join([str(i) for i in self.deck])
    

#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player, score, deck
    deck = Deck()
    deck.shuffle()
    dealer = Hand()
    player = Hand()
    for i in range(2):
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())  
    
    dealer.cards[-1].show = False    
    outcome = "Hit or Stand?"    
    in_play = True
    
def hit():
    global outcome, in_play, score
    if not in_play:
        return
    player.add_card(deck.deal_card())
    outcome = "Hit or Stand?"
    if player.get_value() > 21:
        outcome = "You have busted. Deal again?"
        in_play = False
        score -= 1 
    
def stand():
    global outcome, in_play, score
    if not in_play:
        return
    while dealer.get_value() < 17:
        dealer.add_card(deck.deal_card())
    if dealer.get_value() > 21:
        score += 1
        outcome = "The dealer has busted!"
    elif player.get_value() > dealer.get_value():
        score += 1
        outcome = "You win!"
    else:
        score -= 1
        outcome = "You have lost. Deal again?"
    in_play = False
    
# draw handler    
def draw(canvas):    
    canvas.draw_text("BlackJack", [200, 50], 35, "Black")
    canvas.draw_text("Score: "+ str(score), [200, 250], 20, "Black")
    canvas.draw_text(outcome, [200, 275] , 20, "Black")
    dealer.draw(canvas, [200, 100])    
    player.draw(canvas, [200, 300])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [220 + CARD_BACK_CENTER[0], 100 + CARD_BACK_CENTER[1]], CARD_SIZE)    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the grading rubric