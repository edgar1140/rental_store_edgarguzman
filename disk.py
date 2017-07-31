import core
def in_the_history():
    left = []
    with open('history.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2]), float(split_string[3]), float(split_string[4])])
    return left

def open_inventory():
    inventory = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().replace('$', '').split(', ')
        inventory.append([split_string[0], float(split_string[1]), float(split_string[2]), float(split_string[3]), float(split_string[4])])
    return inventory

# def in_the_inventory():
#     left = []
#     with open('inventory.txt', 'r') as file:
#         file.readline()
#         lines = file.readlines()
#     for line in lines:
#         split_string = line.strip().split(', ')
#         left.append([split_string[0], float(split_string[1]), float(split_string[2])])
#     return left
 
def restock(inventory):
    """ [] -> None
    creates new inventory and writes it to file 
    """
    str_l = ['item, quantity, rental price, deposit, replacement price']
    for item in inventory:
        if int(item[1]) < 100:
            (item[1]) = 100
            item[1] = str(item[1])
            item[2] = str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)  
    with open('inventory.txt', 'w') as file:
        file.write(message)

def takes_away(gear_type, amount):
    str_l = ['item, quantity, rental price, deposit, replacement price']
    left = open_inventory()
    for item in left:
        if item[0] == gear_type:
            if float(amount) > item[1]:
                print('Sorry amount of inventory have been reached, We only have 100 .')
                return False
            else:
                item[1] = float(item[1]) - float(amount)
        item[1] = str(item[1])
        item[2] = str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('inventory.txt', 'w') as file: 
        file.write(message)
    return True

def keeps_history():
    message = '\n{}, {}, ${}'.format(gear,amount,get_gear_type)
    with open('history.txt', 'a') as file:
        file.write(message)

def close_inventory(inventory):
    return None