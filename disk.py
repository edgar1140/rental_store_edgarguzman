def in_the_histoy():
    left = []
    with open('log.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2].strip().replace('$', ''))])
    return left

def in_the_inventory():
    left = []
    with open('tank.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2])])
    return left
 
def refreshes():
    str_l = ['type, amount_in_tank, price']
    for item in left:
        if item[1] < 5000.0:
            item[1] = 5000.0
        item[1]=str(item[1])
        item[2]= str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)  
        return message
    with open('tank.txt', 'w') as file:
        file.write(message)

def takes_away(gas_type, amount):
    str_l = ['type, amount_in_tank, price']
    left = in_the_tank()
    for item in left:
        if item[0] == gas_type:
            if float(amount) > item[1]:
                print('Sorry amount of gas have been reached, We only have 5000.0 gallons.')
                return False
            else:
                item[1] = float(item[1]) - float(amount)
        item[1] = str(item[1])
        item[2] = str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('tank.txt', 'w') as file: 
        file.write(message)
    return True
