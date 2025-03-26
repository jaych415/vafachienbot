### main.py
import os
import sys

# basic code added for the game

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.game_key_maker import GameKeyMaker
from src.dungeons.intro_dungeon import IntroDungeon

def main():
    game = GameKeyMaker(IntroDungeon)
    game.start()

if __name__ == "__main__":
    main()
