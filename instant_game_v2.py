import random
import json
'''
Ok, this has been updated, and it's not perfect, but it is now saving the generated game in the JSON file.
is that the right way? probably not. but it's doing something now that it wasn't before.

NEW UPDATE TO WORK ON - note added 2/6/23
OOP to create this random game
class
    method
    return

'''


# the dict to hold the data to save for backup_data.txt file
backup_data = {}

# Getting a random Setting
def roll_settings(file_name):
    with open(file_name, "r") as settings:
        setting_list = settings.read().split("\n")
        return(random.choice(setting_list))

# Getting a random Place
def roll_places(file_name):
    with open(file_name, "r") as places:
        places_list = places.read().split("\n")
        return(random.choice(places_list))

# Getting a random population
def roll_pop(file_name):
    with open(file_name, "r") as population:
        population_list = population.read().split("\n")
        return(random.choice(population_list))

# Getting a random tone 
def roll_tone(file_name):
    with open(file_name, "r") as tones:
        tone_list = tones.read().split("\n")
        return(random.choice(tone_list))

# Getting a random thing
def roll_thing1(file_name):
    with open(file_name, "r") as things1:
        things1_list = things1.read().split("\n")
        return(random.choice(things1_list))

# Getting a random other thing 
def roll_other_thing(file_name):
    with open(file_name, "r") as other_thing:
        other_thing_list = other_thing.read().split("\n")
        return(random.choice(other_thing_list))

# Getting a random opposition (for the plot)
def roll_opposition(file_name):
    with open(file_name, "r") as opposition:
        opposition_list = opposition.read().split("\n")
        return(random.choice(opposition_list))

#Getting a random action
def roll_action(file_name):
    with open(file_name, "r") as action:
        action_list = action.read().split("\n")
        return(random.choice(action_list))

# Getting a random technology level
def roll_tech(file_name):
    with open(file_name, "r") as tech:
        tech_list = tech.read().split("\n")
        return(random.choice(tech_list))

# Getting random descriptors        
def roll_descriptors(file_name):
    with open(file_name, "r") as descriptors:
        descriptors_list = descriptors.read().split("\n")
        return(random.choice(descriptors_list))

# Getting the Instant Game Setting
def rolling_the_setting(settings_file, tones_file, places_file, descriptors_file, things1_file, tech_file, population_file):
    instant_game_setting = {}
    instant_game_setting["Your setting"] = roll_settings(settings_file)
    instant_game_setting["Setting tone"] = roll_tone(tones_file)
    instant_game_setting["Some places to include"] = roll_places(places_file) + ", " + roll_places(places_file)
    instant_game_setting["Two things to influence your world"] = roll_descriptors(descriptors_file) + " " + roll_thing1(things1_file) + " & " + roll_descriptors(descriptors_file) + " " + roll_thing1(things1_file)
    instant_game_setting["(This is optional) Tech level"] = roll_tech(tech_file)
    instant_game_setting["(This is optional) Population"] = roll_pop(population_file)
    for key, value in instant_game_setting.items():
        print(key + ": " + value)
    return instant_game_setting

# Getting the Instant Game Plot
#Creating a dictionary for the plot - KEY: Value (oppostion:value, prompt1:action & desc. thing1, prompt2:action & desc. thing2)
def rolling_the_plot(opposition_file, actions_file, descriptors_file, things1_file, things2_file):
    instant_game_plot = {}
    instant_game_plot["Here is your main opposition"] = roll_opposition(opposition_file)
    instant_game_plot["Here are some prompts"] = roll_action(actions_file) + " & " + roll_descriptors(descriptors_file) + " " + roll_thing1(things1_file)
    instant_game_plot["Here's another prompt"] = roll_action(actions_file) + " & " + roll_descriptors(descriptors_file) + " " + roll_other_thing(things2_file)
    for key, value in instant_game_plot.items():
        print(key + ": " + value)
    return instant_game_plot

#convert to json
#def convert_to_json():
    json_backup = json.dumps(backup_data)
    return json_backup

#store backup data
#def write_game_backup(backup_data):
    with open("backup_data.json", "w") as json_backup_file:
        json.dump(backup_data, json_backup_file)

#main function
def main():
    print("Creating an Instant Game!")
    backup_data.update(rolling_the_setting("settings.txt", "tones.txt", "places.txt", "descriptors.txt", "things1.txt", "tech.txt", "population.txt"))
    print("Here are the bare bones of the plot: ")
    backup_data.update(rolling_the_plot("opposition.txt", "actions.txt", "descriptors.txt", "things1.txt", "things2.txt"))
    json_backup_file = json.dumps(backup_data, indent=4)
    with open("backup_data.json", "a") as outfile:
        outfile.write(json_backup_file)
        outfile.write("," + "\n")
#    write_game_backup(json_backup_file)

main()