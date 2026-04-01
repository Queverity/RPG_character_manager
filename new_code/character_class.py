# CB 1st Character Class

# import  item_class and skill_class

# Class Character:
    # define method __init__(self):
        # attributes important to character will be name, class, race, level, inventory, skills, and attributes
    
    # define method __str__(self):
        # print out basic details of character, such as name, class, race, and level

    # define method level_up():
        # tell user they have gained a new skill slot and can go select that elsewhere, and allow them to add +1 to a stat

    # define method edit_inventory():
        # ask user how they would like to edit inventory (add item, remove item)
        # if add item, first check that inventory isn't full
        # if it isn't give user list of avaiable items they can add, take user input
        # if remove item, first check that inventory isn't empty
        # if it isn't, give user list of items in inventory, take user input
        # remove item user entered, update csv

    # define method edit_skills():
        # ask user how they would like to edit skills (add skill, remove skill)
        # if add skill, first check if all skill slots are taken
        # if they aren't, display avaialable skills, take user input
        # if remove skill, first check if all skill slots are empty
        # if they aren't, display current skills, take user input
        # remove chosen skill, update csv

# define function create_character():
    # have user enter character name, class, race, and level
    # for skills, max will be level + 2 (skills will be entered using id)
    # if user is above level 1, ask them what stat they would like to boost (unless all stats are at max)
    # for items, max will be 7 (items will be entered using ID)
    # once creation is done, first create character object, then save to character CSV

