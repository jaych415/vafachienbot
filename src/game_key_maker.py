from .player import Player
from .screens import Scene
from .dungeons.intro_dungeon import IntroDungeon

class GameKeyMaker:
    def __init__(self, intro_class):
        self.player = Player()
        self.game_over = False

        self.screens = {
            "forest clearing": intro_class("Forest Clearing", "You're in a clearing surrounded by tall trees.", items=["seed"]),
            "shaded grove": Scene("Shaded Grove", "Sunlight filters through. Nature feels alive.", items=["water", "twig"]),
            "tree hollow": Scene("Tree Hollow", "You discover a hollow tree — it could be a way out.", items=["leaf", "bark", "moss"]),
        }

        self.current_screen = self.screens["forest clearing"]

    def start(self):
        print("\n🌳 Welcome to the Nature Escape Game 🌱")
        while not self.game_over:
            self.current_screen.enter(self)

    def change_screen(self, name):
        if name in self.screens:
            self.current_screen = self.screens[name]
        else:
            print("That place doesn't exist.")
