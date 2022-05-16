"""
Imperative approach at creating the SET game
--------------------------------------------
Functionally identical to the OOP approach,
but much shorter and more efficient.
--------------------------------------------
Author: J.D. Hamelink
Date: May 2022
"""

import random
from itertools import product, combinations

PILE = set(product(*[[1,2,3] for _ in range(4)]))
TABLE = set()

def draw() -> tuple:
    card = random.sample(PILE, 1)[0]
    PILE.remove(card)
    return card

def is_set(triple: set[tuple]) -> bool:
    for i in range(4):
        uniques = len(set([triple[0][i], triple[1][i], triple[2][i]]))
        if uniques == 2:
            return False
    return True

while True:
    while len(TABLE) < 9:
        if not PILE: break      # no more cards left
        TABLE.add(draw())
    for candidate_set in combinations(TABLE, 3):
        if is_set(candidate_set):
            print(f'\nSET!!!\n{candidate_set[0]}\n{candidate_set[1]}\n{candidate_set[2]}')
            TABLE.remove(candidate_set[0]); TABLE.remove(candidate_set[1]); TABLE.remove(candidate_set[2])
            break
    else:
        if not PILE: break      # no more cards left
        TABLE.add(draw())
