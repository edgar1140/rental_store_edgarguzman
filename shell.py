import core.py
import disk.py

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
        equipment = input(msg)
        if equipment.lower() == 'refresh':
            left = disk.in_the_history()
            Core.refresh(left)
            print('refreshed.')
            return None
        if gas.lower() == 'track':
            left = disk.in_the_history()
            print('your total sales are  ${:.2f}'.format(Core.track_history(left)))
            return None
        if gas == '1' or equipment.lower() == 'one'or gas == '2' or equipment.lower() == 'two' or gas == '3' or equipment.lower() == 'three':
            break

        else:
            print('Sorry, invalid choice!')
    amount = input('What quantity would you like? ')
    if not amount.strip().isnumeric():
        print('Sorry, invalid choice!')
        return None

    
    gas_type = Core.get_gear_type(gear)
    if not Core.take_away(gear_type, amount):
        print('Please come back later.')
        return None
    
    print('Your total will be ${:.2f}'.format(Core.gear_price(gear, amount)))
    Core.keep_history(gear, amount, gear_type)
    print('Thank you for shopping with us today! Have a nice day!!')


if __name__ == '__main__':
    main()
