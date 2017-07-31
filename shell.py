import core
import disk

def main():
    inventory = disk.open_inventory()
    history = disk.in_the_history()
    
    print('Welcome to Chemas DJ Gear Store. ', end='')
    msg = ''' What items would you like to rent?'
    \t1. djspeakers, $80\n
    \t2. stagespeakers, $120\n
    \t3. subspeakers, $135\n
    \t4. djController, $600\n
    \t5. mixingboards, $185\n
    press Q to finish and pay.\n'''
    while True:
        gear = input(msg)
        if gear.lower() == 'refresh':
            disk.refresh(inventory)
            print('refreshed.')
            exit()
        if gear.lower() == 'track':
            print('your total sales are  ${:.2f}'.format(core.track_history(history)))
            return None
        if gear == '1' or gear.lower() == 'one' or gear == '2' or gear.lower() == 'two' or gear == '3' or gear.lower() == 'three' or '4' or gear.lower() == 'four' or '5' or gear.lower () == 'five':
            break

        else:
            print('Sorry, invalid choice!')
    amount = input('What quantity would you like? ')
    if not amount.strip().isnumeric():
        print('Sorry, invalid choice!')
        return None

    
    gear_type = core.get_gear_type(gear)
    if not core.take_away(gear, gear_type, amount):
        print('Please come back later.')
        return None
    
    print('Your total will be ${:.2f}'.format(core.gear_price(gear, amount)))
    core.keep_history(history, gear, amount, gear_type)
    disk.close_inventory(inventory)
    print('Thank you for shopping with us today! Have a nice day!!')


if __name__ == '__main__':
    main()
