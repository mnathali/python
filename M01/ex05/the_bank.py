class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

        def transfer(self, amount):
            self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account) or \
            new_account.name in map(lambda x: x.name, self.accounts):
            return False
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        # ... Your code ...
        accs = list(filter(lambda x: x.name in (origin, dest), self.accounts))
        if amount < 0 or origin == dest or len(accs) != 2:
            return False
        acc = list(filter(lambda x: x.name == origin, accs))[0]
        dst = list(filter(lambda x: x.name == dest, accs))[0]
        if len(vars(acc)) % 2 == 0 or len(vars(dst)) % 2 == 0 or \
        'b' in map(lambda x: x[0], list(vars(acc).keys()) + list(vars(dst).keys())) or \
        any(map(lambda x: x.startswith('zip') or x.startswith('addr'), vars(acc).keys() + vars(dst).keys())) or \
        {'name', 'id', 'value'} not in set(vars(acc).keys) or {'name', 'id', 'value'} not in set(vars(dst).keys) or \
        amount > acc.value or \
        type(acc.name) != type(str) or type(dst.name) != type(str) or \
        type(acc.value) != type(float) or type(dst.value) != type(float) or \
        type(acc.id) != type(int) or type(dst.id) != type(int):
            return False
        acc.value -= amount
        dst.value += amount
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """
        pass
    # ... Your code ...


if __name__ == "__main__":
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        bref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation'
    ))

    if bank.transfer('William John', 'Smith Jane', 545.0) is False:
        print('Failed')
    else:
        print('Success')


lst = ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

print(*lst, sep='\n')