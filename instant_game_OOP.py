import random
import json

class RandomRoll:
    def __init__(self, file_name):
        self.file_name = file_name

    def roll(self):
        with open(self.file_name, "r") as f:
            data = f.read().split("\n")
            return random.choice(data)

class GameSetting:
    def __init__(self, settings_file, tones_file, places_file, descriptors_file, things1_file, tech_file, population_file):
        self.setting = RandomRoll(settings_file).roll()
        self.tone = RandomRoll(tones_file).roll()
        self.places = RandomRoll(places_file).roll() + ", " + RandomRoll(places_file).roll()
        self.things = RandomRoll(descriptors_file).roll() + " " + RandomRoll(things1_file).roll() + " & " + RandomRoll(descriptors_file).roll() + " " + RandomRoll(things1_file).roll()
        self.tech = RandomRoll(tech_file).roll()
        self.population = RandomRoll(population_file).roll()
    
    def get_setting(self):
        return {
            "Your setting": self.setting,
            "Setting tone": self.tone,
            "Some places to include": self.places,
            "Two things to influence your world": self.things,
            "(This is optional) Tech level": self.tech,
            "(This is optional) Population": self.population
        }

class GamePlot:
    def __init__(self, opposition_file, actions_file, descriptors_file, things1_file, things2_file):
        self.opposition = RandomRoll(opposition_file).roll()
        self.prompt1 = RandomRoll(actions_file).roll() + " & " + RandomRoll(descriptors_file).roll() + " " + RandomRoll(things1_file).roll()
        self.prompt2 = RandomRoll(actions_file).roll() + " & " + RandomRoll(descriptors_file).roll() + " " + RandomRoll(things2_file).roll()
    
    def get_plot(self):
        return {
            "Here is your main opposition": self.opposition,
            "Here are some prompts": self.prompt1,
            "Here's another prompt": self.prompt2
        }

class Generate_Game:
    def rolling_the_game(self):
        setting = GameSetting("settings.txt", "tones.txt", "places.txt", "descriptors.txt", "things1.txt", "tech.txt", "population.txt")
        print(setting.get_setting())
        plot = GamePlot("opposition.txt", "actions.txt", "descriptors.txt", "things1.txt", "things2.txt")
        print(plot.get_plot())
        return setting, plot

    def backup_results(self, setting, plot, filename):
        results = {
            "setting": setting.get_setting(),
            "plot": plot.get_plot()
        }
        with open(filename, "a+") as f:
            json.dump(results, f, indent=4)
            f.write("\n")

if __name__ == "__main__":
    game = Generate_Game()
    results = game.rolling_the_game()
    game.backup_results(*results, "results.json")

'''
For future development
MongoDB will be a good database to manage the JSON files created. 
Would it be best to create a new file every time?
WHO KNOWS
FIND OUT NEXT WEEK ON
"daleth tries to learn how to code by himself with this game again"

'''

'''
Ok. so this was much more clean and easy to read/understand and faster of code.
OOP was the way to go.
And it helps to understand the classes and calling functions better.
And you don't need to write essentially the same function repeatedly to do the same thing over and over again.


'''

'''
# This is me, trying to write this code as OOP paragdigm instead of functional
# Good luck me.

import random
import json

class File_loader:
    def __init__(self, file_name):
        self.file_name = file_name

    def roll_data(self):
        with open(self.file_name, "r") as file:
            data_list = file.read().split("\n")
            return random.choice(data_list)


class Instant_Game_Setting:
    def __init__(self,settings_file, tones_file, places_file, descriptors_file, things1_file, tech_file, population_file):
        self.settings = File_loader(settings_file)
        self.tones = File_loader(tones_file)
        self.places = File_loader(places_file)
        self.descriptors = File_loader(descriptors_file)
        self.things1 = File_loader(things1_file)
        self.tech = File_loader(tech_file)
        self.pop = File_loader(population_file)
    
    def get_setting(self):
        instant_game_setting = {}
        instant_game_setting["Your setting"] = self.settings.roll_data()
        instant_game_setting["Setting tone"] = self.tones.roll_data()
        instant_game_setting["Some places to include"] = self.places.roll_data() + ", " + self.places.roll_data()
        instant_game_setting["Two things to influence your world"] = self.descriptors.roll_data() + " " + self.things1.roll_data() + " & " + self.descriptors.roll_data() + " " + self.things1.roll_data()
        instant_game_setting["(This is optional) Tech level"] = self.tech.roll_data()
        instant_game_setting["(This is optional) Population"] = self.pop.roll_data()
        for key, value in instant_game_setting.items():
            print(key + ": " + value)
        return instant_game_setting

class Instant_Game_Plot:
    def __init__(self, opposition_file, actions_file, descriptors_file, things1_file, things2_file):
        self.opposition = File_loader(opposition_file)
        self.actions = File_loader(actions_file)
        self.descriptors = File_loader(descriptors_file)
        self.things1 = File_loader(things1_file)
        self.things2 = File_loader(things2_file)
    
    def get_plot(self)
        instant_game_plot = {}
        instant_game_plot["Here is your main opposition"] = self.opposition.roll_data()
        instant_game_plot["Here are some prompts"] = self.actions.roll_data() + " & " + self.descriptors.roll_data() + " " + self.things1.roll_data()
        instant_game_plot["Here's another prompt"] = self.actions.roll_data() + " & " + self.descriptors.roll_data() + " " + self.things2.roll_data()
        for key, value in instant_game_plot.items():
            print(key + ": " + value)
        return instant_game_plot
'''


'''
This is the old code writen in functional programing

# the dict to hold the data to save for backup_data.txt file
import random
import json

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

main()
'''