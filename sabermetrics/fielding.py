"""
.. module:: fielding
   :platform: Unix, Windows
   :synopsis: Fielding module for sabermetrics package containing some functions related to fielding only.

.. moduleauthor:: Fernando Crema <fcremaldc@gmail.com>
"""


def fpct(a, po, e):
    """How often does a fielder or team make the play when tasked with fielding a batted ball, throwing a ball,
     or receiving a thrown ball for an out.
    :param a: Assists.
    :type a: int.
    :param po: Putouts.
    :type po: int.
    :param e: Errors.
    :type e: int.
    :returns:  float -- The fielding percentage.
    :raises: ZeroDivisionError
    """

    try:
        return (po + a) * 1.0 / (po + a + e)
    except ZeroDivisionError:
        print("Total chances must be greater than 0.")
        import sys
        sys.exit(-1)