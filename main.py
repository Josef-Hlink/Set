"""
Brute-force approach at solving the "anti-set" problem
-------------------------------------------------------------------
This script is used for a brute-force approach at finding the
largest anti-set by playing a number of complete traditional games.
It will return the largest number of cards that were on the table,
along with what set has been found on that table.
-------------------------------------------------------------------
Author: J.D. Hamelink
Date: May 2022
"""

import random                           # taking random cards from deck
import time                             # tracking experiment time
from itertools import product           # taking all potential sets on a board
from itertools import combinations      # mathematical stuff I couldn't be bothered to write out
from typing import TypeAlias            # type hinting <3
from functools import cache             # major speed boost

Card: TypeAlias = tuple[int]

def main():
    # 1e3 = 1K, 1e5 = 100K, etc. this notation makes it easier to switch n_games imo
    n_games: int = 1e3
    random.seed(123)
    
    highest: int = 0                    # largest number of cards on table
    highest_table: set[Card] = set()    # table where ^ was encountered
    set_in_highest: set[Card] = set()   # valid set that was found in ^ table
    
    tic: float = time.perf_counter()

    for i in range(int(n_games)):
        # progress counter
        try:
            if (i)%(n_games//100) == 0: print(f'\r{round(i/n_games*100)}%', end='')
        except ZeroDivisionError: print(f'\r{i}/{n_games}', end='')
        # one playout
        highest, highest_table, set_in_highest = game(highest, highest_table, set_in_highest)
    
    toc: float = time.perf_counter()

    # printing statistics
    print(f'\rlargest number of cards on table: {highest}')
    for card in highest_table:
        if card in set_in_highest: print(f'\033[1m\033[36m{card} <-\033[0m')
        else:                      print(card)
    print(f'{int(n_games)} games took {toc-tic:.2f} seconds')

def game(highest: int, highest_table: set[Card], set_in_highest: set[Card]) -> tuple[int, set[Card], set[Card]]:
    """Does one playout of a SET game where the computer finds all valid sets until deck is empty"""

    deck: set[Card] = set(product(*[range(3) for _ in range(4)]))
    table: set[Card]  = set()

    def draw() -> Card:
        """Draws one random card from deck"""
        card: Card = random.choice([*deck])
        deck.remove(card)
        return card

    while True:
        # fill up table until minimum amount of cards are present
        while len(table) < 9:
            if not deck: break
            table.add(draw())
        # play one round; see if any sets are present on the table
        for candidate_set in combinations(table, 3):
            if is_set(candidate_set):
                if len(table) > highest:
                    highest, highest_table, set_in_highest = len(table), table.copy(), candidate_set
                for card in candidate_set: table.remove(card)
                break
        # always add one card after a round
        if not deck: break
        table.add(draw())

    return (highest, highest_table, set_in_highest)

@cache
def is_set(candidate: set[Card]) -> bool:
    """Checks if a triple of cards is a valid set"""
    for i in range(4):
        # attribute variations must either be identical or all unique
        # if number of unique values is neither 1 nor n_variations, the candidate can not be valid
        if len({candidate[j][i] for j in range(3)}) == 2: return False
    return True


if __name__ == '__main__':
    main()
