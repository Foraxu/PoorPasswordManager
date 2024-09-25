import random

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
LETTERS_CAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SPECIAL_CHARACTERS = '!@#$%?}{][&*()_'

class PasswordGenerator():
    def __init__(self, numbers: int = 4, letters: int = 3, capital_letters: int = 3, special_characters: int = 4):
        self.letters = [letter for letter in LETTERS]
        self.letters_cap = [letter for letter in LETTERS_CAP]
        self.numbers = [number for number in NUMBERS]
        self.special_characters = [character for character in SPECIAL_CHARACTERS]

        self.numbers_amount = numbers
        self.letters_amount = letters
        self.capital_amount = capital_letters
        self.special_amount = special_characters
        
    def create_random_password(self):
        random_items = []
        password_list = []
        password = ''
        
        random_items += [random.choice(self.letters) for i in range(self.letters_amount)]
        random_items += [random.choice(self.letters_cap) for i in range(self.capital_amount)]
        random_items += [random.choice(self.numbers) for i in range(self.numbers_amount)]
        random_items += [random.choice(self.special_characters) for i in range(self.special_amount)]

        for i in range(len(random_items)):
            item = random.choice(random_items)
            random_items.remove(item)
            password_list.append(item)

        password = ''.join(password_list)
        
        return password
