from typing import Union

class Bug:
    def __str__(self):
        return "a bug"

    def action(self):
        return "eats it"

class Frog:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle: Bug):
        act = obstacle.action()
        print(f"{self} the frog encounters {obstacle} and {act}!")


class FrogWorld:
    def __init__(self, name: str):
        print(self)
        self._player_name = name

    def __str__(self):
        return"\n\n\t----- FROG WORLD ------"

    def make_character(self) -> Frog:
        return Frog(name=self._player_name)

    def make_obstacle(self) -> Bug:
        return Bug()

class Ork:
    def __str__(self):
        return "an ork"

    def action(self):
        return "kills it"

class Wizard:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle: Ork):
        act = obstacle.action()
        print(f"{self} the wizard battles against {obstacle} and {act}!")

class WizardWorld:
    def __init__(self,name: str):
        print(self)
        self._player_name = name

    def __str__(self):
        return "\n\n\t----- WIZARD WORLD -----"

    def make_character(self):
        return Wizard(name=self._player_name)

    def make_obstacle(self):
        return Ork()

GameFactory = Union[
        FrogWorld,
        WizardWorld]

class GameEnvironment:
    def __init__(self, factory: GameFactory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_age(name: str) -> tuple[bool,int]:
    try:
        age = input(f"Welcome {name}. How old are you? ")
        age = int(age)
    except ValueError:
        print(f"{age} is an invalid age. please try again")
        return (False,age)
    return (True, age)

def main():
    name = input("Hello! What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input,age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()

if __name__ == "__main__":
    main()
