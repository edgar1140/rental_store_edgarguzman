import core
import disk

def main():
    print('Welcome to Chemas DJ Gear Store. ', end='')
    msg = ''' What items would you like to purchse?/n'
    \t1. djspeakers, $80\n
    \t2. stagespeakers, $120\n
    \t3. subspeakers, $135\n
    \t4. djController, $600\n
    \t5. mixingboards, $185\n
    pess Q to finish and pay.\n'''
    while True:
        gear = input(msg)
        if gear.lower() == 'refresh':
            left = disk.in_the_history()
            core.restock(left)
            history = disk.keeps_history(gear, amount, get_gear_type)
            take_out = disk.takes_away(get_gear_type, amount)
            print('refreshed.')
            return None
        if gear.lower() == 'track':
            left = disk.in_the_history()
            print('your total sales are  ${:.2f}'.format(core.track_history(left)))
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
    core.keep_history(gear,amount, gear_type)
    print('Thank you for shopping with us today! Have a nice day!!')


if __name__ == '__main__':
    main()
