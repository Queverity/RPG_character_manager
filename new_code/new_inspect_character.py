# CB 1st Inspect Character

# define function inspect_character(character_object):
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