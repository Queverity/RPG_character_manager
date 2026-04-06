# CB 1st Skill Class

import csv
from helper import *
from saving_parsing import save_skill

# class Skill:
    # define method __init__:
        # attributes for skill will be name, description, id, level_requirement, and class_requirement

    # define method __str__:
        # print out basic info on skill, such as name and description (also id, because user will input skills as id)



# define function load_skills(skills_csv):
    # skill_list = []
    # after loading string from skills csv, take info from each row and turn it into a object. Then, append each object to skill_list, where it can be stored for later use.
    # return skill_list

# define function create_skill():
    # have user enter data for each attribute of a skill object (make sure id isn't already taken, ids will be 3 letter combinations)
    # first take object and save to skill list, then save to skills csv

class Skill:
    def __init__(self,name,id,description,level_requirement,class_requirement):
        self.name = name
        self.id = id
        self.description = description
        self.level_requirement = level_requirement
        self.class_requirement = class_requirement

    def __str__(self):
        return f"{self.name} ({self.id}): {self.description} | Level: {self.level_requirement}"
    
    def basic_view(self):
        return f"{self.name} ({self.id})"
    
def load_skill_objects(skills):
    skills_list = []
    for i in skills:
        skill_object = (i['name'],i['id'],i['description'],i['level'],i['classes'])
        skills_list.append(skill_object)

    return skills_list

def create_skill(skills_list):
    available_classes = ['Rouge','Fighter','Barbarian','Bard','Wizard','Sorcerer','Warlock','All']
    name = input("Enter name for skills\n").strip()
    description = input("Enter description for item:\n").strip()

    while True:
        class_requirement = input("Please enter the required class to use this skill. If any class could use this skill, enter 'All'.").strip().capitalize()

        if class_requirement not in available_classes:
            print("Please enter a valid class.")
            continue

        break


    while True:
        level = input("Enter level of skill:\n").strip()
        try:
            value = int(value)
            break
        except:
            print("Please enter a number.")
            continue

    while True:
        id = input("Enter ID for skill (3-letter combination):\n").strip().lower()
        if len(id) > 3:
            print("Please enter 3 letters for the skill id.")
            continue

        for i in skills_list:
            if i.id.lower() == id:
                print("There is already an skill with that id saved. Please enter a different id.")
                continue
        
        break

    skill_object = Skill(name,id,description,level,class_requirement)
    skills_list.append(skill_object)
    try:
        save_skill(skill_object)
    except:
        print("Failed to create skill; Unexpected error has occured")
        return
    else:
        print("Skill created and saved succesfully!")
        after_action()
        return skills_list
