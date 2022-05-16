"""
Charlotte Chan's example of 20 cards that make up an "anti-set"
"""

from itertools import combinations

TABLE = {
    (1,'r','~','▓'),
    (3,'r','~','▓'),
    (1,'r','○','▓'),
    (3,'r','○','▓'),
    (2,'r','□','▒'),
    (2,'r','~','░'),
    (1,'r','□','░'),
    (3,'r','□','░'),
    (2,'r','○','░'),
    (2,'g','□','▓'),
    (2,'g','□','░'),
    (2,'b','~','▓'),
    (1,'b','□','▓'),
    (3,'b','□','▓'),
    (2,'b','○','▓'),
    (2,'b','□','▒'),
    (1,'b','~','░'),
    (3,'b','~','░'),
    (1,'b','○','░'),
    (3,'b','○','░'),
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

if not sets_found:
    print(f'no sets found in {len(TABLE)} cards')
