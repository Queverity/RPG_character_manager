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


