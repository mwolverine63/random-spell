"""
Script returns a random wizard spell that the input level can cast

Alex Philpott in Python 3.6
"""
import csv
import argparse
from typing import Dict
import random

# Define max spell level for each wizard level
MAX_SPELL_LEVEL = {
    '1': 1,
    '2': 1,
    '3': 2,
    '4': 2,
    '5': 3,
    '6': 3,
    '7': 4,
    '8': 4,
    '9': 5,
    '10': 5,
    '11': 6,
    '12': 6,
    '13': 7,
    '14': 7,
    '15': 8,
    '16': 8,
    '17': 9,
    '18': 9,
    '19': 9,
    '20': 9
}

def get_spell_dict() -> Dict[str, float]:
    """
    Parse the wizard spells csv and return a dict containing them

    :return: dict with key as wizard spell and value as spell level
    """
    spells = {}
    with open('wizard_spells.csv', 'r') as fin:
        READER = csv.reader(fin)

        for row in READER:
            try:
                # Only save the first character of the spell level
                spells[row[0].strip()] = float(row[1][0].strip())
            except ValueError:
                continue

    return spells

if __name__ == "__main__":
    # Parse input args
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('wizard_level', help='Level of the wizard character', type=int)

    args = vars(PARSER.parse_args())

    level = args['wizard_level']

    if not 1 <= level <= 20:
        PARSER.error('Wizard level must be between 1 and 20')

    # Parse csv
    spells_dict = get_spell_dict()
    spells = list(spells_dict.keys())

    # Get max spell level
    max_spell_level = MAX_SPELL_LEVEL[str(level)]

    while True:
        rand_num = random.randrange(len(spells))
        spell = spells[rand_num]
        level = spells_dict[spell]

        if level <= max_spell_level:
            print('Random spell: {}'.format(spell))
            break