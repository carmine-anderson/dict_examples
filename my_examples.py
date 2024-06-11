"""Examples of Dictionaries in Use, and the integration of for loops to mutate or change dictionaries."""

###
# Like I said, Dictionaries are literally built like its name. there is something, and then a value that it holds
# Just like a dictionary for words, there is a word, and then a definition of that word.
###
"-----------------------------------------------------------------------------------------------------------------"
###
# If we go ahead and define a dictionary with strings as keys and integers as values, to create that key value pair, 
# It will look like the following:

# First way:
my_dict_1: dict[str, int] = {}

# Alternative way:
my_dictionary: dict[str, int] = dict()

# The above dictionary is initialized as empty, just like you can do as lists, we can also preset the dictionary as well,

my_dict_2: dict[str, int] = {"Hello": 1, "Guys": 2}

# Printing these will result in an empty dictionary and then another dictionary with key value pairs.

print(f"{my_dict_1} <- Empty Dictionary, and Instantiated Dictionary -> {my_dict_2}")
###
"-----------------------------------------------------------------------------------------------------------------"
print("\n")
###
# We can also mutate these dictionaries by adding new key value pairs
# This is done by calling the 'dictionary_name[key_you_choose] = value you choose', this can be seen below:
my_dict_1["Howdy"] = 1738

# Now printing we can see the updated dictionary 1 with a key of "howdy" and a value associated to that key of 1738
print(my_dict_1)
###
"-----------------------------------------------------------------------------------------------------------------"
print("\n")
###
# The following is a use of how to remove a key value pair in a dictionary using the pop built in method:
my_dict_2.pop("Hello")
# Now printing this dictionary will prove that the first key value pair of {"Hello": 1}
# Was entirely removed from the existing dictionary.
print(my_dict_2)
###
"-----------------------------------------------------------------------------------------------------------------"
print("\n")
###
# You can use the if in keywords to check if there is a certain key in a dictionary already
new_dictionary_1: dict[str, int] = {"Stop": 1, "Go": 2}
# We can use the if in keyword to mutate the dictionary, 
# such as adding to the values at a certain key if it exists:
print(new_dictionary_1)

if "Stop" in new_dictionary_1:
    new_dictionary_1["Stop"] += 29

print(new_dictionary_1)
# Now you can see this change visibly
###
"-----------------------------------------------------------------------------------------------------------------"
print("\n")

###
# Practice from slides:
in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}
# Printing all the keys where the values are True would look like the following:
for key in in_stock:
    if in_stock[key]: # This statement is basically saying, if the dictionary at the key is True (if True)
        print(key)
###
"-----------------------------------------------------------------------------------------------------------------"
print("\n")

###################################
# HUGE EXAMPLE OF DICTIONARY USAGE:
# There exists a game where players collect watermelons.
# Below is the dictionary containing how many watermelons were collected by each player.
players: dict[str, float] = {"Ronald": 1.0, "Alyssa": 3.5, "Carmine": 5.0}

print(players)
# Say we wanted to know who won the game (aka: who collected the most)
max: float = 0.0

for key in players:
    if players[key] > max:
        max = players[key]

for player in players:
    if players[player] == max:
        print(player)

### You can also do this in one step
max = 0.0
winning_player: str = ""
for person in players:
    if players[person] > max:
        max = players[person]
        winning_player = person

print(winning_player, max)

"-----------------------------------------------------------------------------------------------------------------"
print("\n")
# Say Alyssa, got a little sneaky and cheated in the game, and collected a watermelon after time ran out:
# Instead of disqualifying her from the tournament, we remove 1 and a half watermelons from her score, 
# and create a new score board (dictionary) after removing 1.5 watermelons from her score.
updated_players: dict[str, float] = players # making a copy
updated_players["Alyssa"] -= 1.5
print(updated_players)
# Now you can see that Alyssa's value changed from 3.5 to 2.0

"-----------------------------------------------------------------------------------------------------------------"
print("\n")
# Lets say Carmine decided to cheat the entire game, and do nothing and had someone give him watermelons in secret.
# This calls for disqualification, lets remove him from the original scoreboard and create a new one
updated_players_without_carmine: dict[str, float] = players # Again making a copy
updated_players_without_carmine.pop("Carmine")
print(updated_players_without_carmine)
# Now you can see that Carmine doesn't appear on the new scoreboard, and thats why you don't cheat.
###################################