"""
.. module:: pitching
   :platform: Unix, Windows
   :synopsis: Pitching module for sabermetrics package containing some functions related to pitching only.

.. moduleauthor:: Fernando Crema <fcremaldc@gmail.com>
"""


def era(er, outs):
    """Represents the number of earned runs a pitcher allows per nine innings -- with earned runs being any runs that
    scored without the aid of an error or a passed ball.
    :param er: Earned runs.
    :type er: int.
    :param outs: Number of batters and baserunners that are put out while the pitcher is on the mound.
    :type outs: int.
    :returns:  float -- the return code.
    :raises: ZeroDivisionError
    """

    try:
        return 27.0*er/outs
    except ZeroDivisionError:
        print("Outs must be greater than 0.")
        import sys
        sys.exit(-1)

