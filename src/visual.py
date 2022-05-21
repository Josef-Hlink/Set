"""
plots
------------------------------------------------------------------
WIP
------------------------------------------------------------------
Author: J.D. Hamelink
Date: May 2022
"""

from helper import fix_dirs, histogram, log_plot, save_plot
from math import log10

import os                               # directories
import random                           # taking random cards from deck
import time                             # tracking experiment time
from itertools import product           # taking all potential sets on a board
from itertools import combinations      # mathematical stuff I couldn't be bothered to write out
from typing import TypeAlias            # type hinting <3
from functools import cache             # major speed boost
import argparse                         # easier experiment settings

Card: TypeAlias = tuple[int]

def main():
    fix_dirs()

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--n_games', type=int, help='set the number of games to play (order of magnitude)')
    args = parser.parse_args()
    if args.n_games is not None:
        n_games: int = 10 ** args.n_games
    else:
        n_games: int = 1e3
    powers_of_10: set[int] = {10**x for x in range(int(log10(n_games))+1)}
    random.seed(123)
    
    global N_ATTRIBUTES, N_VARIATIONS
    N_ATTRIBUTES = 4        # for "normal" SET: number, color, shape, filling
    N_VARIATIONS = 3        # for "normal" SET: 123,    gbr,   dwp,   ehf

    global UNIQUE_SETS
    UNIQUE_SETS = set()
    
    highest: int = 0                    # largest number of cards on table
    highest_table: set[Card] = set()    # table where ^ was encountered
    set_in_highest: set[Card] = set()   # valid set that was found in ^ table
    distr = []
    sets_evaluated = []

    tic: float = time.perf_counter()

    for i in range(int(n_games)):
        # progress counter
        try:
            if (i)%(n_games//100) == 0: print(f'\r{round(i/n_games*100)}%', end='')
        except ZeroDivisionError: print(f'\r{i}/{n_games}', end='')
        # one playout
        distr, highest, highest_table, set_in_highest = game(distr, highest, highest_table, set_in_highest)
        if i+1 in powers_of_10:
            sets_evaluated.append(len(UNIQUE_SETS))

    toc: float = time.perf_counter()

    # printing statistics
    print(f'\rlargest number of cards on table: {highest}')
    for card in highest_table:
        if card in set_in_highest: print(f'\033[1m\033[36m{card} <-\033[0m')
        else:                      print(card)
    print(f'{int(n_games)} games took {toc-tic:.2f} seconds')
    
    fig = histogram(distr)
    save_plot(fig, filename=os.path.join('..', 'results', 'distribution.png'))
    fig = log_plot(sets_evaluated)
    save_plot(fig, filename=os.path.join('..', 'results', 'cachesize.png'))

def game(distr, highest: int, highest_table: set[Card], set_in_highest: set[Card]) -> tuple[int, set[Card], set[Card]]:
    """Does one playout of a SET game where the computer finds all valid sets until deck is empty"""

    deck: set[Card] = set(product(*[range(N_VARIATIONS) for _ in range(N_ATTRIBUTES)]))
    table: set[Card]  = set()

    def draw() -> Card:
        """Draws one random card from deck"""
        card: Card = random.choice([*deck])
        deck.remove(card)
        return card

    while True:
        # fill up table until minimum amount of cards are present
        while len(table) < 1:
            if not deck: break
            table.add(draw())
        # play one round; see if any sets are present on the table
        for candidate_set in combinations(table, N_VARIATIONS):
            if is_set(candidate_set):
                distr.append(len(table))
                if len(table) > highest:
                    highest, highest_table, set_in_highest = len(table), table.copy(), candidate_set
                for card in candidate_set: table.remove(card)
                break
        # always add one card after a round
        if not deck: break
        table.add(draw())

    return (distr, highest, highest_table, set_in_highest)

@cache
def is_set(candidate: set[Card]) -> bool:
    """Checks if a triple of cards is a valid set"""
    UNIQUE_SETS.add(candidate)
    for i in range(N_ATTRIBUTES):
        # attribute variations must either be identical or all unique
        # if number of unique values is neither 1 nor n_variations, the candidate can not be valid
        if len({candidate[j][i] for j in range(N_VARIATIONS)}) in range(2, N_VARIATIONS): return False
    return True


if __name__ == '__main__':
    main()
