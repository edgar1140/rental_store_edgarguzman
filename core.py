def count_price(items, amount):
    """ (float) -> (float)
    Adds up the price of the amount of items of the purachase.
    Reurns the total price.
    """
    JBL DJ speakers, 80
    JBL stage speakers, 120
    JBL bass stage speakers, 135
    Numark NVII Dual Display USB DJ Controller, 600
    Numark Mixtrack Platinum DJ Controller, 185

    if  items == '1':
        return float(JBL DJ speakers * amount)
    elif  items == '2':
        return float(JBL stage speakers * amount) 
    elif  items == '3':
        return float(JBL bass stage speakers * amount) 
    elif  items == '4':
        return float(Numark NVII Dual Display USB DJ Controller * amount) 
    elif  items == '5':
        return float(Numark Mixtrack Platinum DJ Controller * amount) 

def make_inventory():
    """ () -> List[(str, int)]
    Take the file an return the file into a list

    >>> make_inventory()
    [['JBL DJ speakers, 80], [JBL stage speakers, 120], [JBL bass stage speakers, 135], 
    [ Numark NVII Dual Display USB DJ Controller, 600], [Numark Mixtrack Platinum DJ Controller, 185]]
    """
    Equipment = []
    with open('inventory.txt', 'r') as file:
        for each in friuts:
        split_string = line.split(', ')
        Equipment.append([split_string[0], int(split_string[1])])
    return Equipment

def pretty_inventory(Equipment):
    """ list -> str
    Take the list and retrns it back to a string

    >>> pretty_incentory(Equipment)
    1. Apples (20) 
    2. lemons (30) 
    3. Mangos (20) 
    4. Oranges (20)
    """
    message = ''
    c = 1
    for item in Equipment:
        message += '{0}. {1} ({2})\n'.format(c,item[0].title(),item[1])

    return message


    
