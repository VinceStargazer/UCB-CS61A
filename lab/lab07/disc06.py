from doctest import testmod
from math import prod
from lab07 import *
from tree import *


def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk.rest is Link.empty:
        return lnk.first
    return lnk.first + sum_nums(lnk.rest)


def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.first
    0
    >>> p.rest.rest.rest
    ()
    """
    product, continued = 1, True
    for lnk in lst_of_lnks:
        product *= lnk.first
        if lnk.rest is Link.empty:
            continued = False
    if not continued:
        return Link(product)
    return Link(product, multiply_lnks([lnk.rest for lnk in lst_of_lnks]))


def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> unique = remove_duplicates(lnk)
    >>> unique
    Link(1, Link(5))
    >>> lnk
    Link(1, Link(5))
    """
    sets, lnk2 = [], Link.empty
    for i in link_to_list(lnk):
        if i not in sets:
            sets.append(i)
    for s in reversed(sets):
        lnk2 = Link(s, lnk2)
    lnk.first, lnk.rest = lnk2.first, lnk2.rest
    return lnk


def even_weighted(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i * lst[i] for i in range(len(lst)) if i % 2 == 0]


def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if not lst:
        return []
    pivot = lst[0]
    less = [num for num in lst if num < pivot]
    greater = [num for num in lst if num > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)


def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not lst:
        return 1
    if len(lst) in [1, 2]:
        return max(lst)
    if len(lst) == 3:
        return max(lst[0] * lst[2], lst[1])
    return max(lst[0] * max_product(lst[2:]), lst[1] * max_product(lst[3:]))


def eval_tree(tree):
    """Evaluates an expression tree with functions the root.
    >>> eval_tree(tree(1))
    1
    >>> expr = tree('*', [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree('+', [expr, tree(4), tree(5)]))
    15
    """
    if label(tree) == '*':
        return prod([eval_tree(b) for b in branches(tree)])
    elif label(tree) == '+':
        return sum([eval_tree(b) for b in branches(tree)])
    else:
        return label(tree)


def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> print_levels(redundant_map(tree, double))
    [2]
    [4, 8]
    [16]
    [256]
    """
    t.label = f(t.label)
    new_f = lambda x: f(f(x))
    t.branches = [redundant_map(b, new_f) for b in t.branches]
    return t


class Dress:
    """What color is the dress?
    >>> blue = Dress('blue')
    >>> blue.look()
    'blue'
    >>> gold = Dress('gold')
    >>> gold.look()
    'gold'
    >>> blue.look() # 2 does not evenly divide 3; changes to gold
    >>> Dress('black').look()
    'black'
    >>> gold.look() # 2 does not evenly divide 5; changes to black
    >>> gold.look() # 3 evenly divides 6
    'black'
    >>> Dress('white').look()
    'white'
    >>> gold.look() # 4 evenly divides 8
    'black'
    >>> blue.look() # 3 evenly divides 9
    'gold'
    """
    seen = 0
    color = None

    def __init__(self, color):
        self.color = color
        self.seen = 0

    def look(self):
        self.seen = self.seen + 1
        Dress.seen = Dress.seen + 1
        if Dress.seen % self.seen == 0:
            Dress.color = self.color
            return self.color
        else:
            self.color = Dress.color


def play_round(starter, cards):
    """Play a round and return all winners so far. Cards is a list of pairs.
    Each (who, card) pair in cards indicates who plays and what card they play.
    >>> play_round(3, [(3, 4), (0, 8), (1, 8), (2, 5)])
    [1]
    >>> play_round(1, [(3, 5), (1, 4), (2, 5), (0, 8), (3, 7), (0, 6), (1, 7)])
    It's not your turn, player 3
    It's not your turn, player 0
    The round is over, player 1
    [1, 3]
    >>> play_round(3, [(3, 7), (2, 5), (0, 9)]) # Round is never completed
    It's not your turn, player 2
    [1, 3]
    """
    r = Round(starter)
    for who, card in cards:
        try:
            r.play(who, card)
        except AssertionError as e:
            print(e)
    return Round.winners


class Round:
    players, winners = 4, []

    def __init__(self, starter):
        self.starter, self.player, self.highest = starter, starter, -1

    def play(self, who, card):
        assert not self.complete(), 'The round is over, player '+str(who)
        assert who is self.player, "It's not your turn, player "+str(who)
        self.player = (self.player + 1) % 4
        if card >= self.highest:
            self.control, self.highest = who, card
        if self.complete():
            self.winners.append(self.control)

    def complete(self):
        return self.starter == self.player and self.highest > -1


testmod()
