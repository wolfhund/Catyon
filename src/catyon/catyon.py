# -*- coding: utf-8 -*-
#from .console.console import *
from console.console import Console


class Catyon(Console):

    """
    Similar behavior as the interface concept from JAVA.
    Inherits given classes so it can implements them in just one main class.
    """
    pass

if __name__ == "catyon.catyon":

    """ Creates main Catyon instance """
    catyon_cmd = Catyon()
    try:
        catyon_cmd.cmdloop(catyon_cmd.logo + "\nWelcome to Catyon!")
    except KeyboardInterrupt:
        catyon_cmd.do_quit(None)
