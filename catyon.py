# -*- coding: utf-8 -*-
"""
Author: Siberian Wolf
Twitter: @wolfs_hund

This twitter client command-line based aims to get all possible twitter 
api functionality. Its special behavior is to be 
capable of extend its own functionality by adding new
features of other Python modules as user need it, without 
implementing all twitter functionality.

Coming up Windows installer on next release
"""

from console import Console
from myFunctions import MyFunctions

class Catyon(Console, MyFunctions):
    """
    Similar behavior as the interface concept from JAVA.
    Inherits given classes so it can implements them in just one main class.    
    """
    pass

if __name__ == "__main__":
    """ Creates main Catyon instance """
    console = Catyon()    
    
    try:
        console.cmdloop(console.logo+"\nWelcome to Catyon!")
    except KeyboardInterrupt:
        console.do_quit(None)
