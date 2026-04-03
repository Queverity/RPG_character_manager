# CB 1st User Interface

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
    # this iwl lbe for viewing a single character
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

