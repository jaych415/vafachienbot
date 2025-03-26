class IntroDungeon:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items or []

    def enter(self, game):
        print(f"\n--- {self.name.upper()} ---")
        print(self.description)
        if self.items:
            print("\nItems here:")
            for item in self.items:
                print(f" - {item}")
        else:
            print("\nThere are no items here.")

        self.menu_loop(game)

    def menu_loop(self, game):
        while True:
            print("\nWhat would you like to do?")
            print("1. Take an item")
            print("2. Combine items")
            print("3. Check backpack")
            print("4. Move to another location")
            print("5. Try to escape")
            print("6. Quit")

            choice = input("> ").strip()

            if choice == "1":
                if not self.items:
                    print("There are no items to take.")
                else:
                    print("\nWhich item would you like to take?")
                    for i, item in enumerate(self.items, 1):
                        print(f"{i}. {item}")
                    item_choice = input("> ").strip()
                    if item_choice.isdigit():
                        index = int(item_choice) - 1
                        if 0 <= index < len(self.items):
                            item = self.items.pop(index)
                            game.player.add_to_backpack(item)
                        else:
                            print("Invalid selection.")
                    else:
                        print("Please enter a number.")

            elif choice == "2":
                print("Enter the names of two items to combine:")
                item1 = input("Item 1: ").strip().lower()
                item2 = input("Item 2: ").strip().lower()
                game.player.combine_items(item1, item2)

            elif choice == "3":
                game.player.show_backpack()

            elif choice == "4":
                print("\nWhere would you like to go?")
                for key in game.screens:
                    print(f"- {key}")
                dest = input("> ").strip().lower()
                if dest in game.screens:
                    game.change_screen(dest)
                    return
                else:
                    print("You can't go there.")

            elif choice == "5":
                if self.name == "Tree Hollow" and "sprout" in game.player.backpack and "nest" in game.player.backpack:
                    print("You plant the sprout in the nest... A magical tree lifts you to safety. You win! 🌳✨")
                    game.game_over = True
                    return
                else:
                    print("You can't escape yet. Maybe you're missing something...")

            elif choice == "6":
                print("Thanks for playing!")
                game.game_over = True
                return

            else:
                print("Please enter a number between 1 and 6.")
