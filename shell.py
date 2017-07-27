import core.py
import disk.py

def main():
    print('Welcome to Chemas DJ Gear Store. ', end='')
   msg = ''' What items would you like to purchse?/n'
    \t1. JBL DJ speakers, $80\n
    \t2. JBL stage speakers, $120\n
    \t3. JBL bass stage speakers, $135\n
    \t4. Numark NVII Dual Display USB DJ Controller, $600\n
    \t5. Numark Mixtrack Platinum DJ Controller, $185\n
    pess Q to finish and pay.\n'''
    while items != 'Q':
        items = input(msg)
    if items == '1'or items.lower() == 'one':
        amount = float(input('What amount would you like to purchase?\n'))
        total_amount += (core.py.count_price(items, amount) * 1.07)
        Equipment = core.py
        print('Your price will be ${:.2f}'.format(core.py.count_price(items, amount)))
    elif items == '2' or items.lower() == 'two': 
        amount = float(input('What amount would you like to purchase?\n'))
        total_amount += (core.py.count_price(items, amount) * 1.07)
        print('Your price will be ${:.2f}'.format(core.py.count_price(items, amount)))
    elif items == '3' or items.lower() == 'three':
        amount = float(input('What amount would you like to purchase?\n'))
        total_amount += (core.py.count_price(items, amount) * 1.07)
        print('Your price will be ${:.2f}'.format(core.py.count_price(items, amount)))
    elif items == '4' or items.lower() == 'four':
        amount = float(input('What amount would you like to purchase?\n'))
        total_amount += (core.py.count_price(items, amount) * 1.07)
        print('Your price will be ${:.2f}'.format(core.py.count_price(items, amount)))
    elif items == '5' or items.lower() == 'five':
        amount = float(input('What amount would you like to purchase?\n'))
        total_amount += (core.py.count_price(items, amount) * 1.07)
        print('Your price will be ${:.2f}'.format(core.py.count_price(items, amount)))
    else:
            print('Sorry invalid option')

    print('Thank you, Have a nice day!:)')

    



if __name__ == '__main__':
    main()


   def main():
    print('Hello! welcome to Juan Way Gas Station. ', end='')
    
    msg = '''Which type of gass would you like?
    \t1. Regular $1.17\n
    \t2. Midgrade $1.20\n
    \t3. Premium $2.50\n '''
    while True:
        gas = input(msg)
        if gas.lower() == 'refuel':
            left = Juan_Way_disk.in_the_tank()
            Juan_Way_Gas_Core.refill(left)
            print('Tanks refueled.')
            return None
        if gas.lower() == 'revenue':
            left = Juan_Way_Gas_disk.in_the_log()
            print('your total revenue is ${:.2f}'.format(Juan_Way_Gas_Core.revenue_log(left)))
            return None
        if gas == '1' or gas.lower() == 'one'or gas == '2' or gas.lower() == 'two' or gas == '3' or gas.lower() == 'three':
            break

        else:
            print('Sorry, invalid choice!')
    amount = input('How many gallons would you like? ')
    if not amount.strip().isnumeric():
        print('Sorry, invalid choice!')
        return None

    
    gas_type = Juan_Way_Gas_Core.get_gas_type(gas)
    if not Juan_Way_Gas_Core.take_away(gas_type, amount):
        print('Please come back later.')
        return None
    
    print('Your total will be ${:.2f}'.format(Juan_Way_Gas_Core.gas_price(gas, amount)))
    Juan_Way_Gas_Core.keep_log(gas, amount, gas_type)
    print('Thank you for shopping with us today! Have a nice day!!')


if __name__ == '__main__':
    main()



        


