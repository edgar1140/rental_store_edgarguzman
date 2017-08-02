def gear_price(gear, amount):
    """ str -> Float"""
    if gear == '1':
        return float(amount) * 80 * 1.07
    elif gear == '2':
        return float(amount) * 120 * 1.07
    elif gear == '3':
        return float(amount) * 135 * 1.07
    elif gear == '4':
        return float(amount) * 125 * 1.07 
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

def actual_price(gear):
    """actual price """
    if gear == '1' or gear.lower() == 'one':
        return float(350)
    elif gear == '2' or gear.lower() == 'two':
        return float(750)
    elif gear == '3' or gear.lower() == 'three':
        return float(750)
    elif gear == '4' or gear.lower() == 'four':
        return float(600)
    elif gear == '5' or gear.lower() == 'five':
        return float(600)

    

def deposit(gear_type):
    '''deeposit for each item
    >>> deposit('1')
    35.0
    >>> deposit('2')
    75.0
    '''
    gears = (float(gear_type) * float(0.10))
    return round(gears, 2)