languages = ["English", "Spanish", "Turkish", "Italian", "Chinese"]

def select_language(selection):
    if selection in languages:
        print(f'You selected: {selection}.')
    else:
        print(f'{selection} is not available.')
selection = input('Please, select a language: ')
select_language(selection)