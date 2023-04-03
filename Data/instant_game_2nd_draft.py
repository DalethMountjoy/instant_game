'''

This is a game setting and plot builder that I wrote myself.
It is based on and the 'Instant Game' by Animalball Game//Animalball Partners.
This was some practice for reading files/creating lists/pulling random selections from those lists.
The data in the .txt files was pulled directly from the Instant Game.

# instant summary
# setting - 1 roll
# tone - 1 roll
# things - 2 rolls

# instant plot/story
# opposition - 1 roll
# action + thing
# action + other thing
'''

''' BELOW IS SOME DRAFT CODE FOR REFERENCE
def turn_file_into_list(file_name):
    with open(file_name, 'r') as list:
        new_list = list.split("\n")
       return new_list

print(random.choice(new_list))

'''
import random

# Getting a random Setting
def roll_settings(file_name):
    with open(file_name, "r") as settings:
        setting_list = settings.read().split("\n")
        return(random.choice(setting_list))
#        return setting_list

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
#        return tone_list

# Getting a random thing
def roll_thing1(file_name):
    with open(file_name, "r") as things1:
        things1_list = things1.read().split("\n")
        return(random.choice(things1_list))
#        return things1_list

# Getting a random other thing 
def roll_other_thing(file_name):
    with open(file_name, "r") as other_thing:
        other_thing_list = other_thing.read().split("\n")
        return(random.choice(other_thing_list))
#        return other_thing_list

# Getting a random opposition (for the plot)
def roll_opposition(file_name):
    with open(file_name, "r") as opposition:
        opposition_list = opposition.read().split("\n")
        return(random.choice(opposition_list))
#        return opposition_list

#Getting a random action
def roll_action(file_name):
    with open(file_name, "r") as action:
        action_list = action.read().split("\n")
        return(random.choice(action_list))
#        return action_list

# Getting a random technology level
def roll_tech(file_name):
    with open(file_name, "r") as tech:
        tech_list = tech.read().split("\n")
        return(random.choice(tech_list))
#        return tech_list

# Getting random descriptors        
def roll_descriptors(file_name):
    with open(file_name, "r") as descriptors:
        descriptors_list = descriptors.read().split("\n")
        return(random.choice(descriptors_list))

# writing a function to create a doc to back-up the created games
# def write_game_to_file(instant_game_results, output_filename):
    x = instant_game_results
    with open(output_filename, "w") as instant_game_results:
        instant_game_results.write(x)
    return 

'''
This was the old version of the setting function 

def rolling_the_setting():
    print("Your setting: ")
    roll_settings("settings.txt")
    print("Setting tone: ")
    roll_tone("tones.txt")
    print("Two things to influence your world: ")
    roll_thing1("things1.txt")
    roll_thing1("things1.txt")
    print("Tech level: ")
    roll_tech("tech.txt")
'''
"""# Getting the Setting for the Instant Game
def rolling_the_setting():
    print(("Your setting: "), roll_settings("settings.txt"), sep=" ")
    print(("Setting tone: "), roll_tone("tones.txt"), sep= ' ')
    print(("Some places to include: "), roll_places("places.txt"), roll_places("places.txt"), sep=" ")
    print("Two things to influence your world: ") 
    print(roll_descriptors("descriptors.txt") + " " + roll_thing1("things1.txt") + " & " + roll_descriptors("descriptors.txt") + " " + roll_thing1("things1.txt"))
    print(("(This is optional)"), ("Tech level: "), roll_tech("tech.txt"), sep=" ")
    print(("(This is optional)"), ("Population: "), roll_pop("population.txt"), sep=" ")
    return instant_game_setting

#Getting the Plot for the Instant Game 
def rolling_the_plot():
    print(("Here is your main opposition: "), roll_opposition("opposition.txt"), sep= " ")
    print("Here are some prompts: ")
    print(roll_action("actions.txt") + " & " + roll_descriptors("descriptors.txt") + " " + roll_thing1("things1.txt"))
    print("Here's another prompt: ") 
    print(roll_action("actions.txt") + " & " + roll_descriptors("descriptors.txt") + " " + roll_other_thing("things2.txt"))
    return instant_game_plot

backup_data = []
backup_data.append(rolling_the_setting())
backup_data.append(rolling_the_plot())
"""
#create backup data for storage
# I BELIEVE THE LIST ABOVE DOES THIS ALREADY?
#def create_game_backup(plot, setting):
#    instant_game_results = plot + setting
#    return(instant_game_results)

# writing a function to create a doc to back-up the created games
#def back_up_game_data(plot, setting, output_filname):
#    instant_game_results = plot + setting
#    with open(output_filename, "a") as instant_game_results:
#        instant_game_results.write(instant_game_results)

# def write_game_to_file(instant_game_results, output_filename):
#    x = instant_game_results
#    with open(output_filename, "w") as instant_game_results:
#        instant_game_results.write(x)
#    return 

def rolling_the_setting(settings_file, tones_file, places_file, descriptors_file, things1_file, tech_file, population_file):
    instant_game_setting = {}
    instant_game_setting["Your setting"] = roll_settings(settings_file)
    instant_game_setting["Setting tone"] = roll_tone(tones_file)
    instant_game_setting["Some places to include"] = roll_places(places_file), roll_places(places_file)
    instant_game_setting["Two things to influence your world"] = roll_descriptors(descriptors_file) + " " + roll_thing1(things1_file) + " & " + roll_descriptors(descriptors_file) + " " + roll_thing1(things1_file)
    instant_game_setting["(This is optional) Tech level"] = roll_tech(tech_file)
    instant_game_setting["(This is optional) Population"] = roll_pop(population_file)
    for key, value in instant_game_setting.items():
        print(key, value)
    return instant_game_setting

def rolling_the_plot(opposition_file, actions_file, descriptors_file, things1_file, things2_file):
    instant_game_plot = {}
    instant_game_plot["Here is your main opposition"] = roll_opposition(opposition_file)
    instant_game_plot["Here are some prompts"] = roll_action(actions_file) + " & " + roll_descriptors(descriptors_file) + " " + roll_thing1(things1_file)
    instant_game_plot["Here's another prompt"] = roll_action(actions_file) + " & " + roll_descriptors(descriptors_file) + " " + roll_other_thing(things2_file)
    for key, value in instant_game_plot.items():
        print(key, value)
    return instant_game_plot

backup_data = []
backup_data.append(rolling_the_setting("settings.txt", "tones.txt", "places.txt", "descriptors.txt", "things1.txt", "tech.txt", "population.txt"))
backup_data.append(rolling_the_plot("opposition.txt", "actions.txt", "descriptors.txt", "things1.txt", "things2.txt"))

#store backup data
def write_game_backup(output_filename):
    with open(output_filename, "a") as game_backup:
        game_backup.writelines(backup_data)




#calling the functions (to run the code)
#thius should be main()!!!
def main():
        print("Creating an Instant Game!")
        print()
        rolling_the_setting()
        print()
        print("Here are the bare bones of the plot: ")
        print()
        rolling_the_plot()
#        create_game_backup(rolling_the_setting, rolling_the_plot)
        write_game_backup("backup_data.txt")

main()