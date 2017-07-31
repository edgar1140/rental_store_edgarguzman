def gear_price(gear, amount):
    """ str -> Float"""
    if gear == '1':
        return float(amount) * 80 * 1.07
    elif gear == '2':
        return float(amount) * 120 * 1.07
    elif gear == '3':
        return float(amount) * 130 * 1.07
    elif gear == '4':
        return float(amount) * 600 * 1.07 
    elif gear == '5':
        return float(amount) * 185 * 1.07

def get_gear_type(gear):
    """(str, float) --> str"""
    if gear == '1' or gear.lower() == 'one':
        gear_type = 'djspeakers'
    elif gear == '2' or gear.lower() == 'two':
        gear_type = 'stagespeakers'
    elif gear == '3' or gear.lower() == 'three':
        gear_type = 'subspeakers'
    elif gear == '4' or gear.lower() == 'four':
        gear_type = 'djcontroller'
    elif gear == '5' or gear.lower() == 'five':
        gear_type == 'mixingboard'
    return gear_type

def keep_history(history, gear, amount, gear_type):
    price = gear_price(gear, amount)
    return history


def track_history(left):
    """ return float value of total dollars spent"""
    
    price = 0 
    for item in left:
        price += item[2]
    return price
   


def take_away(take_out, get_gear_type, amount):
    return take_out

def restock(left):
    refresh = disk.restock(left)
    return refresh

    