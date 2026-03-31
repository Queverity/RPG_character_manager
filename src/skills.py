#Isaac Covington CP2 Skill Management


from UI_liam import print_indict_dictionaries

general_skills = {'Athletics','Acrobatics','Slight of Hand','Stealth','Arcana','History','Investigation','Relegion','Nature','Animal Handling','Insight','Perception','Survival','Deception','Intimidation','Performance','Persausion'}

ten_rouge_skills = {'Sneak Attack', 'Parkour'}

ten_wizard_skills = {'Fireball', 'Wrong Spell'}

ten_barbarian_skills = {'Rage', 'Angry Bonk'}

ten_bard_skills = {'Sick Lick', 'Distracting Solo'}

ten_fighter_skills = {'Stab', 'Tactical Yelling'}

ten_cleric_skills = {'Judgy Heal', 'Divine "I told you so"'}


twenty_rouge_skills = {'Pocket Sand', 'Not Yours to Take'}

twenty_wizard_skills = {'Mystical Firearm', 'Magic Tape'}

twenty_barbarian_skills = {'Too Angry to Die', 'Optional Physics'}

twenty_bard_skills = {'Power Chord', 'Platinum Record'}

twenty_fighter_skills = {'Parry This', 'Panic Attack'}

twenty_cleric_skills = {'Holy Uno Reverse'}


def skills_available(level,character_class): 
    global ten_rouge_skills,ten_wizard_skills,ten_barbarian_skills,ten_bard_skills,ten_fighter_skills,ten_cleric_skills

    global twenty_rouge_skills,twenty_wizard_skills,twenty_barbarian_skills,twenty_bard_skills,twenty_fighter_skills

    global general_skills
    twenty_cleric_skills
    available_skills = set()

    for i in general_skills:
        available_skills.add(i)

    if level < 10:
        character_class = str(character_class)
        match character_class:
            case 'Fighter':
                for i in ten_fighter_skills:
                    available_skills.add(i)
            case 'Bard':
                for i in ten_bard_skills:
                    available_skills.add(i)
            case 'Wizard':
                for i in ten_wizard_skills:
                    available_skills.add(i)
            case 'Rogue':
                for i in ten_rouge_skills:
                    available_skills.add(i)
            case 'Barbarian':
                for i in ten_barbarian_skills:
                    available_skills.add(i)
            case 'Cleric':
                for i in ten_cleric_skills:
                    available_skills.add(i)
    else:
        match character_class:
            case 'Fighter':
                for i in ten_fighter_skills:
                    available_skills.add(i)

                for i in twenty_fighter_skills:
                    available_skills.add(i)
            case 'Bard':
                for i in ten_bard_skills:
                    available_skills.add(i)

                for i in twenty_bard_skills:
                    available_skills.add(i)
            case 'Wizard':
                for i in ten_wizard_skills:
                    available_skills.add(i)

                for i in twenty_wizard_skills:
                    available_skills.add(i)
            case 'Rogue':
                for i in ten_rouge_skills:
                    available_skills.add(i)

                for i in twenty_rouge_skills:
                    available_skills.add(i)
            case 'Barbarian':
                for i in ten_barbarian_skills:
                    available_skills.add(i)

                for i in twenty_barbarian_skills:
                    available_skills.add(i)
            case 'Cleric':
                for i in ten_cleric_skills:
                    available_skills.add(i)

                for i in twenty_cleric_skills:
                    available_skills.add(i)

    return available_skills

def skill_choice(available_skills,characters,character_name,amount_of_skills):
    print("Available Skills")
    new_skills = set()
    print("Current Skills:")
    print_indict_dictionaries(characters,character_name,type="Skills")
    for i in available_skills:
        print(i)
    for _ in range(amount_of_skills):
        while True:
            chosen_skill = input(f"Which skill do you want? Type the name of your chosen skill, exactly as seen on the list.\nEnter here:\n").strip()
            if chosen_skill in available_skills:
                check = input(f"Are you sure you want to take {chosen_skill} as a skill? Y/N: ").strip().capitalize()
                if check == "Y":
                    new_skills.add(chosen_skill)
                    available_skills.remove(chosen_skill)
                    break
                else:
                    continue
            else:
                print("Invalid answer")
                continue
    return new_skills
