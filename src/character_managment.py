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


from skills import skills_available,skill_choice



characters = {
    
}

items = {
    "Rogue_items": {
        "Daggers": {
            "Description": "A pair of daggers that deal 1d4 damage.",
            "Weight": "2 pounds",
            "Value": "5 Gold pieces"
        },
        "Rapier": {
            "Description": "An old European sword with a thin, fast blade that deals 1d8 damage.",
            "Weight": "3 pounds",
            "Value": "25 Gold pieces"
        },
        "Leather Armor": {
            "Description": "Basic leather armor that provides an AC of 11 + Dex Modifier.",
            "Weight": "10 pounds",
            "Value": "10 Gold"
        },
        "Lockpicks": {
            "Description": "A set of lockpicks that can unlock many doors, if you have the skill.",
            "Value": "2 Gold",
            "Weight": "½ pound"
        },
        "Fake ID": {
            "Description": "A fake ID that can get you many places you shouldn’t be.",
            "Value": "Varies",
            "Weight": "Insignificant"
        }
    },

    "Fighter_items": {
        "Greatsword": {
            "Description": "A large two-handed sword ideal for heavy attacks, dealing 2d6 damage.",
            "Weight": "6 pounds",
            "Value": "50 Gold pieces"
        },
        "Poleaxe": {
            "Description": "A versatile weapon with an axe blade, hammer, and spike that deals 1d10 damage.",
            "Weight": "7 pounds",
            "Value": "40 Gold pieces"
        },
        "Chainmail": {
            "Description": "Interlocked metal rings providing solid protection with an AC of 16.",
            "Weight": "20 pounds",
            "Value": "75 Gold"
        },
        "Full Plate": {
            "Description": "Heavy plate armor covering the entire body, providing an AC of 18.",
            "Weight": "50 pounds",
            "Value": "150 Gold"
        },
        "Military Insignia": {
            "Description": "A symbol representing rank and affiliation.",
            "Value": "10 Gold",
            "Weight": "1 pound"
        },
        "Battle Trinket": {
            "Description": "A personal charm carried into battle for luck.",
            "Value": "5 Gold",
            "Weight": "Negligible"
        }
    },

    "Barbarian_items": {
        "Warhammer": {
            "Description": "A heavy hammer designed for crushing armor, dealing 1d8 damage.",
            "Weight": "5 pounds",
            "Value": "30 Gold"
        },
        "Greataxe": {
            "Description": "A massive axe for devastating swings that deals 1d12 damage.",
            "Weight": "7 pounds",
            "Value": "35 Gold"
        },
        "Chainmail": {
            "Description": "Interlocked metal rings providing solid protection with an AC of 16.",
            "Weight": "20 pounds",
            "Value": "75 Gold"
        },
        "Stress Toy": {
            "Description": "Something to make sure the barbarian doesn’t rage during a fine(ish) dinner, or any other situation.",
            "Value": "1 Gold",
            "Weight": "Negligible"
        },
        "Unidentified Blood Vial": {
            "Description": "A vial of blood that the barbarian won’t say where or what it’s from.",
            "Value": "Unknown",
            "Weight": "Negligible"
        }
    },

    "Cleric_items": {
        "Holy Staff": {
            "Description": "A staff imbued with divine power that deals 1d6 damage.",
            "Weight": "4 pounds",
            "Value": "20 Gold"
        },
        "Robes": {
            "Description": "Simple robes that offer minimal protection, providing an AC of 10.",
            "Weight": "3 pounds",
            "Value": "5 Gold"
        },
        "Leather": {
            "Description": "Light leather armor for additional protection, providing an AC of 11 + Dex Modifier.",
            "Weight": "10 pounds",
            "Value": "10 Gold"
        },
        "Holy Symbol": {
            "Description": "A symbol representing the cleric's deity.",
            "Value": "15 Gold",
            "Weight": "1 pound"
        },
        "Scriptures": {
            "Description": "Religious texts for prayer and guidance.",
            "Value": "10 Gold",
            "Weight": "2 pounds"
        }
    },

    "Wizard_items": {
        "Magic Focus": {
            "Description": "An object used to channel magical energy; damage varies by spell.",
            "Weight": "1 pound",
            "Value": "30 Gold"
        },
        "Leather": {
            "Description": "Light armor providing minimal protection with an AC of 11 + Dex Modifier.",
            "Weight": "10 pounds",
            "Value": "10 Gold"
        },
        "Textbooks": {
            "Description": "Books full of spells, theories, and magical research.",
            "Value": "50 Gold",
            "Weight": "10 pounds"
        },
        "Really Cool Hat": {
            "Description": "A really tall wizard’s hat with stars and stuff on it.",
            "Value": "Undetermined",
            "Weight": "1 pound"
        }
    },

    "Bard_items": {
        "Instrument": {
            "Description": "A musical instrument used for performance and magic that can deal 1d4 damage.",
            "Weight": "3 pounds",
            "Value": "25 Gold"
        },
        "Leather Armor": {
            "Description": "Light armor providing minimal protection with an AC of 11 + Dex Modifier.",
            "Weight": "10 pounds",
            "Value": "10 Gold"
        },
        "Chainmail Armor": {
            "Description": "Interlocked metal rings providing solid protection with an AC of 16.",
            "Weight": "20 pounds",
            "Value": "75 Gold"
        },
        "Notepad": {
            "Description": "A book to jot down lyrics, stories, or magical notes.",
            "Value": "2 Gold",
            "Weight": "1 pound"
        },
        "Tuning Fork": {
            "Description": "A tuning fork for the bard’s instrument.",
            "Value": "5 Gold",
            "Weight": "1 pound"
        }
    },

    "General_Items": {
        "Ropes": {
            "Description": "Strong ropes for climbing or tying objects.",
            "Value": "5 Gold",
            "Weight": "5 pounds"
        },
        "Torches": {
            "Description": "Standard torches for lighting dark areas.",
            "Value": "1 Gold",
            "Weight": "1 pound"
        },
        "First-aid kit": {
            "Description": "Basic supplies for treating wounds.",
            "Value": "10 Gold",
            "Weight": "3 pounds"
        },
        "Potions": {
            "Description": "Various potions for healing, mana, or temporary boosts.",
            "Value": "Varies",
            "Weight": "1 pound each"
        },
        "Bedroll": {
            "Description": "A compact roll of bedding for resting outdoors.",
            "Value": "2 Gold",
            "Weight": "4 pounds"
        },
        "Rations": {
            "Description": "Preserved food sufficient for one day.",
            "Value": "1 Gold",
            "Weight": "2 pounds"
        },
        "Waterskin": {
            "Description": "A leather container used to carry drinking water.",
            "Value": "1 Gold",
            "Weight": "1 pound (full)"
        },
        "Backpack": {
            "Description": "A sturdy pack for carrying equipment and supplies.",
            "Value": "3 Gold",
            "Weight": "2 pounds"
        },
        "Flint and Steel": {
            "Description": "Tools used to start fires in the wilderness.",
            "Value": "2 Gold",
            "Weight": "1 pound"
        },
        "Lantern": {
            "Description": "A reusable light source that burns oil for extended illumination.",
            "Value": "7 Gold",
            "Weight": "2 pounds"
        },
        "Oil Flask": {
            "Description": "A small flask of oil used to fuel lanterns or start fires.",
            "Value": "1 Gold",
            "Weight": "1 pound"
        }
    }
}
species_list = ("Human (+2 to Consitution)","Elf (+2 to Wisdom)","Dwarf (+2 to Strength)","Gnome (+2 to Intelligence)","Dragonborn (+2 to Dexterity)","Halfling (+2 to Charisma)")
actual_species_list = ("Human","Elf","Dwarf","Gnome","Dragonborn","Halfling")
stats_list = ("Strength","Dexterity","Constitution","Wisdom","Intelligence","Charisma")
classes_list = ('Bard','Barbarian','Rogue','Cleric','Fighter','Wizard')

def available_items(characters, character_name, items):
    available_items = {}
    character_class = characters[character_name]["Class"]
    # Add general items
    for key in items["General_Items"].keys():
        available_items[key] = items["General_Items"][key]

    # Add class-specific items
    match character_class[0]:
        case "Rogue":
            for key in items["Rogue_items"].keys():
                available_items[key] = items["Rogue_items"][key]

        case "Fighter":
            for key in items["Fighter_items"].keys():
                available_items[key] = items["Fighter_items"][key]

        case "Barbarian":
            for key in items["Barbarian_items"].keys():
                available_items[key] = items["Barbarian_items"][key]

        case "Cleric":
            for key in items["Cleric_items"].keys():
                available_items[key] = items["Cleric_items"][key]

        case "Wizard":
            for key in items["Wizard_items"].keys():
                available_items[key] = items["Wizard_items"][key]

        case "Bard":
            for key in items["Bard_items"].keys():
                available_items[key] = items["Bard_items"][key]

    return available_items

def create_inventory(character_name,items):
    inventory = {}
    for _ in range(7):
        available_items_list = available_items(characters, character_name, items)               
        for i in inventory.keys():
            if i in available_items_list.keys():
                available_items_list.pop(i)
        while True:
            print("Available Items:")
            for i in available_items_list:
                print(i)
            
            item_to_add = input("What item would you like to add? Make sure to enter the name exactly as it is in the list.\nEnter here:  ")
            if item_to_add not in available_items_list:
                print("Please enter an item that is in the list.")
            else:
                check = input(f"Are you sure you want to add {item_to_add} to your inventory? Y/N: ").strip().capitalize()
                
                if check == "Y":
                    inventory[item_to_add] = available_items_list[item_to_add]
                    break
                else:
                    continue

    return inventory

def create_character(species_list,classes_list,characters): 
    new_stats = {"Strength":0,"Dexterity":0,"Constitution":0,"Wisdom":0,"Intelligence":0,"Charisma":0}
    while True:
        
        character_name = input("What will the name of your character be?\nEnter here: ").strip()
        
        check = input(f"Are you sure you want {character_name} to be your character's name? Y/N: ").strip().capitalize()
        if check == "Y":
            characters[character_name] = {}
            characters[character_name]["Level"] = 1
            level = 1
            break
        else:
            continue

    while True:
        
        print("Available Races")
        for i in species_list:
            print(i)
        race = input("What will the race of your character be?\nEnter here (name):\n ").strip().capitalize()
        if race not in actual_species_list:
            
            print("Invalid answer")
        else:
            
            check = input(f"Are you sure you want {character_name} to be a {race}? It cannot be changed later. Y/N: ").strip().capitalize()
            if check == "Y":
                race = tuple([race])
                characters[character_name]["Race"] = race
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
                
                stat = input(f"What do you want your base stat for {i} to be?")
                if stat.isnumeric() == False:
                    
                    print("Invalid answer")
                    continue
                else:
                    stat = int(stat)
                    final_stat = new_stats[i] + stat
                    if final_stat > 20:
                        
                        print("That would make the stat go over 20. Please enter a lower number.")
                        continue
                    else:
                        
                        check = input(f"{i}: {final_stat}. Are you sure this is what you want? Y/N: ").strip().capitalize()
                        if check == "Y":
                            new_stats[i] = final_stat
                            break
                        else:
                            continue
        characters[character_name]["Stats"] = new_stats
        break   
    print("Available Classes:")
    for i in classes_list:
        print(i)
    while True:
        
        class_choice = input("What class do you want to take?\nEnter here: ").strip().capitalize()
        if class_choice not in classes_list:
            print("Invalid answer")
        else:
            
            check = input(f"Are you sure you want to take {class_choice} as your class? Y/N: ").strip().capitalize()
            if check == "Y":
                class_choice = tuple([class_choice])
                characters[character_name]["Class"] = class_choice
                break
            else:
                continue
    
    while True:
        characters[character_name]["Skills"] = set()
        class_choice = str(class_choice[0])
        available_skills = skills_available(level,character_class = class_choice)
        amount_of_skills = 2
        new_skills = skill_choice(available_skills,characters,character_name,amount_of_skills)
        for i in new_skills:
            characters[character_name]["Skills"].add(i)
        break
    while True:
        inventory = create_inventory(character_name,items)
        characters[character_name]["Inventory"] = inventory
        break
    
    print("Character Creation Finished!")
    return


def level_up(characters,character_name):
    while True:
        
        choice = input("Would like to to gain +1 to a stat or gain a new skill? Skill/Stat: ").strip().capitalize()
        if choice == "Skill":
            class_choice = characters[character_name]["Class"][0]
            level = characters[character_name]["Level"]
            available_skills = skills_available(level,character_class = class_choice)
            new_skills = skill_choice(available_skills,characters,character_name,amount_of_skills=1)
            for i in new_skills:
                characters[character_name]["Skills"].add(i)
            return
        elif choice == "Stat":
            while True:
                for k in characters[character_name]["Stats"].keys():
                    print(f"{k}: {characters[character_name]["Stats"][k]}")
                stat = input("What stat would you like to increase? Enter number:\n1. Strength\n2. Dexterity\n3. Constitution\n4. Wisdom\n5. Intellgience\n6. Charisma\nEnter here:").strip()
                match stat:
                    case "1":
                        if characters[character_name]["Stats"]["Strength"] == 20:
                            
                            print("Strength is already 20, it cannot go any higher.")
                            continue
                        else:
                            characters[character_name]["Stats"]["Strength"] += 1
                            break
                    case "2":
                        if characters[character_name]["Stats"]["Dexterity"] == 20:
                            
                            print("Strength is already 20, it cannot go any higher.")
                            continue
                        else:
                            characters[character_name]["Stats"]["Dexterity"] += 1
                            break
                    case "3":
                        if characters[character_name]["Stats"]["Constitution"] == 20:
                            
                            print("Strength is already 20, it cannot go any higher.")
                            continue
                        else:
                            characters[character_name]["Stats"]["Constitution"] += 1
                            break
                    case "4":
                        if characters[character_name]["Stats"]["Wisdom"] == 20:
                            
                            print("Strength is already 20, it cannot go any higher.")
                            continue
                        else:
                            characters[character_name]["Stats"]["Wisdom"] += 1
                            break
                    case "5":
                        if characters[character_name]["Stats"]["Intelligence"] == 20:
                            
                            print("Strength is already 20, it cannot go any higher.")
                            continue
                        else:
                            characters[character_name]["Stats"]["Intelligence"] += 1
                            break
                    case "6":
                        if characters[character_name]["Stats"]["Charisma"] == 20:
                            
                            print("Strength is already 20, it cannot go any higher.")
                            continue
                        else:
                            characters[character_name]["Stats"]["Charisma"] += 1
                            break
                    case _:
                        
                        print("Invalid answer")
                        continue
                return

def manage_inspect(characters,character_name):
    while True:
        print(f"Name: {character_name}\nRace: {str(characters[character_name]["Race"][0])}\nClass: {str(characters[character_name]["Class"][0])}\nLevel: {characters[character_name]["Level"]}")
        change = input("Would you like to edit the Name or Level of your character? Y/N: ").strip().capitalize()
        if change == "N":
            break
        elif change == "Y":
            
            item_to_change = input("Name or Level?\nEnter here: ").strip().capitalize()
            if item_to_change == "Name":
                while True:
                    
                    new_name = input("Enter the new name of your character: ")
                    
                    check = input(f"Are you sure you want {new_name} to tbe the name of your character? Y/N: ").strip().capitalize()
                    if check == "Y":
                        characters[new_name] = characters[character_name].pop()
                        character_name = new_name
                    else:
                        continue
            elif item_to_change == "Level":
                while True:
                    
                    print(f"Current Level: {characters[character_name]["Level"]}")
                    
                    new_level = input("What do you want to change your level to? It can only be increased. Type 'Exit' to go back to the inspect menu.\nEnter here: ").strip().capitalize()
                    if new_level == "Exit":
                        return character_name
                    elif new_level.isnumeric() is False or int(new_level) > 20 or int(new_level) < characters[character_name]["Level"]:
                        print("Please enter a valid answer.")
                        continue
                    else:
                        
                        check = input(f"Are you sure you want to set your character's level to {new_level}? Y/N: ").strip().capitalize()
                        if check == "Y":
                            old_level = characters[character_name]["Level"]
                            new_level = int(new_level)
                            characters[character_name]["Level"] = new_level
                            for _ in range(new_level - old_level):
                                level_up(characters,character_name)
                            break
                        else:
                            continue
            else:
                
                print("Please enter 'Name' or 'Level'.")
                continue
                    
