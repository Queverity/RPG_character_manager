#PS 1st Character inspection

#import from pryors stuff

#import attribute manager
from attribute_management import attribute_inspect
from character_managment import manage_inspect,characters,available_items,items
from UI_liam import print_indict_dictionaries
#function for inventory changer (character chosen, character dictionary)










def inspect_inventory(characters,items, character_name):
    inventory = characters[character_name]["Inventory"]
    print_indict_dictionaries(characters,character_name,type="Inventory")
    while True:
        change = input("Would you like to add or remove items from your inventory? Y/N:\n ").strip().capitalize()
        if change == "Y":
            while True:
                inventory_function = input("Are you adding or removing something? Add/Remove:\n").strip().capitalize()
                
                if inventory_function == "Add":
                    available_items_list = available_items(characters, character_name, items)
                    
                    for i in inventory.keys():
                        if i in available_items_list.keys():
                            available_items_list.pop(i)
                    
                    if len(inventory) == 7:
                        print("Your inventory is at max capacity. You first need to remove something.")
                        continue
                    else:
                        for i in available_items_list:
                            print(i)
                    
                    item_to_add = input("What item would you like to add? Make sure to enter the name exactly as it is in the list.\nEnter here:  ")
                    
                    check = input(f"Are you sure you want to add {item_to_add} to your inventory? Y/N: ").strip().capitalize()
                    
                    if check == "Y":
                        inventory[item_to_add] = available_items_list[item_to_add]
                    break  
                
                elif inventory_function == "Remove":
                    if len(inventory) == 0:
                        print("You have nothing in your inventory to remove. Add something to it first.")
                        break
                    else:
                        for i in inventory:
                            print(i)
                    
                    item_to_remove = input("What item would you like to remove? Enter the name exactly as it is seen on the list.\nEnter here:  ")
                    
                    check = input(f"Are you sure you want to remove {item_to_remove} from your inventory? Y/N: ").strip().capitalize()
                    
                    if check == "Y":
                        inventory.pop(item_to_remove)
                    break  
                else:
                    
                    print("Please enter 'Add' or 'Remove'.")
                    continue
                
        
        elif change == "N":
            break
        
        else:
            
            print("Please enter 'Y' or 'N'.")
            continue

        go_again = input("Would you like to continue with inventory inspection? Y/N:\n")
        if go_again == "Y":
            continue
        else:
            break

        
    return inventory



def character_inspect_menu(characters):
    
    print("Character Names")
    if bool(characters) == False:
        print("You have no characters currently.")
        return
    else:
        for i in characters.keys():
            print(i)
        while True:
            character_name = input("What character do you want to inspect? Enter name exactly as seen on the list: ").strip()
            if character_name not in list(characters.keys()):
                print("Enter a valid name.")
            else:
                while True:
                    inspect_type = input(f"Do you want to inspect {character_name}'s inventory, attributes, skills, or race and class? Enter number:\n1. Inventory\n2. Attributes\n3. Skills\n4. Race and Class\n5. Return to main menu\nEnter here:\n")
                    match inspect_type:
                        case "1":
                            inventory = inspect_inventory(characters, items, character_name)
                            characters[character_name]["Inventory"] = inventory
                        case "2":
                            attribute_inspect(characters,character_name)
                            pass
                        case "3":
                            print_indict_dictionaries(characters,character_name,type = "Skills")
                        case "4":
                            manage_inspect(characters,character_name)
                        case "5":
                            return
                        case _:
                            print("Please enter 1, 2, 3, 4, or 5 as your answer.")
                            continue
                    


    return inventory

