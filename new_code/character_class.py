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
    def __init__(self,name,char_class,race,level,attributes = {"Strength":10,"Dexterity":10,"Constitution":10,"Wisdom":10,"Intelligence":10,"Charisma":10}):
        self.name = name
        self.char_class = char_class
        self.race = race
        self.level = level
        self.inventory = []
        self.skills = []
        self.attributes = attributes

    def __str__(self):
        return f"{self.name}, Level {self.level} {self.race} {self.char_class}"
    
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

            print("What would you like to do with your character's inventory?\n1. Inspect Item\n2. Remove Item\n3. Add Item\n4. Return to Character Inspection Menu")
            choice = input("Enter number:\n").strip()

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

                    available_items = self.find_items(items_list)

                    count = 0
                    for i in available_items:
                        count += 1
                        # Since these are Item class objects, they have a __str__ function built in so they print out pretty.
                        print(f"{count}. {i.basic_view()}")

                    item_id = input("Enter ID of item you wish to add, or enter 'exit' to return to inventory inspection menu:\n").strip().lower()

                    if item_id == 'exit':
                        return

                    found = False

                    for i in self.inventory:
                        if item_id == i.lower():
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

                    return
                case '4':
                    return
                case _:
                    print("Please enter 1, 2, 3, or 4.")
                    # after_action


    def edit_skills(self):
        pass

def create_character():
    pass

def load_character():
    pass
