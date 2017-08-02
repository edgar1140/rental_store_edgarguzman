import core



def open_inventory():
    inventory = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().replace('$', '').split(', ')
        inventory.append([split_string[0], float(split_string[1]), float(split_string[2]), float(split_string[3]), float(split_string[4]), float(split_string[5])])
    return inventory

def restock(gear_type, how_much):
    """ [] -> None
    creates new inventory and writes it to file 
    """
    str_l = ['gear_type, amount, price, deposit, replacement, gear number']
    inventory = open_inventory()
    for item in inventory:
        if item[0] == gear_type:
            (item[1]) = int(how_much) + int(item[1])
        item[1] = str(item[1])
        item[2] = str(item[2])
        item[3] = str(item[3])
        item[4] = str(item[4])
        item[5] = str(item[5])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)  
    with open('inventory.txt', 'w') as file:
        file.write(message)



def takes_away(gear_type, amount):
    str_l = ['gear_type, amount, price, deposit, replacement, gear number']
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
        item[3] = str(item[3])
        item[4] = str(item[4])
        item[5] = str(item[5])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('inventory.txt', 'w') as file: 
        file.write(message)
    return True




def keeps_history(gear_type, price):
    message = '\n{}, ${:.2f}'.format(gear_type, price)
    with open('history.txt', 'a') as file:
        file.write(message)
    
def in_the_history():
    left =[]
    with open('history.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]).strip().replace('$', '')])
    return left