from lea import *

from itertools import combinations_with_replacement
from math import factorial

# TODO: Generalise this to pick from any distribution, not just a die roll.
def dice_set_freqs(n, m):
    """Sets of N M-sided dice, ignoring order, with relative frequencies.
    """
    # The total number of permutations of N dice is N!
    permutations = factorial(n)

    # Use itertools to get the sets.
    for outcome in combinations_with_replacement(range(1, m+1), n):
        # For each set, the weight is N!/a!b!c!... where a, b, c... are
        # the sizes of each group of equal values.
        weight = permutations
        # We run through the set counting an dividing as we go
        run_len = 0
        prev_roll = None
        for roll in outcome:
            if roll != prev_roll:
                prev_roll = roll
                run_len = 0
            run_len = run_len + 1
            if run_len > 1:
                weight = weight // run_len
        yield outcome, weight

# This is actually general enough to start from any distribution
def dice(n, m):
    """A Lea distribution representing an ordered set of N M-sided dice.
    """
    return Lea.interval(1, m).cprodTimes(n)

# See the todo note above
def dice_unordered(n, m):
    """A Lea distribution representing an unordered set of N M-sided dice.

    Combinations of dice which are the same apart from order are considered
    equal. The particular value used is chosen to be in order from smallest
    to largest.
    """
    return Lea.fromValFreqs(*dice_set_freqs(n, m))
