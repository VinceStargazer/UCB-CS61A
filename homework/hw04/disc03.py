from doctest import testmod


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def tree_max(tree):
    return max([label(tree)] + [tree_max(b) for b in branches(tree)])

def height(tree):
    if is_leaf(tree):
        return 0
    return max([height(b) + 1 for b in branches(tree)])

def square_tree(tree):
    return [label(tree) ** 2] + [square_tree(b) for b in branches(tree)]

def find_path(tree, x):
    """
    >>> find_path(t, 5)
    [1, 3, 5]
    >>> find_path(t, 10)
    [1, 2, 7, 10]
    >>> find_path(t, 12) # returns None
    """

    if label(tree) == x:
        return [label(tree)]
    for path in [find_path(b, x) for b in branches(tree)]:
        if path:
            return [label(tree)] + path

def prune(tree, k):
    if k == 0:
        return [label(tree)]
    return [label(tree)] + [prune(b, k-1) for b in branches(tree)]

t = tree(1,
         [tree(3,
                [tree(4),
                 tree(5),
                 tree(6)]),
            tree(2,
                 [tree(7,
                       [tree(9),
                        tree(10)]),
                  tree(8)])])

print(tree_max(t))
print(height(t))
print(square_tree(t))
print(prune(t, 2))
print('\a\a\a')
testmod()