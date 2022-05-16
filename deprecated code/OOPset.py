"""
Object Oriented approach at creating the SET game
-------------------------------------------------
This script runs one game of the original game,
and returns all the sets it has found.
-------------------------------------------------
Author: J.D. Hamelink
Date: May 2022
"""

import random
from itertools import product, combinations

class Card:
    def __init__(self, number: int, color: str, shape: str, filling: str):
        self.number = number
        self.color = color
        self.shape = shape
        self.filling = filling
    
    def __repr__(self):
        return f'{self.number}{self.color}{self.shape}{self.filling}'

class Deck:    
    def __init__(self):
        self.pile = set(Card(c[0],c[1],c[2],c[3]) for c in product(*[[1,2,3], ['b','r','g'], ['s','o','w'], ['e','h','f']]))
    
    def __call__(self) -> set[Card]:
        card = random.sample(self.pile, 1)[0]
        self.pile.remove(card)
        return card
    
    def is_empty(self) -> bool:
        return not len(self.pile)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.table = set()
        self.game_loop()
        
    def find_sets(self) -> bool:
        for candidate in combinations(self.table, 3):
            if self.is_valid_set(candidate):
                print(f'\nSET!!!\n{candidate[0]}\n{candidate[1]}\n{candidate[2]}')
                self.table.remove(candidate[0])
                self.table.remove(candidate[1])
                self.table.remove(candidate[2])
                return True
        return False
    
    def game_loop(self):
        counter = 0
        while True:
            while len(self.table) < 9:
                if self.deck.is_empty():
                    break
                self.table.add(self.deck())
            if not self.find_sets():
                if self.deck.is_empty():
                    break
                self.table.add(self.deck())
            else:
                counter += 1
        
        print(f'\n{counter} sets found')
    
    def is_valid_set(self, candidate):
        for attribute in ['number', 'color', 'shape', 'filling']:
            attr1 = getattr(candidate[0], attribute)
            attr2 = getattr(candidate[1], attribute)
            attr3 = getattr(candidate[2], attribute)
            if not (attr1 == attr2 == attr3 or attr1 != attr2 != attr3 != attr1):
                return False
        return True

def main():
    Game()

if __name__ == '__main__':
    main()
