def count_price(items, amount):

    """ (float) -> (float)
    Adds up the price of the amount of items of the purachase.
    Reurns the total price.
    """
    djspeakers = 80
    stagespeakers = 120
    subspeakers = 135
    djController = 600
    mixingboard = 185

    if  items == '1'
        return float(djspeakers * amount)
    elif  items == '2':
        return float(stagespeakers * amount) 
    elif  items == '3':
        return float(subspeakers * amount) 
    elif  items == '4':
        return float(djController * amount) 
    elif  items == '5':
        return float(mixingboard * amount)

def make_inventory():
    """ () -> List[(str, int)]
    Take the file an return the file into a list

    >>> make_inventory()
    [[djspeakers = 56], [stagespeakers = 60], [subspeakers = 60], 
    [ djController = 20], [mixingboard = 23]]
    """
    Equipment = []
    with open('inventory.txt', 'r') as file:
        for each in Equipment:
            split_string = line.split(', ')
            Equipment.append([split_string[0], int(split_string[1])])
        return Equipment

def pretty_inventory(Equipment):
    """ list -> str
    Take the list and retrns it back to a string

    >>> pretty_incentory(Equipment)
    1. djspeakers, 56
    2. stagespeakers, 60
    3. subspeakers, 60
    4. djController, 20
    5. mixingboard, 23

    """
    message = ''
    c = 1
    for item in Equipment:
        message += '{0}. {1} ({2})\n'.format(c,item[0].title(),item[1])

    return message
    
