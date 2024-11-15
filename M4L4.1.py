import pygal
from random import randint

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a 6-sided die by default."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1, self.num_sides)


#create 2 D6
die_1 = Die()
die_2 = Die(10)
# Make rolls and store results in a list
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range (2,max_result+1):
    frequency = results.count (value)
    frequencies.append(frequency)
#visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling 1d6 and 1d10 5000 times,"
hist.x_labels = ['2','3','4','5','6','7','8', '9', '10', '11', '12','13','14','15','16']
hist._x_title = 'Result'
hist._y_title = 'Frequency of result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

