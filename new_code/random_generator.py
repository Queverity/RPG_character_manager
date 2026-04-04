# CB 1st Character Generation (Faker)

from faker import Faker
import random
from character_class import *


# define function background_generator():
    # write this kind of like a madlib, where there are preset paragraphs that faker fills in based on details from character, such as class and race
    # have faker pick personality details out of a list


# define function character_generator():
    # allow user to enter character race and class if they want, also name
    # randomly pick skill and items based off of class, for a level 1 character

# define function quest_generator():
    # similar to background generator, write this like madlibs where faker fills in certian information like quest giver, destination, and other stuff

fake = Faker()

class RandomGenerator():
    def __init__(self,characters):
        # info for backgrounds and character
        races = ["Human", "Elf", "Dwarf", "Dragonborn", "Gnome", "Halfling"]
        classes = ['Fighter','Barbarian','Rouge','Warlock','Sorcerer','Wizard','Bard']

        traits = [
    "fiercely loyal", "haunted by visions", "hungry for power",
    "kind-hearted", "vengeful", "cursed from birth",
    "recklessly brave", "obsessive", "mysterious", "stoic",
    "compassionate", "greedy", "charming", "impulsive",
    "proud", "cunning", "fearful of magic", "determined",
    "secretly noble", "quick-tempered", "wise beyond years",
    "altruistic", "morally conflicted", "untrusting", "loyal to a fault"
]

        events = [
            "their family was slain by a mysterious force",
            "they discovered a forbidden magical artifact",
            "they were exiled for a crime they didn’t commit",
            "they made a pact with a dark entity",
            "they survived a catastrophe that destroyed their home",
            "they witnessed the rise of a tyrant who destroyed their village",
            "they were chosen by a mystical creature to carry a prophecy",
            "they accidentally unleashed an ancient evil",
            "they were betrayed by their closest friend",
            "they found a secret passage to a lost kingdom",
            "they were taken prisoner by marauding bandits",
            "they stumbled upon an enchanted forest and were forever changed",
            "they lost everything to a devastating plague",
            "they angered a powerful spirit and must atone",
            "they were shipwrecked on a mysterious island",
            "they inherited a dangerous and cursed legacy",
            "they survived an encounter with a legendary beast"
        ]

        goals = [
    "seek revenge",
    "uncover the truth",
    "restore their homeland",
    "master their powers",
    "forge their own destiny",
    "protect a sacred artifact",
    "find a lost loved one",
    "stop an ancient evil",
    "gain recognition and honor",
    "amass wealth and influence",
    "learn forbidden knowledge",
    "break a powerful curse",
    "reclaim a lost throne",
    "avenge their mentor",
    "form a legendary guild",
    "unite warring factions",
    "defeat a rival in battle",
    "discover a hidden realm",
    "redeem themselves from past mistakes",
    "prevent a prophecy from coming true",
    "fulfill a sacred oath",
    "become a master of their craft"
]

        quests = {
            'fetch':['Powerful Dragon', 'Corruped Necromancer', 'Goblin Warlord', 'Frost Giant', 'Shadow Wraith'],
            'slay':['Ancient Relic', 'Healing Herb Bundle', 'Enchanted Gemstone', 'Lost Spell Tome', 'Royal Signet Ring'],
            'escort':['Nervous Merchant', 'Wounded Knight', 'Young Noble', 'Traveling Scholar', 'Mystic Seer']
            ,'craft':['Powerful Sword','Vital Potion','Mysterious Amulet','Gun','Magical Armor'],
            'ccourier':['Secret Letter', 'Royal Decree', 'Encrypted Scroll', 'War Dispatch', 'Love Letter'],
            'recon':['Enemy Troop Movements', 'Hidden Treasure Location', 'Ancient Ritual Details', 'Spy Network Contacts', 'Dungeon Layout Map'],
            'steal':['Jeweled Crown', 'Vault Key', 'Ancient Artifact', 'Bag of Gold Coins', 'Magical Amulet'],
            'assassinate':['Corrupt Noble', 'Enemy General', 'Rogue Wizard', 'Crime Lord', 'Traitorous Guard Captain'],
            'sabotage':['Burn Supply Wagons', 'Poison Water Source', 'Destroy Bridge', 'Disable Siege Weapons', 'Cut Communication Lines']}
        
        self.characters = characters



    def generate_char_backstory(self,name,race,char_class,trait,event,origin,goal):
        return f"{name} is a {race} who is known for being {trait}. They come from {origin}, and cherish that place dearly.It was changed forever, though, when {event}. After that, they became a {char_class}, and hope to {goal} one day."

    def generate_char_attributes(self):
        name = Faker.first_name()

        attribute_names = ['Strength','Dexterity','Constitution','Wisdom','Intelligence','Charisma']
        char_attributes = {"Strength":10,"Dexterity":10,"Constitution":10,"Wisdom":10,"Intelligence":10,"Charisma":10}

        race = random.choice(self.races)
        char_class = random.choice(self.classes)


        for i in range(0,5):
            attribute = random.randint(8,18)
            char_attributes[attribute_names[i]] = attribute

        return name,char_attributes,race,char_class

    def generate_character(self):
        name,char_attributes,race,char_class = self.generate_char_attributes()
        origin = faker.city_name(it_IT)
        trait = random.choice(self.traits)
        event = random.choice(self.events)
        origin = random.choice(self.origins)
        goal = random.choice(self.goals)

        backstory = self.generate_char_backstory(name,race,char_class,trait,event,origin,goal)

        while True:
            id = input("Enter ID for generated character:\n").strip().upper()

            for i in self.characters:
                if id == i.id.upper():
                    print("There is already a character saved with that ID.")
                    continue
            
            level = 1

            character_object = Character(name,id,char_class,race,level)

            print("Character succesfully generated!")
            print("Note: Character does not come preloaded with inventory items and skills chosen; You will have to do that yourself.")
            print(backstory)

            # after_action()

            return character_object

    def generate_quest(self):
        quest_type = random.choice(self.quests.keys)
        quest_focus = random.choice(self.quests[quest_type])
        if quest_type not in ['craft','slay']]:
            city = faker.city_name(it_IT)
        quest_giver = faker.first_name()

        if quest_type not in ['craft','slay']:
            print(f"You have been given a {quest_type} by a mysterious person named {quest_giver}. The goal of this quest is to {quest_type} the/a {quest_focus}. Your target will be found in the city of {city}")
        else:
            print(f"You have given a {quest_type} by a mysterious person named {quest_giver}. The goal of this quest is to {quest_type} the/a {quest_focus}. To gather information on how to proceed, talk to the locals.")

        # after_action
        return