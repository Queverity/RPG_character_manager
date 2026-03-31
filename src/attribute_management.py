#PS 1st attribute manager
#

#
from character_managment import characters
from UI_liam import print_indict_dictionaries

#function called attribute_manager(character dictionary, character chosen)

def attribute_manager(char_dict,character):
  #Display attributes of chosen character
  
  print(char_dict[character]["stats"])
  #Input for user to choose if they want to change any of them
  
  use = input("Would you like to change any of the attributes? (y/n): ").strip().lower()
  #if yes
  if use == "y":
    #for each attribute
    for x in char_dict[character]["stats"]:
      #display the attribute
      print(f"Would you like to change: {char_dict[character]["stats"][x]}")
      #ask user if they want to change that attribute
      change = input("Enter here y/n: ").strip().lower()
      #if yes
      if change == "y":
        #ask for what they want to update the value to
        
        new_value = int(input(f"Enter the number for: {char_dict[character]["stats"][x.keys()]} here: ").strip())
        #Update the value
        char_dict[character]["stats"][x] = new_value
    #display that it is done with the attribute changer
    
    print("attribute changer is done")
  #return character dictionary
  return char_dict

def stat_change(characters,character_name,stat):
  while True:
    
    new_stat = input(f"What do you want to change {stat} to? It cannot go above 20 or below 1.\nEnter here: ").strip()
    
    if new_stat.isnumeric() is False or int(new_stat) > 20 or int(new_stat) < 1:
      
      print("Please enter a valid answer.")
    else:
      
      check = input(f"Are you sure you want to set {stat} to {new_stat}? Y/N: ").strip().capitalize()
      if check == "Y":
        characters[character_name]["Stats"][stat] = int(new_stat)
        break
      else:
        continue

def attribute_inspect(characters,character_name):
  while True:
    print_indict_dictionaries(characters, character_name, type = "Stats")
    
    change = input("Would you like to change any of your attributes? Y/N: ").strip().capitalize()
    if change == "N":
      return
    elif change == "Y":
      
      print("1. Strength\n2. Dexterity\n3. Constitution\n4. Intelligence\n5. Wisdom\n6. Charisma")
      
      stat_to_change = input("Enter number of what stat you want to change:\n").strip()
      match stat_to_change:
        case "1":
          stat_change(characters,character_name,stat = "Strength")
          break
        case "2":
          stat_change(characters,character_name,stat = "Dexterity")
          break
        case "3":
          stat_change(characters,character_name,stat = "Constitution")
          break
        case "4":
          stat_change(characters,character_name,stat = "Intelligence")
          break
        case "5":
          stat_change(characters,character_name,stat = "Wisdom")
          break
        case "6":
          stat_change(characters,character_name,stat = "Charisma")
          break
        case _:
          
          print("Please enter one of the displayed options. 1, 2, 3, 4, 5, or 6.")

