"""compere.

Cleans the console and shows a nice message that indicates the init execution
of the system.

"""
from os import name, system
from typing import Callable


title = """
   _____                                
  / ____|                               
 | (___   ___ _ __ __ _ _ __   ___ _ __ 
  \___ \ / __| '__/ _` | '_ \ / _ \ '__|
  ____) | (__| | | (_| | |_) |  __/ |   
 |_____/ \___|_|  \__,_| .__/ \___|_|   
                       | |              
                       |_| 
"""


def compere():
    """Compere.

    Displays on screen a nice title.

    """
    clear: Callable = lambda: system("clear")
    clear()
    print(title)
