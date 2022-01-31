from doctest import testmod


class Baller:
    all_players = []

    def __init__(self, name, has_ball = False):
        self.name = name
        self.has_ball = has_ball
        Baller.all_players.append(self)

    def pass_ball(self, other_player):
        if self.has_ball:
            self.has_ball = False
            other_player.has_ball = True
            return True
        else:
            return False


class BallHog(Baller):
    def pass_ball(self, other_player):
        return False


class TeamBaller(Baller):
    """
    >>> cheerballer = TeamBaller('Thomas', has_ball=True)
    >>> surya = BallHog('Surya')
    >>> cheerballer.pass_ball(surya)
    Yay!
    True
    >>> cheerballer.pass_ball(surya)
    I don't have the ball
    False
    """
    def pass_ball(self, other_player):
        if self.has_ball:
            self.has_ball = False
            other_player.has_ball = True
            print('Yay!')
            return True
        else:
            print("I don't have the ball")
            return False


class PingPongTracker:
    """
    >>> tracker1 = PingPongTracker()
    >>> tracker2 = PingPongTracker()
    >>> tracker1.next()
    1
    >>> tracker1.next()
    2
    >>> tracker1.next()
    3
    >>> tracker1.next()
    4
    >>> tracker1.next()
    5
    >>> tracker1.next()
    6
    >>> tracker1.next()
    7
    >>> tracker1.next()
    6
    >>> tracker2.next()
    1
    """
    def __init__(self):
        self.current = 0
        self.index = 1
        self.add = True

    def next(self):
        if self.add:
            self.current += 1
        else:
            self.current -= 1
        if self.index % 7 == 0 or has_seven(self.index):
            self.add = not self.add
        self.index += 1
        return self.current


def has_seven(k):
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


testmod()
