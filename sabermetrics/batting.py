"""
.. module:: batting
   :platform: Unix, Windows
   :synopsis: Batting module for sabermetrics package containing some functions related to batting only.

.. moduleauthor:: Fernando Crema <fcremaldc@gmail.com>
"""


def avg(h, ab):
    """batting average is determined by dividing a player's hits by his total at-bats for a number between zero
    (shown as .000) and one (1.000).
    :param h: Hits.
    :type h: int.
    :param ab: At bats.
    :type ab: int.
    :returns:  float -- The batting average.
    :raises: ZeroDivisionError
    """
    # TODO: Add innings option.
    try:
        return h*1.0/ab
    except ZeroDivisionError:
        print("At bats must be greater than 0.")
        import sys
        sys.exit(-1)