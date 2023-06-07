
from modules.input import get_input, verify_input, print_rate








while True:
    
    first_currency, second_currency = get_input()[0:2]
    

    if verify_input(first_currency, second_currency):
        print_rate(first_currency, second_currency)
   
    
    else:
        print('Wrong input!')



    
    
        