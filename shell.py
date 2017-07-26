import core.py
import disk.py

def main():
    msg = ''' Welcome to Chema's DJ Gear Store, What items would you like to purchse?/n
    \t1. JBL dj speakers, $80
    \t2. JBL stage speakers, $120
    \t3. JBL bass stage speakers, $135
    \t4. Numark NVII Dual Display USB DJ Controller, $600
    \t5. Numark Mixtrack Platinum DJ Controller, $185
    pess Q to finish and pay.\n'''
    items = ''
    total_amount = 0
    while items != 'Q':
        items = input(msg)
    if items == '1':
        amount = float(input('What amount would you like to purchase?\n'))
        total_amount += (core.py.count_price(items, amount) * .07)
        Equipment = core.py
        print('Your price will be ${:.2f}'.format(core.py.count_price(items, amount)))
    elif items == '2':
        amount = float(input('What amount would you like to purchase?\n'))
        total_amount += (core.py.count_price(items, amount) * .07)
        print('Your price will be ${:.2f}'.format(core.py.count_price(items, amount)))
    elif items == '3':
        amount = float(input('What amount would you like to purchase?\n'))
        total_amount += (core.py.count_price(items, amount) * .07)
        print('Your price will be ${:.2f}'.format(core.py.count_price(items, amount)))
    elif items == '4':
        amount = float(input('What amount would you like to purchase?\n'))
        total_amount += (core.py.count_price(items, amount) * .07)
        print('Your price will be ${:.2f}'.format(core.py.count_price(items, amount)))
    elif items == '5':
        amount = float(input('What amount would you like to purchase?\n'))
        total_amount += (core.py.count_price(items, amount) * .07)
        print('Your price will be ${:.2f}'.format(core.py.count_price(items, amount)))
    else:
            print('Sorry invalid option')

    print('Thank you, Have a nice day!:)')



if __name__ == '__main__':
    main()







def main():
    msg = '''What items would you like to purchase?\n
    \t1. Apples.$0.75
    \t2. lemons.$0.50
    \t3. Mangos $0.99
    \t4. Oranges $0.75
    press Q to finish and pay.\n '''
    items = ''
    total_amount = 0
    while items != 'Q':
        items = input(msg)
        if items == '1':
            amount = int(input('What amount would you like purchse?\n'))
            total_amount += (store_program_core.count_price(items, amount) * 1.07)
            fruits = store_program_core
            print('Your price will be ${:.2f}'.format(store_program_core.count_price(items,amount))) 
        elif items == '2':
            amount = int(input('What amount would you like purchse\n'))
            total_amount += (store_program_core.count_price(items, amount) * 1.07)
            print('Your price will be ${:.2f}'.format(store_program_core.count_price(items,amount))) 
        elif items == '3':
            amount = int(input('What amount would you like purchse?\n'))
            total_amount += (store_program_core.count_price(items, amount) * 1.07)
            print('Your price will be ${:.2f}'.format(store_program_core.count_price(items,amount))) 
        elif items == '4':
            amount = int(input('What amount would you like purchse?\n'))
            total_amount += (store_program_core.count_price(items, amount) * 1.07)
            print('Your price will be ${:.2f}'.format(store_program_core.count_price(items,amount))) 
        elif items == 'Q':
            print("Your total amount will be  ${:.2f}".format(total_amount))
        else:
            print('Sorry invalid option')

    print('Thank you, Have a nice day!:)')



if __name__ == '__main__':

     main()

        


