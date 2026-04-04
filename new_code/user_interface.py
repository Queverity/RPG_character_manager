# CB 1st User Interface

from character_class import *
from data_visulisation import *
from item_class import *
from random_generator import *
from saving_parsing import *
from skill_class import *
from statistacal_analysis import *


# define function visulalisation_menu():
    # ask user what they would like to visualize (single character stats [bar chart, radar chart], compare characters, stuff like that)
    # if compare characters, have user choose two seperate characters, visulalize stats and also print out a few other things
    # if single character, visualize character stats

# define function stat_analyze_menu():
    # ask user what statistical analyze function that would like to perform (roster stats, character comparison, character creation trends/popular builds, stuff like that)
    # take user input

    # call reqiusite function from statistical analysis class


# define function generator_menu():
    # connect this to the random generator thing that is using faker
    # have user choose what to generate (character or quest)
    # if quest, ask user if there is anything they want to preset (location, names, stuff like that)
    # generate quest using input information, and return

    # if character, have user choose any preset items if they want to (class, race, name, etc.)
    # generate character object based off of input information, display user (for inventory and skills, just pick randomly from available things)

# define function inspect_character(character_object):
    # this will lbe for viewing a single character
    # give user a few options on how to inspect character (inventory, attributes, skills, character details)
    # match-case uesr input
    # if inventory, show user inventory, give options to add/remove items from inventory
        # if add, make sure inventory is not full, then see what items user could add (load class items and items marked all, then remove items user already has)
        # have user choose what item they want to add, or exit
        # if remove, make sure inventory is not empty, then see what items are in user inventory
        # have user choose item by ID, then remove item

    # if attributes, give user a few options on what to do with attributes, and how to view (bar graphs, stuff like that, call data visualisation class)

    # if skills, show skill list, give options to add/remove skills
        # if add, make sure all skill slots aren't already taken, then see what skills user can get (load class skills and skills marked all from skill class, then remove skills user already has)
            # have user choose what skill they want to add via ID
        # if remove, make sure all skill slots aren't empty, then display skills in user skill list
            # have user choose skill via ID

    # if character details, show name, race, class, and level
        # ask user if they would like to change name or level (if change level, make sure skill slots are increased appropiately)


# define function main_menu():
    # whlie True:
        # give user options to view characters, stat analyze characters, visualize character attributes, compare characters, create a character, generate a character, and a few more (also save characters, though I might do that automatically)
def inspect_character(characters,skills,items):
    for i in characters:
                print(i)

                id = input("Enter ID of character you want to inspect:\n").strip().upper()

                found = False
                # clear_screen()

                for char in characters:
                    if char.id.upper() == id:
                        found = True
                        print(f"How would you like to inspect/manage {char.name}?\n[1] Inspect Inventory\n[2] Inspect Skills\n[3] Inspect Stats\n[4] Inspect Basic Details\n\n[R] Return to Main Menu")

                        choice = input("Enter choice:\n").strip().capitalize()

                        match choice:
                            case '1':
                                char.edit_inventory(items)
                                continue
                            case '2':
                                char.edit_skills(skills)
                            case '3':
                                pass
                            case '4':
                                pass
                            case 'R':
                                return
                            case _:
                                print("Please enter of the displayed options.")
                                # after_action()
                                continue
    
def main_menu():
    characters_csv = load_characters()
    skills_csv = load_skills()
    items_csv = load_items()

    characters = create_character_objects(characters_csv)
    skills = load_skills(skills_csv)
    items = load_items(items_csv)


    print("Welcome to the Enhanced RPG Character Manager. Using this program, you can create characters, save characters, compare them, statistically analyze them, and do much, much more! You are also givne the ability to randomly generate characters, as well as quests! Note: This is not a game in itself. It is a program intended to hold characters for different games.")



    while True:
        print("What would you like to do?\nCHARACTER FEATURES\n[1] Create Character\n[2] Inspect Character\n[3] Random Generator\n\nDATA & ANALYSIS\n[4] Character Visualisation\n[5] Statistical Analysis\n[6] Character Comparison Tools\n\nSKILL AND ITEM MANAGEMENT\n[7] Add Skill to Database\n[8] Add Item to Database\n\nDATA MANAGEMENT\n[9] Save Current Characters\n\n[Q] Quit")

        choice = input("Enter choice:\n").strip().capitalize()

        # clear_screen

        match choice:
            case '1':
                character_object = create_character(characters)
                characters.append(character_object)
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                pass
            case '7':
                pass
            case '8':
                pass
            case '9':
                pass
            case 'Q':
                pass
            case _:
                print("Please enter one of the displayed options.")
                # after_action()
                continue