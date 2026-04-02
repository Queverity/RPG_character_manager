# CB 1st Item Class

import csv

# class Item:
    # define method __init__(self):
        # attributes for items will be name, id, description, value, weight, and class_requirement

    # define method __str__(self):
        # print out name, id, and description 

# define function load_items(items_csv):
    # items_list = []
    # after loading string from items csv, take info and turn each row into an item object
    # append each object to items list, then return items_list

# define function create_item():
    # have user enter data for each attribute of a item object (make sure id isn't already taken)
    # first take object and save to item list, then save to item csv

class Item:
    def __init__(self,name,id,description,value,weight,class_requirement):
        self.name = name
        self.id = id
        self.description = description
        self.value = value
        self.weight = weight
        self.class_requirement = class_requirement

    def __str__(self):
        return f"{self.name} ({self.id}): {self.description} | Value: {self.value} | Weight: {self.weight}"
    
def load_items(items):
    items_list = []
    for _ in items:
        item_object = Item(items['item_name'],items['item_id'],items['description'],items['value'],items['weight'],items['class_requirement'])
        items_list.append(item_object)

    return items_list

def create_item(items_list):
    available_classes = ['Rouge','Fighter','Barbarian','Bard','Wizard','Sorcerer','Warlock','All']
    name = input("Enter name for item:\n").strip()
    description = input("Enter description for item:\n").strip()

    while True:
        class_requirement = input("Please enter the required class to use this item. If any class could use this item, enter 'All'.").strip().capitalize()

        if class_requirement not in available_classes:
            print("Please enter a valid class.")
            continue

        break


    while True:
        value = input("Enter value in gold for item:\n").strip()
        try:
            value = int(value)
            break
        except:
            print("Please enter a number.")
            continue

    while True:
        weight = input("Enter weight in pounds for item:\n").strip()
        try:
            weight = int(weight)
            break
        except:
            print("Please enter a number.")
            continue

    while True:
        id = input("Enter ID for item (3-letter combination):\n").strip().lower()
        if len(id) > 3:
            print("Please enter 3 letters for the item id.")
            continue

        for i in items_list:
            if i.id.lower() == id:
                print("There is already an item with that id saved. Please enter a different id.")
                continue
        
        break

    item_object = Item(name,id,description,value,weight,class_requirement)
    items_list.append(item_object)
    try:
        with open('documents/items.csv',mode='a',newline="") as items:
            fieldnames = ['name','id','description','value','weight','class_requirement']
            writer = csv.DictWriter(items,fieldnames)

            writer.writerow(vars(item_object))
    except:
        print("Failed to create item; Unexpected error has occured")
        return
    else:
        print("Item created and saved succesfully!")
        # after_action()
        return

    
