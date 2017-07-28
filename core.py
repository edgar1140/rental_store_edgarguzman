def gear_price(gear, amount):
    """ str -> Float"""
    if gear == '1':
        return float(amount) * 1.17
    elif gear == '2':
        return float(amount) * 1.20
    elif gear == '3':
        return float(amount) * 2.50
    elif gear == '4':
        return float(amount) * 333333
    elif gear == '5':
        return float(amount) * 333333

def get_gear_type(gear):
    """(str, float) --> str"""
    if gear == '1' or gear.lower() == 'one':
        gear_type = 'Regular'
    elif gear == '2' or gear.lower() == 'two':
        gear_type = 'Midgrade'
    elif gear == '3' or gear.lower() == 'three':
        gear_type = 'Premium'
    elif gear == '4' or gear.lower() == 'four':
        gear_type = """"""
    elif gear == '5' or gear.lower() == 'five':
        gear_type == """""""
    return gear_type

def keep_history(gear,amount, gear_type):
    price = gear_price(gear, amount)
    history = disk.keep_history(gear,amount,get_gear_type)
    return history


def revenue_history(left):
    """ return float value of total dollars spent"""
    
    price = 0 
    for item in left:
        price += item[2]
    return price
   


def take_away(get_gear_type, amount):
    take_out = disk.takes_away(get_gear_type, amount)
    return take_out

def restock(left):
    refresh = disk.restock(left)
    return refresh

    