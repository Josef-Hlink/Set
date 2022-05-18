"""
Script to verify Charlotte Chan's example of 20 cards that make up an "anti-set"
"""

from itertools import combinations

TABLE = {
    (0,0,0,0),
    (2,0,0,0),
    (0,0,1,0),
    (2,0,1,0),
    (1,0,2,1),
    (1,0,0,2),
    (0,0,2,2),
    (2,0,2,2),
    (1,0,1,2),
    (1,1,2,0),
    (1,1,2,2),
    (1,2,0,0),
    (0,2,2,0),
    (2,2,2,0),
    (1,2,1,0),
    (1,2,2,1),
    (0,2,0,2),
    (2,2,0,2),
    (0,2,1,2),
    (2,2,1,2)
}

def is_set(triple: set[tuple]) -> bool:
    for i in range(4):
        uniques = len(set([triple[0][i], triple[1][i], triple[2][i]]))
        if uniques == 2:
            return False
    return True

sets_found = 0
for candidate_set in combinations(TABLE, 3):
    if is_set(candidate_set):
        sets_found += 1
        print(f'\nSET!!!\n{candidate_set[0]}\n{candidate_set[1]}\n{candidate_set[2]}')

if sets_found == 0:
    print(f'no sets found in {len(TABLE)} cards')
