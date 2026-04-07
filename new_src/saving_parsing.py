# CB 1st Saving Parsing Characters

import csv

# define function load_characters():
    # use with open to open characters file so it will close on its own
    # go through file, add each row to a list, then return so each dict can be made into a character object


# define function save_characters(characters):
    # use with open to open characters file so it will close on its own
    # go through list of character objects, turn into dictionaries, and save

# define function load_skills():
    # use with open to open skills file so it will close on its own
    # go through file, add each row to a list, then return so each dict can be made into a skill object

# define function save_skills(skills):
    # use with open to open skills file so it will close on its own
    # go through list of skill objects, turn into dictionaries, and save


# define function load_items():
    # use with open to open ites file so it will close on its own
    # go through file, add each row to a list, then return so each dict can be made into a item object

# define function save_items(items):
    # use with open to open items file so it will close on its own
    # go through list of item objects, turn into dictionaries, and save

def load_characters():
    character_list = []
    with open("RPG_character_manager\\documents\\characters.csv",mode="r",newline="") as characters:
        fieldnames = ['name','id','char_class','level','race','attributes','skills','inventory']
        reader = csv.DictReader(characters,fieldnames)
        next(reader)

        for i in reader:
            character_list.append(i)

    return character_list

def save_characters(characters):
    with open("RPG_character_manager\\documents\\characters.csv",mode="w",newline="") as characters_csv:
        fieldnames = ['name','id','char_class','level','race','attributes','skills','inventory']
        writer = csv.DictWriter(characters_csv,fieldnames)
        basic_writer = csv.writer(characters_csv)

        basic_writer.writerow(fieldnames)
 
        for char in characters:
            char = vars(char)
            char['attributes'] = list(char['attributes'].values())
            attribute_holder = []
            for attr in char['attributes']:
                attribute_holder.append(str(attr))
            char['attributes'] = "|".join(attribute_holder)
            
            
            char['inventory'] = "|".join(char['inventory'])
            char['skills'] = "|".join(char['skills'])

            writer.writerow(char)

def load_skills():
    skills_list = []
    with open("RPG_character_manager\\documents\\skills.csv",mode="r",newline="") as skills:
        fieldnames = ['name','id','description','level','classes']
        reader = csv.DictReader(skills,fieldnames)

        for i in reader:
            skills_list.append(i)

        return skills_list

def save_skill(skill_object):
    with open("RPG_character_manager\\documents\\skills.csv",mode="a",newline="") as skills:
        fieldnames = ['name','id','description','level','classes']
        writer = csv.DictWriter(skills,fieldnames)

        writer.writerow(vars(skill_object))


def load_items():
    items_list = []
    with open("RPG_character_manager\\documents\\items.csv",mode="r",newline="") as items:
        fieldnames = ['name','id','description','value','weight','classes']
        reader = csv.DictReader(items,fieldnames)

        for i in reader:
            items_list.append(i)

        return items_list

def save_item(item_object):
    with open("RPG_character_manager\\documents\\items.csv",mode="a",newline="") as items:
        fieldnames = ['name','id','description','value','weight','classes']
        writer = csv.DictWriter(items,fieldnames)

        writer.writerow(vars(item_object))

