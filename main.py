import random

# Die Class:
# - value: int
# - roll() -> none

# Player Class:
# - die: Die
# - is_computer: bool
# - counter: int
# - increment_counter() -> none
# - decrement_counter() -> none
# - roll_die() -> none

# DiceGame Class:
# - human: Player
# - computer: Player
# - play() -> None
# - play_round() -> None
# - check_game_over() -> bool

class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value


# Testing the class
die = Die()

print(die.value)
die.roll()

print(die.value)