import json
from iso3166 import countries
import collections.abc
import pygal
from pygal.style import RotateStyle

# Function to get the country code
def get_country_code(country_name):
    try:
        return countries.get(country_name).alpha2.lower()
    except KeyError:
        return None

# Load the JSON file
with open("C:/Users/shado/Downloads/Population.json", 'r') as f:
    data = json.load(f)

cc_populations = {}

# Iterate over each country in the data
for country_code, country_data in data.items():
    # Ensure country_data is a dictionary before checking for keys
    if isinstance(country_data, dict) and 'data' in country_data and '2010' in country_data['data']:
        country_name = country_data['name']
        population = int(country_data['data']['2010'])

        # Get the two-letter country code
        code = get_country_code(country_name)

        if code:
            cc_populations[code] = population

# Create a Pygal world map
from pygal_maps_world.maps import World
from pygal.style import RotateStyle

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = "World Population in 2010 by Country"
wm.add('2010', {'us': 309349000, 'ca': 34126000, 'mx': 113423000})
wm.render_to_file('world_population.svg')

print("Map has been created successfully!")
