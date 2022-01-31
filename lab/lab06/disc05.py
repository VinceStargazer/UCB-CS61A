from tree import *
from doctest import testmod


class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Mailman:
    """Each Mailman has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds it
        to the clients instance attribute.
        """
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), mailman
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, mailman, name):
        self.inbox = []
        self.mailman = mailman
        self.name = name

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        email = Email(msg, self.name, recipient_name)
        self.mailman.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)


class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Dog(Pet):
    def __init__(self, name, owner):
        Pet.__init__(self, name, owner)

    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        """A cat says meow! when asked to talk."""
        print(self.name + ' says meow!')

    def lose_life(self):
        """A cat can only lose a life if they have at
        least one life. When lives reaches zero, 'is_alive'
        becomes False.
        """
        self.lives -= 1
        if self.lives <= 0:
            self.is_alive = False


class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    def talk(self):
        """Repeat what a Cat says twice."""
        for time in range(2):
            Cat.talk(self)


class Yolo:
    def __init__(self, motto):
        self.motto = motto

    def g(self, num):
        return self.motto + num


def about_equal(t1, t2):
    """Returns whether two trees are 'about equal.'
    Two trees are about equal if and only if they contain
    the same labels the same number of times.
    >> x = tree(1, [tree(2), tree(2), tree(3)])
    >> y = tree(3, [tree(2), tree(1), tree(2)])
    >> about_equal(x, y)
    True
    >> z = tree(3, [tree(2), tree(1), tree(2), tree(3)])
    >> about_equal(x, z)
    False
    """
    def tree_to_list(t):
        if is_leaf(t):
            return [label(t)]
        return [label(t)] + [tree_to_list(b) for b in branches(t)]
    return sorted(tree_to_list(t1)) == sorted(tree_to_list(t2))


def decrypt(s, d):
    """List all possible decoded strings of s.
    >>> codes = {
    ... 'alan': 'spooky',
    ... 'al': 'drink',
    ... 'antu': 'your',
    ... 'turing': 'ghosts',
    ... 'tur': 'scary',
    ... 'ing': 'skeletons',
    ... 'ring': 'ovaltine'
    ... }
    >>> decrypt('alanturing', codes)
    ['drink your ovaltine', 'spooky ghosts', 'spooky scary skeletons']
    """
    if s == '':
        return []
    ms = []
    if s in d:
        ms.append(d[s])
    for k in range(1, len(s) + 1):
        first, suffix = s[:k], s[k:]
        if first in d:
            for rest in decrypt(suffix, d):
                ms.append(d[first] + ' ' + rest)
    return ms


def ensure_consistency(fn):
    """Returns a function that calls fn on its argument, returns fn's
    return value, and returns None if fn's return value is different
    from any of its previous return values for those same argument.
    Also returns None if more than 20 calls are made.
    >>> def consistent(x):
    ...     return x
    >>>
    >>> lst = [1, 2, 3]
    >>> def inconsistent(x):
    ...     return x + lst.pop()
    >>>
    >>> a = ensure_consistency(consistent)
    >>> a(5)
    5
    >>> a(5)
    5
    >>> a(6)
    6
    >>> a(6)
    6
    >>> b = ensure_consistency(inconsistent)
    >>> b(5)
    8
    >>> b(5)
    None
    >>> b(6)
    7
    """
    n = 20
    z = {}

    def helper(x):
        nonlocal n
        n -= 1
        if n < 0:
            return print('None')
        val = fn(x)
        if x not in z:
            z[x] = [val]
        if val not in z[x]:
            return print('None')
        else:
            z[x] = [val]
            return val
    return helper


testmod()
