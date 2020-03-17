#rpg_queries.py

import sqlite3
import os
import pandas as pd

# construct a path to where the data is located
connection = sqlite3.connect('rpg_db.sqlite3')
#print("CONNECTION:", connection)

#create a cursor, what is that for? []
cursor = connection.cursor()
#print("CURSOR:", cursor)

# How many total Characters are there? (query)
character_count = """
    SELECT
    	COUNT (*)
    FROM charactercreator_character;
    """

# Execute query and print result.
result = cursor.execute(character_count).fetchall()
print("\nHow many total Characters are there?", result[0][0])


# Make the format pretty for Tally: How many of each specific subclass? 
print('\nHow many of each specific subclass?')

#for loop for character types query
characters = ['Cleric', 'Fighter', 'Mage', 'Necromancer', 'Thief']

for character in characters:
    count = f'''
        SELECT
            COUNT (*)
        From charactercreator_{character}
    '''
    count = cursor.execute(count).fetchall()
    print(f'{character}:', count[0][0])

# How many total Items? (query)
item_count = '''
    SELECT
	    COUNT (*)
    FROM armory_item
    '''

# Execute query and print answer
result2 = cursor.execute(item_count).fetchall()
print('\nHow many total Items?', result2[0][0])

# How many of the Items are weapons? (query)
weapon_count = '''
    SELECT
	    COUNT (*)
    FROM armory_weapon
    '''

# Execute weapon_count query and print result;include
# How many are not? with answer.
result3 = cursor.execute(weapon_count).fetchall()
print('\nHow many of the Items are weapons?', result3[0][0], 'How many are not?', 
      result2[0][0]-result3[0][0])


# How many Items does each character have? (Return first 20 rows) (query)
character_item_count = '''
    SELECT
    	name,
    	count(item_Id)
    FROM charactercreator_character
    LEFT JOIN charactercreator_character_inventory on charactercreator_character.character_id = charactercreator_character_inventory.character_id
    group	BY	name
    limit 20;
    '''

# Execute character_item_count query and print result.
result4 = cursor.execute(character_item_count).fetchall()
table = pd.DataFrame(result4, columns=['Character', 'Item Count'])
print('\nFirst 20 characters w/ item count: \n', table)


# How many Weapons does each character have? (Return first 20 rows) (query)

# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?

