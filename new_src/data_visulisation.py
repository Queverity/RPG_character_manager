# CB 1st Data Visualisation

# use matplotlib for this

import matplotlib.pyplot as plt
import numpy as np


# class DataVisulisation():
    # def __init__:
        # for a matplotlib bar chart, we'll need a list of values (attributes), our categories (attribute names), and maybe a few other things
        # we'll need to be able to generate charts with the attributes of two character side by side (maybe attach a color to each character)

    # def single_plt():
        # take attribute information from a single character, generate a bar graph to display it, and return that bar graph

    # def comparison_plt():
        # take attribute information from two characters, generate a bar graph with each attribute side by side, assign a color to each character so it is readable, and return that bar graph

class DataVisulisation:
    def __init__(self,character1,character2):
        self.categories = ['Strength','Dexterity','Constitution','Wisdom','Intelligence','Charisma']
        self.character1 = character1
        self.character2 = character2

    def single_plt(self):
        plt.bar(self.categories,list(self.character1.attributes.values()))

        plt.xlabel('Stats')
        plt.ylabel('Value')

        plt.show()

    def comparison_plt(self):
        # 1. Prepare data
        categories = ['Str','Dex','Con','Int','Wis','Rizz']
        stats1 = list(self.character1.attributes.values())
        stats2 = list(self.character2.attributes.values())

        x = np.arange(len(categories))  # Base label locations
        width = 0.35               # Width of each individual bar

        fig, ax = plt.subplots()

        # 2. Plot bars with offsets
        # Subtract half width for the first group, add for the second
        rects1 = ax.bar(x - width/2, stats1, width, label=self.character1.name)
        rects2 = ax.bar(x + width/2, stats2, width, label=self.character2.name)

        # 3. Add labels and legend
        ax.set_ylabel('Stat Value')
        ax.set_title('Chararacter Stats Compared')
        ax.set_xticks(x)
        ax.set_xticklabels(categories)
        ax.legend()

        # 4. Optional: Add bar labels (requires Matplotlib 3.4+)
        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        plt.show()


