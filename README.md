Set
===

About
-----

I created this for two reasons:

1. my little brother always beats me in this card game.
2. i was interested in its mathematical properties.

###Dependencies

None, only standard Python libraries.

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

The set as shown in the figure would still be valid if all card had the same color

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

### My approach

In main.py, I run a set number of games and keep track of the largest number of cards that has been present on the table.
This number minus one should be the answer to the question about the biggest "anti-set" that has been encountered.

100.000 games takes roughly 5 minutes, and the largest number of cards present on the table is ±18.
This is to be expected, but more thorough experiments could be run in the hopes of reaching 21, which would be the limit Charlotte Chan showed an example of.
