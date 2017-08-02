import core
import disk

def main():
    inventory = disk.open_inventory()
    
    print('Welcome to Chemas DJ Gear Store. ', end='')
    msg = ''' Would you like to rent or return items?'
    \t1. djspeakers, $80\n
    \t2. stagespeakers, $120\n
    \t3. subspeakers, $135\n
    \t4. djController, $125\n
    \t5. mixingboards, $185\n
    press Q to finish and pay.\n'''
    while True:
        gear = input(msg)
        if gear.lower() == 'return':
            gear = input('What gear are you returning? From options 1-5\n')
            gear_type = core.get_gear_type(gear)
            gears = core.actual_price(gear)
            how_much = input('How many of this Items are you returning?\n')
            in_all = float(how_much) * float(gears)
            deposit = core.deposit(in_all)
            disk.restock(gear_type, how_much)
            print('Thank you, your deposit back is $' + str(float(deposit)))
            return None 

            # exit()
        if gear.lower() == 'track':
            print('your total sales are  ${:.2f}'.format(disk.keeps_history(gear_type, price)))
        
            return None
        if gear == '1' or gear.lower() == 'one' or gear == '2' or gear.lower() == 'two' or gear == '3' or gear.lower() == 'three' or '4' or gear.lower() == 'four' or '5' or gear.lower () == 'five':
            break

        else:
            print('Sorry, invalid choice!')
    amount = input('What amount would you like? ')
    if not amount.strip().isnumeric():
        print('Sorry, invalid choice!')
        return None

    gear_type1 = core.actual_price(gear)
    gear_type = core.get_gear_type(gear)
    if not disk.takes_away(gear_type, amount):
        print('Please come back later.')
        return None
    
    price = core.gear_price(gear, amount)
    deposit = core.deposit(gear_type1)
    total_all = core.gear_price(gear, amount) + (float(deposit))
    print('Your total will be ${:.2f}'.format(total_all))
    disk.keeps_history(gear_type, price)
    print('Thank you for shopping with us today! Have a nice day!!')


if __name__ == '__main__':
    main()
