# CB 1st Character Statistacal Analyasis

# from character_class import *

import pandas as pd
import matplotlib.pyplot as plt

# define class StatisticalAnalyzer:
    # def __init__():
        # get list of character objects, load into panda dataframes (figure out what that means exactly)
        # use read_csv to load into dataframes

    # define method filter_data():
        # give user multiple options on how to filter data that is loaded into the dataframes, such as by class, race, level, or specific characters
        # use methods such .query(), .drop(), .isin(lists), or straight boolean to change the dataframe before passing it on to the other functions

    # define method roster_statistics():
        # find mean, median, max, and min attributes for all characters in roster
        # maybe find amounts of each class or race as well

    # define method compare_characters(char1,char2):
        # similar to matplotlib comparison, maybe generate charts to compare attributes, then also compare race, class, and level

    # define method creation_trends():
        # see how many of each class there is in the roster, as well as race

class StatiscalAnalyzer:
    def __init__(self,characters,character1,character2):
        self.characters = characters
        self.character1 = character1
        self.character2 = character2

    def filter_data(self):
        for i in self.characters:
            i = vars(i)

        characters_df = pd.DataFrame(self.characters)

        while True:
            print("How would you like to filter the character date?\n1. Name\n2. Race\n3. Class\n4. Level (anything equal to or above level is removed)\n5. Continue to Next Step")
            choice = input("Enter number:\n").strip()

            # clear_screen()

            match choice:
                case '1':
                    name = input("Enter name you want to rmeove from dataset, or enter 'exit' to return to filtering menu:\n").strip().lower()

                    if name == 'exit':
                        continue

                    df = df[name in df['name'].lower()]
                    print("Name removed from dataset.")
                    # after_action
                    continue
                case '2':
                    while True:
                        races = ['Human','Elf','Dwarf','Dragonborn','Gnome','Halfling']
                        for i in races:
                            print(i)

                        race = input("Enter race you want to exclude from dataset, or enter 'exit' to return to filtering menu:\n").strip().capitalize()

                        if race == 'Exit':
                            break

                        if race not in races:
                            print("Please enter one of the displayed character races.")
                            # after_action
                            continue

                        df = df[df['race'].capitalize() == race]
                        print("Race removed from dataset.")
                        # after_action()
                        break

                    continue
                case '3':
                    while True:
                        classes = ['Fighter','Barbarian','Rouge','Wizard','Warlock','Sorcerer','Bard']
                        for i in classes:
                            print(i)

                        char_class = input("Enter class you want to exclude from dataset, or enter 'exit' to return to filtering menu:\n").strip().capitalize()

                        if char_class == 'Exit':
                            break

                        if char_class not in classes:
                            print("Please enter one of the displayed character races.")
                            # after_action
                            continue

                        df = df[df['char_class'].capitalize() == char_class]
                        print("Class removed from dataset.")
                        # after_action()
                        break

                    continue
                case '4':
                     while True:
                        level = input("Enter level between 1 and 20 to remove from dataset (any character with this level or higher will be removed), or enter 'exit' to return to filtering menu:\n").strip().capitalize()

                        if level == 'Exit':
                            break

                        try:
                            level = int(level)
                        except:
                            print("Please enter a numerical value between 1 and 20.")
                            # after_action()
                            continue
                        else:
                            if level > 20 or level < 1:
                                print("Please enter a numerical value between 1 and 20.")
                                # after_action()
                                continue
                        

                        df = df[df['level'].capitalize() >= level]
                        print("Level removed from dataset.")
                        # after_action()
                        break
                     continue
                case '5':
                    return characters_df

    def roster_statistics(self):
        roster_attributes = []
        for i in self.characters:
            roster_attributes.append(i.attributes)

        df = pd.DataFrame(roster_attributes)

        print(df.describe())

        df.boxplot()
        plt.show()

    def compare_characters(self):
        character1_stats = self.character1.attributes
        character1_df = pd.DataFrame(character1_stats)
        character2_stats = self.character2.attributes
        character2_df = pd.DateFrame(character2_stats)

        print(character1_df.describe())
        print(character2_df.describe())

        character1_df.boxplot()

        character2_df.boxplot()

        print(self.character1)
        print(self.character2)

    def creation_trends(self):
        races = []
        classes = []

        for i in self.characters:
            races.append(i.race)
            classes.append(i.char_class)

        races_df = pd.DataFrame({"Race": races})
        classes_df = pd.DataFrame({"Class": classes})

        races_mode = races_df["Race"].mode()
        classes_mode = classes_df["Class"].mode()

        print(f"Most commmon race: {races_mode}")
        print(f"Most common class: {classes_mode}")

        print("To see stat averages, look at roster statistics.")
        # after_action()
        return

