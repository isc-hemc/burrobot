"""compere.

Cleans the console and shows a nice message that indicates the init execution
of the system.

"""
from os import name, system
from typing import Callable


title = """
  _   _ _      _____  
 | \ | | |    |  __ \ 
 |  \| | |    | |__) |
 | . ` | |    |  ___/ 
 | |\  | |____| |     
 |_| \_|______|_|     
"""


def compere():
    """Compere.

    Displays on screen a nice title.

    """
    clear: Callable = lambda: system("clear")
    clear()
    print(title)
