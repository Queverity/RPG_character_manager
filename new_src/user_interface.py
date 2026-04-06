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

# define function comparison_menu():
    # use functions from both Stats class and Data Vis class that compare characters
    # display avaiable actions, ask user what they want to do

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

def choose_characters(characters,mode):

    if bool(characters) == False:
        print("You have no characters currently saved.")
        after_action()
        return "No"

    for i in characters:
        print(i)

    if mode == 1:
        while True:
            character = input("Enter ID of character you want:\n").strip().upper()

            for i in characters:
                if i.id.upper() == character:
                    character = i
                    return character
                else:
                    pass

            print("Please enter a valid ID.")
            # after_action
            continue

    elif mode == 2:
        while True:
            character1 = input("Enter ID of the first character you want:\n").strip().upper()

            found = False
            for i in characters:
                if i.id.upper() == character1:
                    character1 = i
                    found = True
                    break
                else:
                    pass

            if found == True:
                break

            print("Please enter a valid ID.")
            # after_action()
            continue
        
        while True:
            character2 = input("Enter ID of the second character you want:\n").strip().upper()

            for i in characters:
                if i.id.upper() == character2:
                    character2 = i
                    return character1, character2
                else:
                    pass

            print("Please enter a valid ID.")
            # after_action()
            continue

    else:
        print("Unexpected error; Mode is not 1 or 2")
        # after_action()
        return
    
def character_visualisation(characters):
    char = choose_characters(characters,1)

    if char == "No":
        return

    visualizer = DataVisulisation(char,"N/A")
    print("Generating stats chart...")
    visualizer.single_plt()
    print("Chart generated!")
    # after_action()
    return


def stats_analyze(characters):
    analyzer = StatiscalAnalyzer(characters,"N/A","N/A")
    while True:
        print("Whwat would you like to do?\n[1] View Roster Statistics Data\n[2] View Creation Trends and Popular Builds\n[R] Return to Main Menu")
        choice = input("Enter choice:\n").strip().capitalize()

        # clear_screen()

        match choice:
            case '1':
                print("Generating roster data chart...")
                analyzer.roster_statistics()
                print("Succesfully generated!")
                # after_action()
                continue
            case '2':
                print("Generating creation trends...")
                analyzer.creation_trends()
                print("Succesfully generated!")
                # after_action()
                continue
            case 'R':
                return
            case _:
                print("Please enter one of the displayed options.")
                # after_action
                continue

def character_comparison(characters):
    char1,char2 = choose_characters(characters,2)

    if char1 == "No" or char2 == "No":
        return

    visualizer = DataVisulisation(char1,char2)
    analyzer = StatiscalAnalyzer(characters,char1,char2)

    while True:
        print("What would you like to do?\n[1] Visulize & Compare Character Stats\n[2] Statiscally Analyze and Compare Characters\n[R] Return to Main Menu")

        choice = input("Enter choice:\n").strip().upper()

        # clear_screen()

        match choice:
            case '1':
                print("Generating comparison chart...")
                visualizer.comparison_plt()
                print("Succesfully generated!")
                # after_action()
                continue
            case '2':
                print("Generating chart & data...")
                analyzer.compare_characters()
                print("Succesfully generated!")
                # after_action()
                continue
            case 'R':
                return
            case _:
                print("Please enter one of the displayed options.")

def generator_menu(characters):
    generator = RandomGenerator(characters)
    print("Welcome to the Random Generation Menu! Here, you can randomly generate characters and quests. You can't have anything preset, because I didn't feel like coding it. Sorry.")

    while True:
        # clear_screen
        print("What would you like to do?\n[1] Generate Character\n[2] Generate Quest\n[R] Return to Main Menu")
        mode = input("Enter choice:\n").strip().upper()

        # clear_screen()

        match mode:
            case '1':
                character_object = generator.generate_character()
                characters.append(character_object)
                continue
            case '2':
                generator.generate_quest()
                continue
            case 'R':
                break
            case _:
                print("Please enter one of the display choices.")
                # after_action()
                continue

    return characters  
    
def inspect_character(characters,skills,items):
    char = choose_characters(characters,1)

    if char == "No":
        return

    while True:
        print(f"How would you like to inspect/manage {char.name}?\n[1] Inspect Inventory\n[2] Inspect Skills\n[3] Inspect Stats\n[4] Inspect Basic Details\n\n[R] Return to Main Menu")

        choice = input("Enter choice:\n").strip().capitalize()

        # clear_screen

        match choice:
            case '1':
                char.edit_inventory(items)
                continue
            case '2':
                char.edit_skills(skills)
            case '3':
                char.display_stats()
                continue
            case '4':
                while True:
                    # clear_screen()
                    print(char)
                    print("What would you like to do?\n[1] Change Character Name\n[2] Change Character Level\n[R] Return to Character Inspection Menu")

                    choice = input("Enter choice:\n").strip().upper()

                    # clear_screen()

                    match choice:
                        case '1':
                            while True:
                                new_name = input("Enter new name for character, or enter 'exit' to return to Basic Details Menu:\n").strip()
                                if new_name.lower() == exit:
                                    
                                    break

                                if new_name.lower() == char.name:
                                    print("That is the current name of your character.")
                                    # after_action
                                    continue

                                char.name = new_name
                                print("Name changed succesfully.")
                                # after_action
                                break
                            continue
                        case '2':
                            while True:
                                print(f"Current Character Level: {char.level}")
                                print("Note: You can only increase the character level.")
                                new_level = input("Enter new level for character (cannot be above 20), or enter 'exit' to return to Basic Details Menu:\n").strip()

                                if new_level.lower() == 'exit':
                                    break

                                try:
                                    new_level = int(new_level)
                                except:
                                    print("Please enter an actual number for the character level.")
                                    # after_action
                                else:
                                    if new_level <= int(char.level) or new_level > 20:
                                        print("That is either less than or equal the current level of your character, or it is above 20.")
                                        # after_action()
                                    
                                    level_difference = new_level - char.level
                                    char.level = new_level
                                    print("Level increased succesfully.")

                                while level_difference != 0:
                                    char.level_up()
                                    level_different -= 1
                                
                                break
                            continue
                        case 'R':
                            break
                
                continue

            case 'R':
                return
            case _:
                print("Please enter of the displayed options.")
                # after_action()
                continue
    
def main_menu():
    print("Loading...")
    characters_csv = load_characters()
    skills_csv = load_skills()
    items_csv = load_items()

    characters = create_character_objects(characters_csv)
    skills = load_skill_objects(skills_csv)
    items = load_item_objects(items_csv)


    print("Welcome to the Enhanced RPG Character Manager. Using this program, you can create characters, save characters, compare them, statistically analyze them, and do much, much more! You are also givne the ability to randomly generate characters, as well as quests! Note: This is not a game in itself. It is a program intended to hold characters for different games.")



    while True:
        clear_screen()
        print("What would you like to do?\nCHARACTER FEATURES\n[1] Create Character\n[2] Inspect Character\n[3] Random Generator\n\nDATA & ANALYSIS\n[4] Visualize Character Stats\n[5] Statistical Analysis\n[6] Character Comparison Tools\n\nSKILL AND ITEM MANAGEMENT\n[7] Add Skill to Database\n[8] Add Item to Database\n\nDATA MANAGEMENT\n[9] Save Current Characters\n\n[Q] Quit")

        choice = input("Enter choice:\n").strip().capitalize()

        clear_screen()

        match choice:
            case '1':
                character_object = create_character(characters)
                characters.append(character_object)
            case '2':
                inspect_character(characters,skills,items)
                continue
            case '3':
                characters = generator_menu(characters)
                continue
            case '4':
                character_visualisation(characters)
                continue
            case '5':
                stats_analyze(characters)
                continue
            case '6':
                character_comparison(characters)
                continue
            case '7':
                items = create_item(items)
                continue
            case '8':
                skills = create_skill(skills)
                continue
            case '9':
                save_characters(characters)
                print("Character databse saved.")
                after_action()
                continue
            case 'Q':
                check = input("Any unsaved data will be lost. Are you sure you want to quit? Y/N:\n").strip().upper()
                if check != "Y":
                    continue
                else:
                    print("Goodbye!")
                    break
            case _:
                print("Please enter one of the displayed options.")
                after_action()
                continue