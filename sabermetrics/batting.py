"""
.. module:: batting
   :platform: Unix, Windows
   :synopsis: Batting module for sabermetrics package containing some functions related to batting only.

.. moduleauthor:: Fernando Crema <fcremaldc@gmail.com>
"""


def avg(h, ab):
    r"""Batting average is determined by dividing a player's hits by his total at-bats for a number between zero
    (shown as .000) and one (1.000).

    .. math::
        AVG = \frac{H}{AB}

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


def babip(h, hr, ab, k, sf):
    r"""BABIP measures a player's batting average exclusively on balls hit into the field of play, removing outcomes
    not affected by the opposing defense (namely home runs and strikeouts).

    .. math::
        BABIP = \frac{H-HR}{AB-K-HR-SF}

    :param h: Hits.
    :type h: int.
    :param hr: Homeruns.
    :type hr: int.
    :param ab: At bats.
    :type ab: int.
    :param k: Strikeouts.
    :type k: int.
    :param sf: Sacrifice fly.
    :type sf: int.
    :returns:  float -- Batting average balls in play..
    :raises: ZeroDivisionError
    """

    try:
        return (h-hr)*1.0/(ab-k-hr-sf)
    except ZeroDivisionError:
        print('Balls in play must be greater than 0')
        import sys
        sys.exit(-1)