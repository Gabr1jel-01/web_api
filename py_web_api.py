import requests
import json

def display_user(response.text):
    pass


while True:
    user_id = int(input('Upisite ID korisnika kojeg zelite dohvatiti: '))

    URL = f'https://jsonplaceholder.typicode.com/users/{user_id}'

    try:
        response = requests.get(URL)

        if response.status_code == 200:
            display_user(response.text)
            
        elif response.status_code == 404:
            print(f'Ne postoji trazeni dokument. Greska: {response.status_code}')
            
        else:
            print(f'Dogodila se greska: {response.status_code}')

    except Exception as ex:
        print(f'Dogodila se greska: {ex}')
        
    next_cycle = input('Zelite li ponoviti upit ')
    if next_cycle.lower() != 'da':
        break