from random import randint

class Die():
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume 6 sided die"""
        self.num_sides = num_sides

    def roll (self):
        """return random value and number of sides"""
        return randint(1, self.num_sides)
#creates a d20

die = Die()

# make rolls and store results in a list

for roll_num in range (100):
     result = die.roll()
     results.append(result)

print(result)