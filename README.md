Set
===

About
-----

I created this for two reasons:

1. my little brother always beats me in this card game.
2. i was interested in its mathematical properties.

### Dependencies

Python 3.10, because I'm using `TypeAlias`  
Python 3.9 for type hinting with collections (`set`) and for using `itertools.product`  
Python 3.7 will probably work if you remove all type hinting and replace `itertools.product` with a nested for-loop in a generator expression

### Usage

In main.py, you can change `n_games`, `N_ATTRIBUTES`, and `N_VARIATIONS` and just run it to see what happens.

There are also some additional files and depracated code where I tried other approaches, but this functional one was the one I was most happy with, so that's the one where all the fun stuff is.

Rules of _Set_
--------------

In the traditional game of _set_, a card has four attributes, and for every one of those attributes there are three variations.

| Number | Color  | Shape   | Filling |
|--------|--------|---------|---------|
| One    | Green  | Diamond | Empty   |
| Two    | Blue   | Wave    | Half    |
| Three  | Red    | Pill    | Filled  |

An example card could have two blue wave-shaped objects with half filling.

A game typically starts with 9 cards on the table.
When one of the players sees a set, they simply say "SET!", point to the cards in question and if the set is valid, they get to keep the cards.
The dealer puts new cards on the table so there are 9 again, and the game continues untill the deck is empty.

### What is a _set_?

A "set" is made up of three cards, when for each of their properties the following holds:
- they either share the same variation of that property (e.g., all the same color)
- or they all have unique variations of that property (e.g., 1 2 3, but not 1 2 2)

The set as shown in the figure would still be valid if all cards had the same color, but not if the third card would also be diamond-shaped.

<fig>
  <img src="https://github.com/Josef-Hlink/Set/blob/main/assets/set.png" width="256" alt="example cards"/>
  <figcaption>Example of three cards that form a valid set</figcaption>
</fig>

Mathematical properties
-----------------------

The deck is made up of all possible cards, which would be 81 (3<sup>4</sup>) unique instances.
The formula here is _F_<sup>_P_</sup>, with _F_ being the number of features every card has, and _P_ being the number of possibilities for each of there features. Simple math, right?

The part where the math gets interesting is when we want to determine so-called "anti-sets".
As we saw earlier, the game starts with 9 cards on the table.
However, it is quite often the case that no player can find a set in them, and a 10<sup>th</sup> card is needed, or a 11<sup>th</sup>, 12<sup>th</sup>, etc.

The question arises:

> _What is the smallest number of cards where a set **must** be present?_

Or phrasing the problem differently, making it easier to talk about mathematically:

> _What is the largest number of cards where **no** set is present?_

I recommend taking a look at Charlotte Chan's [answer](http://web.math.princeton.edu/~charchan/SET.pdf), and for verification of her example, taking a look at my [antiset.py](https://github.com/Josef-Hlink/Set/blob/main/additional/antiset.py).

My approach
-----------

In main.py, I run a set number of games and keep track of the largest number of cards that has been present on the table.
This number minus one should be the answer to the question about the biggest "anti-set" that has been encountered.

10M games took my MacBook Air M1 roughly hours, and the largest number of cards present on the table was only 19.
Unless an even better example can be thought of than the one that Charlotte Chan showed, the theoretical limit should be 21.

After running this experiment, I added a `@cache` decorator to `is_set()`, resulting in a speedup of ±300%.
Sadly, this run yielded the same results as the previous one: an anti-set of just 18 cards.
The cache stores every _set_ candidate it encounters in a hash-map, so it will never have to do the calculation for the same set of arguments twice.
This is feasible, because in one game, many calls to the function will be the exact same due to the fact that the board configuration largely remains the same from one round to the next.

A more thorough run will be done soon, when even more optimizations are implemented.
In order to encounter the exact configuration where 20 cards exactly compose Chan's "anti-set", upwards of 10<sup>120</sup> (81!) would be needed.
