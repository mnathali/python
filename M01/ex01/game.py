
class GotCharacter:
    def __init__(self, name, is_alive = True):
        self.first_name = name
        self.is_alive = True


class Stark(GotCharacter):
    def __init__(self, name = None, is_alive = True):
        super().__init__(name, is_alive)
        self.family_name = 'Stark'
        self.house_words = 'Winter is Coming'

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False