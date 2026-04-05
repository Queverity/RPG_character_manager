# CB 1st Character Class

# import  item_class and skill_class

# Class Character:
    # define method __init__(self):
        # attributes important to character will be char_name, char_class, race, level, inventory, skills, and attributes
    
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
    # for items, max will be 7 (items will be entered using ID) Note: Don't do this, just let the user choose items after character creation.
    # once creation is done, first create character object, then save to character CSV

class Character:
    def __init__(self,name,id,char_class,race,level,attributes = {"Strength":10,"Dexterity":10,"Constitution":10,"Wisdom":10,"Intelligence":10,"Charisma":10}):
        self.name = name
        self.id = id
        self.char_class = char_class
        self.race = race
        self.level = level
        self.inventory = []
        self.skills = []
        self.attributes = attributes

    def __str__(self):
        return f"{self.name}, Level {self.level} {self.race} {self.char_class} (ID: {self.id})"
    
    def display_stats(self):
        for k,v in self.attributes:
            print(f"{k}: {v}")

        print("Note: Stats cannot be changed from this menu. You can gain +1 to a stat of your choosing per level.")
        # after_action()
        return

    def level_up(self):
        print("You have gained another skill slot.")


        print("You have gained +1 in a stat of your choosing. Which stat would you like to increase?")

        while True:
            for i in self.attributes.keys:
                print(i)

            stat = input("Enter name of attribute you want to increase:\n").strip().capitalize()


            try:
                test = self.attributes[stat]
            except:
                print("Please enter a valid stat.")
                # after_action()
                continue
            else:
                self.attributes[stat] += 1
                print(f"{stat} has been increased by 1.")
                # after_action()
                return

    def find_items(self,items_list):
        user_items = []
        for i in items_list:
            if i.class_requirement.lower() == "all":
                user_items.append(i)
            elif self.char_class.lower() in i.class_requirement.lower():
                user_items.append(i)
            else:
                pass
        
        for i in self.inventory:
            for o in user_items:
                if i.lower() == o.id.lower():
                    user_items.pop(o)

        # after this, check if any of the items in the list match an id in the uesr's inventory

        return user_items

    def find_skills(self,skills_list):
        user_skills = []
        for i in skills_list:
            if i.class_requirement.lower() == "all":
                user_skills.append(i)

            elif self.char_class.lower() in i.class_requirement.lower():
                if self.level >= i.level_requirement:
                    user_skills.append(i)
                else:
                    pass

            else:
                pass
        for i in self.skills:
            for o in user_skills:
                if i.lower() == o.id.lower():
                    user_skills.pop(o)

        return user_skills

    def load_inventory(self,items_list):
        inventory = []
        for i in self.inventory:
            for o in items_list:
                if i.lower() == o.id.lower():
                    inventory.append(o)
                else:
                    pass
        
        return inventory
    
    def inventory_weight(self,items_list):
        user_inventory = self.load_inventory(items_list)

        total_weight = 0

        for i in user_inventory:
            if i.weight == "Negligible":
                pass
            else:
                total_weight += int(i.weight)

        return total_weight

    def load_skills(self,skills_list):
        skills = []
        for i in self.skills:
            for o in skills_list:
                if i.lower() == o.id.lower():
                    skills.append(o)
                else:
                    pass
        
        return skills
    
    def edit_inventory(self,items_list):
        available_items = self.find_items(items_list)
        user_inventory = self.load_inventory(items_list)

        

        while True:
            print(f"{self.name}'s Inventory:")

            count = 0
            for i in user_inventory:
                count += 1
                # Since these are Item class objects, they have a __str__ function built in so they print out pretty.
                print(f"{count}. {i.basic_view()}")

            print("What would you like to do with your character's inventory?\n[1] Inspect Item\n[2] Remove Item\n[3]Add Item\n[R] Return to Character Inspection Menu")
            choice = input("Enter number:\n").strip().capitalize()

            # clear_screen()

            match choice:
                case '1':
                    count = 0
                    for i in user_inventory:
                        count += 1
                        # Since these are Item class objects, they have a __str__ function built in so they print out pretty.
                        print(f"{count}. {i.basic_view()}")

                    item_id = input("Enter ID of item you wish to inspect, or enter 'exit' to return to inventory inspection menu:\n").strip().lower()

                    if item_id == 'exit':
                        return

                    for i in user_inventory:
                        if i.id.lower() == item_id:
                            print(i)
                            # after_action()
                            break
                    
                    continue

                case '2':
                    if bool(self.inventory) == False:
                        print("You have no items in your inventory.")
                        # after_action
                        continue

                    count = 0
                    for i in user_inventory:
                        count += 1
                        # Since these are Item class objects, they have a __str__ function built in so they print out pretty.
                        print(f"{count}. {i.basic_view()}")

                    item_id = input("Enter ID of item you wish to remove, or enter 'exit' to return to inventory inspection menu:\n").strip().lower()

                    if item_id == 'exit':
                        return

                    found = False

                    for i in self.inventory:
                        if item_id == i.lower():
                            found = True
                            self.inventory.pop(i)

                            for o in user_inventory:
                                if o.id.lower() == item_id:
                                    user_inventory.pop(o)
                                else:
                                    pass

                            print("Item succesfully removed.")
                            # after_action
                            break

                    if found != True:
                        print("Please enter a valid ID.")

                    return


                case '3':
                    inventory_weight = self.inventory_weight(items_list)

                    if inventory_weight >= self.attributes['Strength'] * 15:
                        print("You have too much weight in your inventory to carry anything else.")
                        # after_action()
                        return

                    count = 0
                    print("Items available to add:\n")
                    for i in available_items:
                        count += 1
                        # Since these are Item class objects, they have a __str__ function built in so they print out pretty.
                        print(f"{count}. {i.basic_view()}")

                    item_id = input("Enter ID of item you wish to add, or enter 'exit' to return to inventory inspection menu:\n").strip().lower()

                    if item_id == 'exit':
                        return

                    found = False

                    for i in available_items:
                        if item_id == i.id.lower():
                            if i.weight != "Negligible":
                                if inventory_weight + int(i.weight) > self.attributes['Strength'] * 15:
                                    print("Adding that item to your inventory would bring your total inventory weight over maximum (Strength * 15).")
                                    break
                            
                            found = True
                            self.inventory.append(item_id)

                            for o in user_inventory:
                                if o.id.lower() == item_id:
                                    user_inventory.append(o)
                                else:
                                    pass

                            print("Item succesfully added.")
                            # after_action
                            break

                    if found != True:
                        print("Please enter a valid ID.")
                        continue

                    return
                case 'R':
                    return
                case _:
                    print("Please enter one of the displayed options.")
                    # after_action

    def edit_skills(self,skills_list):
        available_skills = self.find_skills(skills_list)
        user_skills = self.load_skills()

        

        while True:
            print(f"{self.name}'s Skill List:")

            count = 0
            for i in user_skills:
                count += 1
                # Since these are Item class objects, they have a __str__ function built in so they print out pretty.
                print(f"{count}. {i.basic_view()}")

            print("What would you like to do with your character's inventory?\n[1] Inspect Item\n[2] Remove Item\n[3] Add Item\n[R] Return to Character Inspection Menu")
            choice = input("Enter number:\n").strip().capitalize()

            # clear_screen()

            match choice:
                case '1':
                    count = 0
                    for i in user_skills:
                        count += 1
                        # Since these are Item class objects, they have a __str__ function built in so they print out pretty.
                        print(f"{count}. {i.basic_view()}")

                    item_id = input("Enter ID of skill you wish to inspect, or enter 'exit' to return to inventory inspection menu:\n").strip().lower()

                    if item_id == 'exit':
                        return

                    for i in user_skills:
                        if i.id.lower() == item_id:
                            print(i)
                            # after_action()
                            break
                    
                    continue

                case '2':
                    if bool(self.skills) == False:
                        print("You have no skills in your inventory.")
                        # after_action
                        continue

                    count = 0
                    for i in user_skills:
                        count += 1
                        # Since these are Skill class objects, they have a __str__ function built in so they print out pretty.
                        print(f"{count}. {i.basic_view()}")

                    item_id = input("Enter ID of skill you wish to remove, or enter 'exit' to return to skill list inspection menu:\n").strip().lower()

                    if item_id == 'exit':
                        return

                    found = False

                    for i in self.skills:
                        if item_id == i.lower():
                            found = True
                            self.skills.pop(i)

                            for o in user_skills:
                                if o.id.lower() == item_id:
                                    user_skills.pop(o)
                                else:
                                    pass

                            print("Skill succesfully removed.")
                            # after_action
                            break

                    if found != True:
                        print("Please enter a valid ID.")

                    return


                case '3':
                    max_skills = self.level + 2
                    if len(self.skills) == max_skills:
                        print(f"You have the max number of skills ({self.level + 2}) for your level:")
                        continue

                    count = 0
                    print("Skills available to add:")
                    for i in available_skills:
                        count += 1
                        # Since these are Skill class objects, they have a __str__ function built in so they print out pretty.
                        print(f"{count}. {i.basic_view()}")

                    item_id = input("Enter ID of skill you wish to add, or enter 'exit' to return to skill list inspection menu:\n").strip().lower()

                    if item_id == 'exit':
                        return

                    found = False

                    for i in available_skills:
                        if item_id == i.id.lower():
                            
                            found = True
                            self.inventory.append(item_id)

                            for o in user_skills:
                                if o.id.lower() == item_id:
                                    user_skills.append(i)
                                else:
                                    pass

                            print("Item succesfully added.")
                            # after_action
                            break

                    if found != True:
                        print("Please enter a valid ID.")
                        # after_action()
                        continue

                    return
                case 'R':
                    return
                case _:
                    print("Please enter one of the displayed options.")
                    # after_action
                    continue

def create_character(characters_list):
    classes = ['Rouge','Fighter','Barbarian','Wizard','Warlock','Sorcerer','Bard']
    races = {'Human':'Constitution','Elf':'Dexterity','Dwarf':'Strength','Dragonborn':'Wisdom','Gnome':'Intelligence','Halfling':'Charisma'}

    # name
    while True:
        name = input("Enter name for your new character:\n").strip()
        
        check = input(f"Are you sure you want {name} to be your character's name? Y/N:\n").strip().lower()

        if check != "y":
            continue

        break

    # id
    while True:
        id = input("Enter ID for character:\n").strip().upper()
        for i in characters_list:
            if i.id.upper() == id:
                print("There is already a saved character with that id. Please enter a different id.")
                continue
        
        break

    # race
    while True:
        print("Available Races:")
        for k,v in races.items():
            print(f"{k} (+2 {v})")

        race = input("Enter name of race you want for your character:\n").strip().capitalize()
        if race not in races:
            print("Please enter one of the displayed races.")
            # after_action()
            continue

        break

    # class
    while True:
        print("Available Classes:")
        for i in classes:
            print(i)

        char_class = input("Please enter name of class you want your character to have:\n").strip().capitalize()

        if char_class not in classes:
            print("Please enter one of the displayed classes.")
            # after_action()
            continue

        break

    # attributes
    while True:
        strength = input("Enter value for strength stat:\n")

        dexterity = input("Enter value for dexterity stat:\n")

        constitution = input("Enter value for constitution stat:\n")

        intelligence = input("Enter value for intelligence stat:\n")

        wisdom = input("Enter value for wisdom stat:\n")

        charisma = input("Enter value for charisma stat:\n")

        attributes = {"Strength":strength,"Dexterity":dexterity,"Constitution":constitution,"Wisdom":wisdom,"Intelligence":intelligence,"Charisma":charisma}

        fail = False

        for k,v in attributes.items():
            try:
                v = int(v)
            except:
                print(f"You have input a non-numerical value for {k}. Please enter an actual number.")
                fail = True
                # after_action()
                break
            else:
                pass

        if fail == True:
            continue

        for k,v in attributes.items():
            print(f"{k}: {v}")

        verify = input("Verify these are the correct values Y/N:\n").strip().lower()

        if verify != "y":
            continue

        break

    # level
    while True:
        level = input("Enter level (between 1 - 20)of character:\n").strip()
        try:
            level = int(level)
        except:
            print("Please enter a numerical value between 1 and 20 for level.")
            # after_action()
            continue
        else:
            if level < 1 or level > 20:
                print("Please enter a level between 1 and 20.")
                # after_action()
                continue
            
            break

    try:
        character_object = Character(name,id,char_class,race,level,attributes)
    except:
        print("There was an unexpected error in creating the character object.")
        # after_action()
        return
    else:
        print("Character created succesfully!")
        # after_action
        return character_object
    

def create_character_objects(characters_csv):
    characters_list = []
    for i in characters_csv:
        character_attributes = {"Strength":"N/A","Dexterity":"N/A","Constitution":"N/A","Wisdom":"N/A","Intelligence":"N/A","Charisma":"N/A"}
        attribute_values = i.attributes.split("|")
        index = 0
        for k in character_attributes.keys():
            character_attributes[k] = attribute_values[index]
            index += 1
        
        inventory = i.inventory.split("|")

        skills = i.skills.split("|")

        character_object = Character(i.name,i.char_class,i.race,i.level,character_attributes)
        character_object.inventory = inventory
        character_object.skills = skills

        characters_list.append(character_object)

    return characters_list



        
