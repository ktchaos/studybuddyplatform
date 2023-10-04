import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.buddy import Buddy
from data.entities.room import Room

class Manager:
    def __init__(self):
        self.buddies = [Buddy]
        self.rooms = [Room]