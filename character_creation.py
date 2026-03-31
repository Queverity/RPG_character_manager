# CB 1st Character Manager Pseudocode
# characters = ({"Name":"Example", "Class":"Example", "Level":1, "Stats":{"Stat1":Example Num}, "Skills":{"Skill_name":"Skill_desc"}, "Inventory":{"Item_name":"Item_desc"}})

# skills_list = []

# classes_list = []

# define function create_character():
    # new_character = {}
    # stats_dictionary = {"Strength":10,"Dexterity":10,"Constitution":10,"Wisdom":10,"Intelligence":10,"Charisma":10} (Note: These are just placeholders)
    # skills_dictionary = {}
    # while True:
        # ask user for character name
        # save character name in a variable
        # have user choose race (human, elf, dwarf, gnome,dragonborn,halfling)
        # have user set level
        # ask user if these choices are okay, display name choice and race choice
        # if yes:
            # append character name and level to new_character dictionary
            # apply race based attribute bonuses to attributes dictionary
            # break
        # if no:
            # continue
    # while True:
        # ask user to enter attributes (use a for loop)
        # if an attribute is bigger than 20:
            # tell user to enter a different thing that is less than 20
        # once user has entered all their attributes:
            # display attributes
            # ask if these are okay
            # if yes:
                # Set stats_dictionary attributes
                # break
            # if no:
                # reset attributes
                # continue
    # while True:
        # ask user to choose class (display list of available classes based off of attributes)
        # ask user if this choice is okay (display class choice)
        # if yes:
            # break
        # if no:
            # continue
    # while True:
        # ask user to choose skills (combat, support, misc) available skills are based off of attributes
        # once user has chosen as many skills as their level is, ask if these choices are okay
        # if yes:
            # break
        # if no:
            # reset skills
            # continue

# define function level_up():
    # while True:
        # ask user if they want a stat boost or a new skill
        # if stat:
            # have user choose a stat to add 1 to
            # if that stat would go over 20:
                # have user choose a different stat
            #else:

                # break
        # if skill:
            # have user choose a skill to gain that they don't already have
            # break

# define function manage_inspect():
    # while True:
        # display Name, Race, Level, and Class of inspected character
        # ask user if they want to change character name or level
        # if Name:
            # have user enter new name for character
            # ask user if they want to continue changing stuff
            # if yes:
                # continue
            # if no:
                # return to character inspect menu
        # if Level:
            # have user set new level that is higher then current level
            # if new level <= current level:
                # tell user to set a different level
            # else:
                # per new level:
                    # run level_up() function


characters = {  
                "Name":{
                    "Race":("Example"), 
                    "Class":("Example"), 
                    "Level":1, 
                    "Stats":{"Stat1":"Example Num"}, 
                    "Skills":{"Skill_name":"Skill_desc"}, 
                    "Inventory":{"Item_name":"Item_desc"},}}

species_list = ["Human (+2 to Consitution)","Elf (+2 to Wisdom)","Dwarf (+2 to Strength)","Gnome (+2 to Intelligence)","Dragonborn (+2 to Dexterity)","Halfling (+2 to Charisma)"]
actual_species_list = ["Human","Elf","Dwarf","Gnome","Dragonborn","Halfling"]
stats_list = ["Strength","Dexterity","Constitution","Wisdom","Intelligence","Charisma"]

def create_character_stepone(species_list):
    new_character = {}
    new_stats = {"Strength":0,"Dexterity":0,"Constitution":0,"Wisdom":0,"Intelligence":0,"Charisma":0}
    while True:
        print()
        name = input("What will the name of your character be?").strip()
        print()
        check = input(f"Are you sure you want {name} to be your character's name? Y/N").strip().capitalize()
        if check == "Y":
            new_character["Name"] = name
            break
        else:
            continue

    while True:
        print()
        print("Available Races")
        count = 0
        for i in species_list:
            count += 1
            print(f"{count}. {i}")
        print()
        race = input("What will the race of your character be?").strip().capitalize()
        if race not in actual_species_list:
            print()
            print("Invalid answer")
        else:
            print()
            check = input(f"Are you sure you want {name} to be a {race}? It cannot be changed later. Y/N").strip().capitalize()
            if check == "Y":
                race = tuple(race)
                new_character["Race"] = race
                match race:
                    case "Human":
                        new_stats["Constitution"] += 2
                    case "Elf":
                        new_stats["Wisdom"] += 2
                    case "Dwarf":
                        new_stats["Strength"] += 2
                    case "Gnome":
                        new_stats["Intelligence"] += 2
                    case "Dragonborn":
                        new_stats["Dexterity"] += 2
                    case "Halfling":
                        new_stats["Charisma"] += 2
                break
            else:
                continue
    while True:
        for i in stats_list:
            while True:
                print()
                stat = input(f"What do you want your base stat for {i} to be?")
                if stat.isnumeric() == False:
                    print()
                    print("Invalid answer")
                    continue
                else:
                    stat = int(stat)
                    final_stat = new_stats[i] + stat
                    if final_stat > 20:
                        print()
                        print("That would make the stat go over 20. Please enter a lower number.")
                        continue
                    else:
                        check = input(f"{i}: {final_stat}. Are you sure this is what you want? Y/N").strip().capitalize()
                        if check == "Y":
                            new_stats[i] = final_stat
                            break
                        else:
                            continue
        new_character["Stats"] = new_stats
        break
    available_classes = []
    if new_stats["Charisma"] >= 13:
        available_classes.append("Bard")
    if new_stats["Constitution"] >= 13:
        available_classes.append("Barbarian")        
    if new_stats["Dexterity"] >= 13:
        available_classes.append("Rouge")
    if new_stats["Wisdom"] >= 13:
        available_classes.append("Wizard")
    if new_stats["Strength"] >= 13:
        available_classes.append("Fighter")
    if new_stats["Intelligence"] >= 13:
        available_classes.append("Sorcerer")  
    print()
    print("Available Classes:")
    for i in available_classes:
        print(i)
    while True:
        print()
        class_choice = input("What class do you want to take?").strip().capitalize()
        if class_choice not in available_classes:
            print()
            print("Invalid answer")
        else:
            print()
            check = input(f"Are you sure you want to take {class_choice} as your class? Y/N").strip().capitalize()
            if check == "Y":
                new_character["Class"] = class_choice
                break
            else:
                continue
    print()
    print(new_character)
    
def manage_inspect(characters,character_name):
    while True:
        print()
        print(f"Name: {character_name}\nClass: {characters[character_name]["Class"]}\nRace: {characters[character_name]["Race"]}\nLevel: {characters[character_name]["Level"]}")
        print()
        change = input("Would you like to change character name or level? Y/N").strip().capitalize()
        if change == "N":
            # We'll need something here to go back to the character inspect menu
            break
        else:
            print()
            item_to_change = input("Select item to change [Enter Number]\n1. Name\n2. Level\n3. Go Back").strip()
            if item_to_change ==  "1":
                while True:
                    print()
                    new_name = input("Enter the character's new name. Type 'Exit' to go back.").strip()
                    if new_name == "exit" or new_name == "Exit":
                        break
                    else:
                        print()
                        check = input(f"Are you sure you want {new_name} to be your character's name? Y/N").strip().capitalize()
                        if check == "Y":
                            # figure out how to change key of a dictoinray
                            # characters[character_name.keys()] = new_name
                            characters[new_name] = characters.pop(character_name)
                            character_name = new_name
                            break
                        else:
                            continue
            if item_to_change == "2":
                while True:
                    print()
                    new_level = input(f"Current Level: {characters[character_name]["Level"]}\n What do you want your new level to be? You cannot set it to a lower number, and it cannot go above 20. Type 'Exit' to go back.").strip().capitalize()
                    if new_level == "Exit":
                        break
                    elif new_level.isnumeric() is False or int(new_level) > 20 or int(new_level) <= characters[character_name]["Level"]:
                        print()
                        print("Invalid answer")
                    else:
                        print()
                        check = input(f"Are you sure you want to set your character's level to {new_level}? Y/N").strip().capitalize()
                        if check == "Y":
                            old_level = characters[character_name]["Level"]
                            characters[character_name]["Level"] = new_level
                            # for _ in range(old_level):
                                # level_up()
                            break
            if item_to_change == "3":
                pass
            print()
            continue_inspect = input("Do you want to change something else? Y/N").strip().capitalize()
            if continue_inspect == "Y":
                continue
            else:
                break



manage_inspect(characters,"Name")