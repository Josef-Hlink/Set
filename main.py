"""
Functional approach at creating the SET game
------------------------------------------------------------------
This script can be configured to run any number of set games,
with different numbers of attributes and variations.
It will return the largest number of cards that were on the table,
along with what set has been found on that table.
------------------------------------------------------------------
Author: J.D. Hamelink
Date: May 2022
"""

import random
import time
from itertools import product, combinations

def main():
    global N_ATTRIBUTES, N_VARIATIONS
    N_ATTRIBUTES = 4
    N_VARIATIONS = 3
    n_games = 1000

    highest = 0
    highest_table = set()
    set_in_highest = set()
    
    tic = time.perf_counter()

    for i in range(n_games):
        try:
            if (i)%(n_games//100) == 0: print(f'\r{i}/{n_games}', end='')
        except ZeroDivisionError: print(f'\r{i}/{n_games}', end='')
        
        highest, highest_table, set_in_highest = game(highest, highest_table, set_in_highest)
    
    toc = time.perf_counter()

    print(f'\rlargest amount of cards on table: {highest}')
    for card in highest_table:
        if card in set_in_highest: print(f'\033[36m{card}\033[0m')
        else: print(card)
    print(f'{n_games} games took {toc-tic:.2f} seconds')

def game(highest: int, highest_table: set[tuple], set_in_highest: set[tuple]) -> \
            tuple[int,                set[tuple],                 set[tuple]]:

    pile = set(product(*[range(N_VARIATIONS) for _ in range(N_ATTRIBUTES)]))
    table = set()

    while True:
        while len(table) < N_VARIATIONS**2:
            if not pile: break
            table.add(draw(pile))
        for candidate_set in combinations(table, N_VARIATIONS):
            if is_set(candidate_set):
                if len(table) > highest: highest, highest_table, set_in_highest = len(table), table.copy(), candidate_set
                for card in candidate_set: table.remove(card)
                break
        else:
            if not pile: break
            table.add(draw(pile))

    return (highest, highest_table, set_in_highest)

def draw(pile: set[tuple]) -> tuple:
    card = random.choice([*pile])
    pile.remove(card)
    return card

def is_set(triple: set[tuple]) -> bool:
    for i in range(N_ATTRIBUTES):
        if len({triple[j][i] for j in range(N_VARIATIONS)}) in range(2, N_VARIATIONS): return False
    return True


if __name__ == '__main__':
    main()
