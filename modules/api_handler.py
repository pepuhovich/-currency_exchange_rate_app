import requests

def request_api():
    ''

def get_symbols():
    symbols = []

    # Contacting the API
    response = requests.get('http://data.fixer.io/api/symbols?access_key=ac0abcdec1b89730c3adb9b70801d482')
    # Loading the API response into the dictionary
    load_response = response.json() 
    symbols_dict = load_response['symbols']

    #Parsing dict's keys into the list as case insenstive strings
    symbols_keys = symbols_dict.keys()
    for key in symbols_keys:
        symbols.append(str.casefold(key))

    return symbols
